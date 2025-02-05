import os


def main():
    path = (os.path.dirname(os.path.abspath(__file__)))
    file_name = input("Nhap ten file ")
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    try: 
        MakeFile(file_name, MakeFolder("Text", path))
    except Exception as e:
        print(e)
        return
    
def MakeFolder(name, path):
    folder_path = os.path.join(path, name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path, exist_ok=True)  # Tạo thư mục
    return folder_path

def MakeFile(name, path):
    if type(path) != str:
        print("Path is not a string")
        return
    
    file_path = os.path.join(path, name)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("\n")

main()
