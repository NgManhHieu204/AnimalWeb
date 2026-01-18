# Báo cáo Tiến độ Tuần 3 (08/01 - 14/01/2026)

**Họ và tên sinh viên:** Nguyễn Mạnh Hiếu

**Nội dung:** Lập trình Cơ sở dữ liệu và Huấn luyện mô hình AI.

## 1. Các công việc đã hoàn thành

### Lập trình Cơ sở dữ liệu
* Đã hiện thực hóa thiết kế ERD thành SQL (`init.sql`).
* Cấu trúc bảng `predictions` đã sẵn sàng để tích hợp vào Docker MySQL.

### Xây dựng và huấn luyện AI
* **Công nghệ:** Sử dụng TensorFlow/Keras xây dựng mạng CNN.
* **Dữ liệu:** Huấn luyện trên bộ dữ liệu 5 loài (Chó, Mèo, Gà, Ngựa, Bò).
* **Kết quả huấn luyện:**
    * Đã tạo thành công file model: `animal_model.h5`.
    * Đã xuất file cấu hình nhãn: `class_indices.json`.
    * Độ chính xác trên tập train đạt: 71.85% - Model ổn định, không bị Overfitting.

### Triển khai Database (Docker)
* Viết cấu hình `docker-compose.yml` cho MySQL.
* Cấu hình Volume để tự động thực thi script `init.sql` khi khởi tạo container.
* Đã triển khai thành công MySQL Container trên môi trường Local.

## 2. Kết quả đạt được
* File mã nguồn: `src/database_scripts/init.sql`
* File mã nguồn: `src/ai_engine/train_cnn.py`
* File Model đầu ra: `animal_model.h5`

## 3. Kế hoạch tuần tiếp theo (Tuần 4)
* Xây dựng Backend Flask (API).
* Viết giao diện Frontend (HTML/JS) để người dùng upload ảnh.
* Tích hợp Model AI vào Website.