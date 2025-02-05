import os

PATH_OF_DIR = os.path.dirname(os.path.abspath(__file__))

def MakeFolder(name, path):
    folderPath = os.path.join(path, name)
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
    return folderPath

def MakeFileWithContent(name, content="", path=""):
    if path == "":
        path = MakeFolder("Data", PATH_OF_DIR)
    
    if(name.endswith(".txt") == False):
        name += ".txt"
    
    filePath = os.path.join(path, name)
    with open(filePath, "w") as file:
        file.write(content)
        
def main():
    MakeFileWithContent(input("Nhap ten file: "), "hello world")
    
main()