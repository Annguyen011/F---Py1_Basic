# Đây là file main.py cho Bai41
colors = ['red', 'green', 'blue', 'yellow', 'white', 'black']  # Initialize a list of colors
str = input()  # Take input from the user
print(colors)  # Print the initial list of colors

try:
    colors.remove(str)  # Try to remove the color entered by the user from the list
    print(colors)  # Print the list after removal
except ValueError:
    print("Error: color not in list")  # Print an error message if the color is not in the list

colors.pop()  # Remove the last color from the list
colors.pop(2)  # Remove the color at index 2 from the list

colors.insert(2, 'purple')  # Insert 'purple' at index 2

try:
    colors.index("yellow")  # Try to find the index of 'yellow' in the list
except ValueError:
    print("Error: color not in list")  # Print an error message if 'yellow' is not in the list

print(colors.count("red"))  # Print the count of 'red' in the list
colors.replace("red", "orange")  # Replace 'red' with 'orange' in the list