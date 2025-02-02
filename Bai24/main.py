def tinhTong(a, b):
    a = float(a)
    b = float(b)
    if(type(a) != float or type(b) != float):
        return 0
    return a + b

print(tinhTong("1", 10)) # 11
