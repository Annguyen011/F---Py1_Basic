# Đây là file main.py cho Bai42
numsB = []
numsA = []

for i in range(5):
    numsB.append(int(i))

with open("data.txt", "w") as f:
    for num in numsB:
        f.write(str(num) + "\n")

with open("data.txt", "r") as f:
    numsA = (f.read().splitlines())
numsA.sort()
print(numsA)