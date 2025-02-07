import os

NAME_OF_FOLDER = os.path.dirname(os.path.abspath(__file__))

def main():
    MakeFile("test1")
    # video = ReadVideos()
    # PrintVideos(video)

class Video:
    def __init__(self, title, length):
        self.title = title
        self.length = length


def MakeFolder(nameFolder, path = ""):
    folderPath = None
    
    if(path == ""):
        path = MakeFolder("Data", NAME_OF_FOLDER)
    
    folderPath = os.path.join(path, nameFolder)
    
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)     
    
    return folderPath
    
def MakeFile(nameFile, content = "", path = ""):
    if(path == ""):
        path = MakeFolder("Data")
    
    if(nameFile.endswith(".txt") == False):
        nameFile += ".txt"
    
    filePath = os.path.join(path, nameFile)
    
    with open(filePath, "w") as file:
        file.write(content)
    
def ReadVideo():
    title = input("Nhap title: ")
    link = input("Nhap link: ")
    return Video(title, link)
    
def ReadVideos():
    videos = []
    totalVideos = int(input())
    for i in range(totalVideos):
        videos.append(ReadVideo())
    return videos
    
def PrintVideo(video):
    print(video.title, video.length)
    
def PrintVideos(videos):
    for video in videos:
        PrintVideo(video)
    
main()