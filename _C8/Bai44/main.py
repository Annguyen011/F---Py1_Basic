import os


def main():
    path = (os.path.dirname(os.path.abspath(__file__)))
    MakeFile("data2.txt", MakeFolder("Text", path))
    
    total_video = int(input("Enter total video: "))
    
class Video:
    def __init__(self, title, link):
        self.title = title
        self.link = link
    
    def PrintVideo(video):
        return f"{video.title} - {video.link}"
    
    def PrintVideos(videos):
        return "\n".join([Video.PrintVideo(video) for video in videos])
    
    def ReadVideos(self, videos):
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