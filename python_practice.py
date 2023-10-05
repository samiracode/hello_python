class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f'Hi {self.name}! You are {self.age} years old')

student1 = Student('Johnny', 11)
student2 = Student('Sally', 8)
print(student1.name)
print(student2.name)

print(Student.intro(student1))
print(Student.intro(student2))




