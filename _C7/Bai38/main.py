""" 
Có nhiều mode để có thể đọc ghi file:
- "r": Đọc file
- "w": Ghi file
- "a": Ghi thêm vào file
- "r+": Đọc và ghi file
- "w+": Ghi và đọc file
- "a+": Ghi thêm và đọc file
- "x": Tạo file mới và ghi file
- "t": Mở file ở mode text (mặc định)
- "b": Mở file ở mode binary        
"""

file = open("data.txt", "r", encoding="utf-8")
data = file.read() # Đọc toàn bộ file
print(data)
file.close() # Đóng file