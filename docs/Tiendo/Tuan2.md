# Báo cáo Tiến độ Tuần 2 (01/01 - 07/01/2026)

**Họ và tên sinh viên:** Nguyễn Mạnh Hiếu

**Nội dung:** Phân tích, Thiết kế hệ thống và Chuẩn bị dữ liệu.

## 1. Các công việc đã hoàn thành

### Thiết kế hệ thống
Em đã phân tích và xây dựng các biểu đồ kỹ thuật:
1.  **Sơ đồ Use Case:** Xác định 4 chức năng chính (Upload, Nhận diện, Lịch sử, Thống kê).
2.  **Sơ đồ ERD:** Thiết kế bảng `predictions` lưu trữ lịch sử trên MySQL.
3.  **Sơ đồ Tuần tự:** Mô tả luồng xử lý dữ liệu từ Frontend -> Backend -> AI -> Database.
4.  **Sơ đồ Hoạt động:** Xây dựng thuật toán xử lý ảnh và các trường hợp rẽ nhánh (xử lý lỗi, độ chính xác thấp).

### Chuẩn bị Dữ liệu
* **Nguồn dữ liệu:** Sử dụng bộ dữ liệu Animals-10.
* **Xử lý:** Đã chọn lọc 5 loài (Chó, Mèo, Gà, Ngựa, Bò) và chuẩn hóa tên thư mục sang tiếng Anh để phục vụ việc huấn luyện.
* **Tình trạng:** Dữ liệu đã sẵn sàng tại `src/ai_engine/dataset/`.

## 2. Kết quả đạt được
* Các biểu đồ Use Case, ERD, Tuần tự, Hoạt động.
* Folder Dataset đã được chuẩn hóa.

## 3. Kế hoạch tuần tiếp theo (Tuần 3)
* Thiết kế SQL trên hệ quản trị MySQL (Sử dụng Docker).
* Lập trình Python để huấn luyện mô hình CNN (Training Model).
* Xây dựng Backend Flask cơ bản.
* Kết nối Backend với Database MySQL qua Docker.