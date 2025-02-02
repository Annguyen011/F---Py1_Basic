age = int(input("Nhap tuoi: "))

if age < 18:
    print("Ban chua du tuoi de xem phim nay")
elif age >= 18 and age < 25:
    print("Ban da du tuoi de xem phim nay")
else:
    print("Ban qua tuoi de xem phim nay")