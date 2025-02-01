choPhep = False

def check_age_for_movie(age):
    if age < 13:
        choPhep = True
    elif 13 <= age < 18 or choPhep:
        return "Bạn có thể xem phim này với sự giám sát của người lớn."
    else:
        return "Bạn đủ tuổi để xem phim này."

def main():
    try:
        age = int(input("Nhập tuổi của bạn: "))
        result = check_age_for_movie(age)
        print(result)
    except ValueError:
        print("Vui lòng nhập một số hợp lệ.")

if __name__ == "__main__":
    main()