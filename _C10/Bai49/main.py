# Đây là file main.py cho e:\Ai\DungLai-CoBan\_C10\Bai49
class Video:
    def __init__(self, title, link):
        self.title = title
        self.link = link
    
class Playlist:
    def __init__(self, name, desc, rating, videos):
        self.name = name
        self.desc = desc
        self.rating = rating
        self.videos = videos
    
def ReadVideo():
    title = input("Enter title: ")
    link = input("Enter link: ")
    return Video(title, link)

def PrintVideo(video):
    print("Title: ", video.title, end=", ")
    print("Link: ", video.link, end="")
    
def ReadVideos():
    videos = []
    totalVideo = int(input("Enter number of videos: "))
    for i in range(totalVideo):
        print("Enter video ", i + 1)
        videos.append(ReadVideo())
    return videos

def PrintVideos(videos):
    print("List of videos: ")
    for video in videos:
        PrintVideo(video)
    print()
    
