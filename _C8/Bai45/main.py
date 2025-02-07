import os

NAME_OF_FOLDER = os.path.dirname(os.path.abspath(__file__))

class Video:
    def __init__(self, title: str, length: str):
        self.title = title
        self.length = length

def write_to_file(filename: str, videos = "", path: str = "") -> None:
    if not path:
        path = make_folder("Data")
    
    if not filename.endswith(".txt"):
        filename += ".txt"
    
    file_path = os.path.join(path, filename)
    
    with open(file_path, "w") as file:
        totalVideo = len(videos)
        file.write(f"Total videos: {totalVideo}\n")
        for video in videos:
            file.write(f"{video.title} {video.length}\n")

def read_file(filename: str, path: str = "") -> list[Video]:
    if not path:
        path = make_folder("Data")
    
    if not filename.endswith(".txt"):
        filename += ".txt"
    
    file_path = os.path.join(path, filename)
    
    with open(file_path, "r") as file:
        return file.read()

def make_folder(folder_name: str, path: str = "") -> str:
    if not path:
        path = NAME_OF_FOLDER
    
    folder_path = os.path.join(path, folder_name)
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    return folder_path

def read_video() -> Video:
    title = input("Nhap title: ")
    length = input("Nhap link: ")
    return Video(title, length)

def read_videos() -> list[Video]:
    videos = []
    total_videos = int(input("Nhap so luong video: "))
    for _ in range(total_videos):
        videos.append(read_video())
    return videos

def print_video(video: Video) -> None:
    print(video.title, video.length)

def print_videos(videos: list[Video]) -> None:
    for video in videos:
        print_video(video)

def main() -> None:
    print(read_file("Videos"))
    
    # videos = read_videos()
    # print_videos(videos)
    # write_to_file("Videos", videos)

if __name__ == "__main__":
    main()
