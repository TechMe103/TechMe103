#18)find the roots of a quadratic eq

import math
a=float(input("Enter coefficient of a:"))
b=float(input("Enter coefficient of b:"))
c=float(input("Enter coefficient of c:"))

if(a!=0):
    d=(b*b) -(4*a*c)
    if(d==0):
        print("The roots are real and eqaul.")
        r=-b/(2*a)
        print("the roots are" , r, "and" , r)
    elif(d >0):
        print("The roots are real and distinct")
        r1=(-b+(math.sqrt(d)))/(2*a)
        r2=(-b-(math.sqrt(d)))/(2*a)
        print("The root1 is:" , r1)
        print("The root2 is:" , r2)
    else: 
        print("The roots are imaginary")
        rp=-b/(2*a)
        ip=math.sqrt(-d)/(2*a)
        print("The root1 is:" , rp , "+i" , ip)
        print("The root2 is:" , rp , "-i" , ip)
else:
    print("Not a quadratic eq")

