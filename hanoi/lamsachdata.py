import pandas as pd
import re

# 1. ĐỌC FILE DỮ LIỆU ĐÃ GỘP
print("Đang đọc dữ liệu...")
df = pd.read_csv('Du_lieu_Hanoi_TongHop.csv')

# 2. CHUẨN HÓA THỜI GIAN
print("Đang xử lý cột thời gian...")
# Chuyển đổi sang dạng ngày tháng chuẩn
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
# Sắp xếp dữ liệu từ cũ đến mới
df = df.sort_values('timestamp').reset_index(drop=True)
# Trích xuất thêm cột ngày, giờ, tháng để tiện phân tích sau này
df['date'] = df['timestamp'].dt.date
df['hour'] = df['timestamp'].dt.hour
df['month'] = df['timestamp'].dt.month

# 3. LÀM SẠCH TỐC ĐỘ GIÓ VÀ ĐỘ ẨM (Bỏ chữ, chuyển thành số)
print("Đang làm sạch tốc độ gió và độ ẩm...")
df['wind_speed'] = df['wind_speed'].astype(str).str.replace(' km/h', '', regex=False).astype(float)
df['humidity'] = df['humidity'].astype(str).str.replace('%', '', regex=False).astype(float)

# 4. TRÍCH XUẤT TRẠNG THÁI THỜI TIẾT
print("Đang trích xuất trạng thái thời tiết...")
# Hàm này bóc tách tên thời tiết từ cái link ảnh dài ngoằng
def extract_weather(icon_str):
    try:
        match = re.search(r'ic-w-\d+-(.*?)-full\.svg', str(icon_str))
        if match:
            return match.group(1).replace('-', ' ').title() # Ví dụ: scattered-clouds -> Scattered Clouds
        return str(icon_str).split('/')[-1]
    except:
        return 'Unknown'

df['weather'] = df['weather_icon'].apply(extract_weather)
df = df.drop(columns=['weather_icon']) # Xóa cột link ảnh cũ cho nhẹ file

# 5. LƯU KẾT QUẢ
output_file = 'Du_lieu_Hanoi_Cleaned.csv'
df.to_csv(output_file, index=False)

print(f"\n✅ THÀNH CÔNG! Đã làm sạch và lưu thành file: {output_file}")
print("-" * 40)
print("Xem trước 5 dòng dữ liệu đã sạch sẽ:")
print(df.head())