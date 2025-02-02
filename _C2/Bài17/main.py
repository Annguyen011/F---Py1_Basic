result = 0

for i in range(3, 100, 2):
    print(i)
    result += float(1/i)
print(round(1/result, 4))