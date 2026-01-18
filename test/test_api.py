import requests

# URL của Server
url = 'http://127.0.0.1:5000/predict'

# Lấy ảnh để test
image_path = "E:\\Animal_Project\\src\\ai_engine\\dataset\\cat\\1.jpeg" 

try:
    with open(image_path, 'rb') as f:
        files = {'file': f}
        print(f"Đang gửi ảnh {image_path} lên server...")
        response = requests.post(url, files=files)
        
    print("Kết quả trả về:")
    print(response.json())
except FileNotFoundError:
    print("Lỗi: Không tìm thấy file ảnh để test")
except Exception as e:
    print(f"Lỗi kết nối: {e}")