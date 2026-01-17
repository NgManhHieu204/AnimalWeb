# Animal Recognition Website (Hệ thống Nhận diện Động vật)

Đồ án Thực tập Chuyên ngành Công nghệ Phần mềm
**Sinh viên thực hiện:** Nguyễn Mạnh Hiếu - K225480106020
**GVHD:** ThS. Đỗ Duy Cốp

---

## Giới thiệu
Dự án xây dựng website cho phép người dùng upload ảnh động vật, hệ thống sử dụng trí tuệ nhân tạo (AI/Deep Learning) để nhận diện tên loài vật, độ chính xác và lưu trữ lịch sử tra cứu.

### Công nghệ sử dụng
* **AI Core:** Python, TensorFlow/Keras (CNN - Convolutional Neural Network).
* **Backend:** Python Flask Framework.
* **Frontend:** HTML5, CSS3 (Bootstrap), JavaScript (Chart.js).
* **Database:** MySQL.
* **DevOps & Deployment:** Docker, Docker Compose, Cloudflare Tunnel.

## Cấu trúc dự án
* `src/ai_engine`: Mã nguồn huấn luyện mô hình AI.
* `src/backend`: Mã nguồn server Flask và API.
* `src/frontend`: Giao diện người dùng.
* `docs`: Tài liệu báo cáo và thiết kế hệ thống.

## Tài liệu Thiết kế (Design)
Dự án đã hoàn thành giai đoạn phân tích thiết kế hệ thống:
* [Biểu đồ Use Case](./docs/design/Usecase.png)
* [Sơ đồ ERD](./docs/design/ERD.png)
* [Biểu đồ hoạt động](./docs/design/Hoatdong.png)
* [Biểu đồ tuần tự](./docs/design/Tuantu.png)