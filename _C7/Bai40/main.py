# Đây là file main.py cho Bai40
def PrintList(arr):
    for i in range(len(arr)):
        if i == len(arr) - 1:
            print(arr[-1], end='.')
            break
        print(arr[i], end=', ')
    print("")
        
def main():
    colors = ['red', 'green', 'blue', 'yellow', 'white', 'black']
    PrintList(colors)
    colors.append('pink')
    PrintList(colors)
    
main()