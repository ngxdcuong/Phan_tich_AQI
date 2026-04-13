import pandas as pd
import glob

# Tìm tất cả file .csv trong thư mục đang mở
file_list = glob.glob("*.csv")

print(f"Đang tìm thấy {len(file_list)} file CSV. Bắt đầu gộp...")

dataframes = []
for file in file_list:
    df = pd.read_csv(file)
    dataframes.append(df)

# Gộp tất cả các bảng lại với nhau
if len(dataframes) > 0:
    df_master = pd.concat(dataframes, ignore_index=True)
    
    # Lưu kết quả thành một file CSV mới
    output_name = "Du_lieu_Hanoi_TongHop.csv"
    df_master.to_csv(output_name, index=False)
    
    print(f"Đã hoàn thành! Kết quả được lưu tại: {output_name}")
    print(f"Tổng số dòng dữ liệu hiện có: {df_master.shape[0]}")
else:
    print("Không tìm thấy file CSV nào trong thư mục này. Vui lòng kiểm tra lại!")