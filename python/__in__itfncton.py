class Student:
    def __init__(self, fullname):
        self.name = fullname
        print(self)
        print("Adding new student in database")

# Example usage:
s1 = Student("Sanika")
print(s1.name)



#Q)
class student:
    def __init__(self , fullname):
        self.name=fullname
        print("Adding new student in database")

s1=student("Sanu")
print(s1.name)

#Q)
class student:
    def __init__(self , name , marks):
        self.name=name
        self.marks=marks
        print("Adding new student in database")

s1=student("Sanika" , 98)
print(s1.name , s1.marks)

s2=student("Sakshi" , 96)
print(s2.name , s2.marks)