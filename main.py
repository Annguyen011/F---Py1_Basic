import datetime

CURRENTYEAR = datetime.datetime.now().year

print("Nhap ten")
name = input()
print("Hello " + name.upper())
print("Nhap nam sinh")
year_of_birth = int(input())
age = CURRENTYEAR - year_of_birth
print("Tuoi cua ban la", age)