import os
from flask import Flask, request, jsonify, send_from_directory
import mysql.connector
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from dotenv import load_dotenv

# Cấu hình Server & Đường dẫn Frontend
load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_FOLDER = os.path.join(BASE_DIR, '../frontend')
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')

# Khởi tạo Flask với static_folder trỏ về frontend
app = Flask(__name__, static_folder=FRONTEND_FOLDER, static_url_path='')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load Model AI
print("Đang tải Model AI...")
MODEL_PATH = os.path.join(BASE_DIR, '../ai_engine/animal_model.h5')
try:
    model = load_model(MODEL_PATH)
    print("Đã tải Model thành công!")
except Exception as e:
    print(f"Lỗi tải Model: {e}")
    model = None

# Danh sách nhãn
class_names = ['cat', 'chicken', 'cow', 'dog', 'horse']

# Kết nối Database
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )

# R1: Trang chủ
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

# R2: API Nhận diện
@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return jsonify({'error': 'Model chưa sẵn sàng'}), 500

    if 'file' not in request.files:
        return jsonify({'error': 'Không có file gửi lên'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Chưa chọn file'}), 400

    if file:
        # Lưu file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Xử lý ảnh
        try:
            img = image.load_img(filepath, target_size=(128, 128))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array /= 255.0

            # Dự đoán
            predictions = model.predict(img_array)
            predicted_class_idx = np.argmax(predictions[0])
            predicted_label = class_names[predicted_class_idx]
            confidence = float(np.max(predictions[0]))

            # Lưu vào DB
            try:
                conn = get_db_connection()
                cursor = conn.cursor()
                query = "INSERT INTO predictions (filename, filepath, label, confidence) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (filename, filepath, predicted_label, confidence))
                conn.commit()
                cursor.close()
                conn.close()
            except Exception as e:
                print(f"Lỗi lưu DB (Không ảnh hưởng kết quả): {e}")

            return jsonify({
                'label': predicted_label,
                'confidence': confidence,
                'filename': filename
            })

        except Exception as e:
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Website đang chạy tại: http://127.0.0.1:5000")
    app.run(debug=True, port=5000)