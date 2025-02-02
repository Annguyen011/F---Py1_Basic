import os

chuongBatDau = int(input("Nhập bài bắt đầu: "))
chuongKetThuc = int(input("Nhập bài kết thúc: "))
chuong = "_C" +  str(input("Nhập số chương: "))
path = os.path.dirname(os.path.abspath(__file__)) 
path = os.path.join(path, chuong)

for i in range(chuongBatDau, chuongKetThuc + 1):  
    folder_name = os.path.join(path, f"Bai{i}") 
    os.makedirs(folder_name, exist_ok=True)  # Tạo thư mục

    # Tạo file main.py bên trong thư mục với encoding UTF-8
    file_path = os.path.join(folder_name, "main.py")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("# Đây là file main.py cho " + folder_name)

print("Thư mục và file main.py đã được tạo!")
