class student:
    college_name="DMCE"
    def __init__(self, name , marks):
        self.name=name
        self.marks=marks
    def welcome(self):
        print("Welcome students," , self.name) 
    def get_marks(self):
        return self.marks
s1=student("Sanika" , 98)
s1.welcome()
print(s1.get_marks())

s2=student("Sakshi" , 96)
s2.welcome()
print(s2.get_marks())


#Q) get_avg
class student:
    def __init__(self , name , marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
            print("Hello" , self.name , "Your avg score is :" , sum/3)

s1=student("Sanu" , [98, 97, 96])
print(s1.get_avg())