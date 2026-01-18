import os
from flask import Flask, request, jsonify
import mysql.connector
import tensorflow as tf
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
from dotenv import load_dotenv
import datetime

# Cấu hình
load_dotenv()
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load Model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, '../ai_engine/animal_model.h5')
model = load_model(MODEL_PATH)

# Danh sách nhãn (Khớp thứ tự lúc train)
class_names = ['cat', 'chicken', 'cow', 'dog', 'horse'] 

# Kết nối DB
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )

@app.route('/', methods=['GET'])
def index():
    return jsonify({"status": "Server Ready", "model": "Loaded"})

# API NHẬN DIỆN
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        # Lưu file tạm
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Xử lý ảnh cho AI đọc
        img = image.load_img(filepath, target_size=(128, 128)) # Resize 128x128
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) # Thêm chiều batch
        img_array /= 255.0 # Chuẩn hóa màu 0-1

        # Dự đoán
        predictions = model.predict(img_array)
        score = tf.nn.softmax(predictions[0])
        
        # Lấy kết quả cao nhất
        predicted_class_idx = np.argmax(predictions[0])
        predicted_label = class_names[predicted_class_idx]
        confidence = float(np.max(predictions[0]))

        # Lưu vào MySQL
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "INSERT INTO predictions (filename, filepath, label, confidence) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (filename, filepath, predicted_label, confidence))
            conn.commit()
            cursor.close()
            conn.close()
            print("Đã lưu vào Database!")
        except Exception as e:
            print(f"Lỗi DB: {e}")

        # Trả kết quả về
        return jsonify({
            'label': predicted_label,
            'confidence': confidence,
            'filename': filename
        })

if __name__ == '__main__':
    app.run(debug=True, port=5000)