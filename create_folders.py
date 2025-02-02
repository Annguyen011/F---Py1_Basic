import os

chuongBatDau = int(input("Nhập chương bắt đầu: "))
chuongKetThuc = int(input("Nhập chương kết thúc: "))

for i in range(chuongBatDau, chuongKetThuc):  # Từ _C3 đến _C4
    os.makedirs(f"_C{i}", exist_ok=True)

print("Thư mục đã được tạo!")
