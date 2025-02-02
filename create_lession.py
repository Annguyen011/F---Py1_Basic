import os

chuongBatDau = int(input("Nhập bài bắt đầu: "))
chuongKetThuc = int(input("Nhập bài kết thúc: "))

for i in range(chuongBatDau, chuongKetThuc + 1):  
    folder_name = f"Bai{i}"
    os.makedirs(folder_name, exist_ok=True)  # Tạo thư mục

    # Tạo file main.py bên trong thư mục
    file_path = os.path.join(folder_name, "main.py")
    with open(file_path, "w") as file:
        file.write("# Đây là file main.py cho " + folder_name)

print("Thư mục và file main.py đã được tạo!")
