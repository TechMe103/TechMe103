class employee:
    def __init__(self , role , dept ,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showdetails(self):
        print("Role=" , self.role)
        print("dept=" , self.dept)
        print("Salary=" , self.salary)

e1=employee("Company secretory CS" , "CS" , "90,000" )
e1.showdetails()

class engineer(employee):
    def __init__(self , name , age):
        self.name=name
        self.age=age
        super().__init__("Engineer" , "CSE" , "1,50,000")

eng1=engineer("Sanika salunkhe" , 30)
eng1.showdetails()