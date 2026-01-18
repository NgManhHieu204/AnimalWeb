import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
import json

# CẤU HÌNH
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, 'dataset')
IMG_SIZE = (128, 128) # Kích thước ảnh
BATCH_SIZE = 32
EPOCHS = 10 # Số lần học

# Kiểm tra xem có dataset chưa
if not os.path.exists(DATASET_PATH):
    print(f"LỖI: Không tìm thấy thư mục '{DATASET_PATH}'. Hãy kiểm tra lại!")
    exit()

# CHUẨN BỊ DỮ LIỆU
print("Đang tải và xử lý dữ liệu ảnh...")
train_datagen = ImageDataGenerator(
    rescale=1./255,       # Chuẩn hóa màu
    rotation_range=20,    # Xoay ảnh ngẫu nhiên để học tốt hơn
    horizontal_flip=True, # Lật ảnh
    validation_split=0.2  # Dành 20% ảnh để kiểm tra
)

train_generator = train_datagen.flow_from_directory(
    DATASET_PATH,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='training'
)

validation_generator = train_datagen.flow_from_directory(
    DATASET_PATH,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='validation'
)

# Lưu lại tên các loài vật
labels = {v: k for k, v in train_generator.class_indices.items()}
print(f"Tìm thấy các loài: {list(labels.values())}")

# XÂY DỰNG MÔ HÌNH CNN
print("Đang xây dựng mô hình CNN...")
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
    MaxPooling2D(2, 2),
    
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(len(labels), activation='softmax') # Lớp đầu ra
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# HUẤN LUYỆN (TRAINING)
print("Bắt đầu huấn luyện...")
history = model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=EPOCHS
)

# LƯU KẾT QUẢ
model.save('animal_model.h5')
print("Đã lưu model: animal_model.h5")

with open('class_indices.json', 'w') as f:
    json.dump(train_generator.class_indices, f)
print("Đã lưu nhãn: class_indices.json")