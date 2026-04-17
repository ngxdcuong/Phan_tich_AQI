# Đề tài: Phân tích Dữ liệu Chất lượng Không khí (AQI) tại Hà Nội

**Môn học:** Chuyên đề 3
**Nhóm thực hiện:** Nhóm 21

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

3. **Xây dựng mô hình dự báo (Machine Learning Modeling):**
   - **Lựa chọn thuật toán:** Ứng dụng mô hình **Random Forest Regressor** để học các quy luật phức tạp và dự báo chỉ số AQI dựa trên các biến đầu vào (Độ ẩm, Tốc độ gió, Giờ, Tháng).
   - **Huấn luyện và Kiểm thử:** Phân chia bộ dữ liệu theo tỷ lệ chuẩn 80% (Train) để máy học và 20% (Test) để kiểm chứng, đảm bảo mô hình không bị học vẹt (overfitting).
   - **Đánh giá hiệu suất:** Sử dụng các chỉ số thống kê **RMSE** (Root Mean Squared Error) và **R² Score** (Hệ số xác định) để đo lường mức độ sai số và độ tin cậy của dự báo.
   - **Đánh giá mức độ quan trọng (Feature Importance):** Trích xuất và xếp hạng mức độ ảnh hưởng của từng yếu tố khí tượng đối với sự biến thiên của chỉ số ô nhiễm.

4. **Tổng hợp Nhận định và Kết luận (Insights & Conclusions):**
   - **Đặc tính chu kỳ:** Xác nhận tình trạng ô nhiễm tại Hà Nội tuân theo quy luật ngày-đêm. Mức độ ô nhiễm chạm đỉnh vào rạng sáng (do hiện tượng nghịch nhiệt giữ bụi ở tầng thấp) và giảm dần vào buổi chiều.
   - **Tác động của thời tiết:** Độ ẩm và Tốc độ gió là hai nhân tố quyết định. Gió giúp khuếch tán bụi làm giảm ô nhiễm, trong khi độ ẩm cao tạo điều kiện cho các hạt bụi mịn (PM2.5) tích tụ lơ lửng trong không khí.
   - **Tính ứng dụng:** Mô hình học máy đã thiết lập được mối quan hệ logic giữa thời tiết và chất lượng không khí. Kết quả dự án có thể làm cơ sở nền tảng để phát triển các ứng dụng cảnh báo sớm, giúp người dân chủ động sắp xếp lịch trình và bảo vệ sức khỏe.
