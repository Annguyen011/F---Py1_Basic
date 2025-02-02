# Đây là file main.py cho Bai43

class Student:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.marks = 0
    
    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Marks: ", self.marks)
    

def main():
    student1 = Student()
    student1.name = "John"
    student1.age = 23
    student1.marks = 90
    student1.display()

    student2 = Student()
    student2.name = "Sam"
    student2.age = 21
    student2.marks = 80
    student2.display()
    
main()