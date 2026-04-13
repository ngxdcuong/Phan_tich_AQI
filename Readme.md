# Đề tài: Phân tích Dữ liệu Chất lượng Không khí (AQI) tại Hà Nội

**Môn học:** Lập trình Python  
**Nhóm thực hiện:** Nhóm ... (Điền tên nhóm của bạn vào đây)

## Thành viên nhóm và Phân công
1. **[Nguyễn Đức Cường] - MSV: [20222582]** - Trưởng nhóm, phụ trách Thu thập & Tiền xử lý dữ liệu (Data Cleaning).
2. **[Nguyễn Hữu Sơn] - MSV: [20220667]** - Trực quan hóa (Visualization).
3. **[Hoàng Thị Thảo Vân] - MSV: [20221498]** - Phụ trách Khám phá dữ liệu (EDA).

---

## Tổng quan dự án
Dự án được thực hiện nhằm đánh giá thực trạng ô nhiễm không khí tại khu vực Hà Nội thông qua việc phân tích dữ liệu quan trắc thực tế từ năm 2025 - 2026. Dự án tập trung vào việc làm sạch dữ liệu, trực quan hóa các xu hướng ô nhiễm theo thời gian và tìm ra mối tương quan giữa chỉ số AQI với các yếu tố thời tiết (Độ ẩm, Tốc độ gió).

### Các nội dung chính đã thực hiện:
1. **Tiền xử lý dữ liệu (Data Preprocessing):**
   - Hợp nhất các file CSV đơn lẻ thành bộ dữ liệu chuẩn gồm **5.632 dòng** quan trắc.
   - Chuẩn hóa cột thời gian (Datetime), bóc tách các đặc trưng như Giờ, Tháng.
   - Làm sạch và ép kiểu số liệu cho các yếu tố khí tượng (loại bỏ ký tự `%`, `km/h`).
   - Đảm bảo tập dữ liệu 100% không bị khuyết thiếu (non-null).

2. **Khám phá và Trực quan hóa (EDA & Visualization):**
   - **Phân bố ô nhiễm:** Đánh giá tần suất các ngưỡng AQI để thấy được mức độ cảnh báo tại Hà Nội.
   - **Phân tích chu kỳ:** Sử dụng biểu đồ Boxplot để chỉ ra quy luật ô nhiễm tăng vọt vào ban đêm/rạng sáng (nghịch nhiệt) và giảm vào buổi chiều.
   - **Tương quan khí tượng:** Xây dựng Ma trận tương quan (Heatmap) chứng minh Độ ẩm tỷ lệ thuận và Tốc độ gió tỷ lệ nghịch với sự tích tụ bụi mịn.