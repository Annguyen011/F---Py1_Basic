import os

PATH_OF_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    pass

def MakeFile(name, path):
    folderPath = os.path.join(path, name)
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
    return folderPath

def MakeFileWithContent(name, path, content=""):
    folderPath = os.path.join(path, name)
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
    with open(os.path.join(folderPath, name + ".txt"), "w") as file:
        file.write(content)
    return folderPath
    
    