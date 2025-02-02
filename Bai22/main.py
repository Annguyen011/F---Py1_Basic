def printNumber(a, b):
    if type(a) != int or type(b) != int:
        print("Invalid input")
    
    if type(int(a)) == int and type(int(b)) == int:
        a = int(a)
        b = int(b)
    else: 
        return 

    for i in range(a, b + 1):
        print(i, end = " ")

def tinhTong(a, b):
    sum = 0
    for i in range(a, b + 1):
        sum += i
    return sum

printNumber("1", 10)