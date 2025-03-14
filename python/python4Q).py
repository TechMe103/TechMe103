#Q) check leap year
#year=int(input("Enter a year:"))
#if (year %4)==0:
#    if(year %400)==0:
#        print(year , "Is a leap year")
#    else:
#        print(year , "is not a leap year")


#Q) nth term in a fibonacci series using recursion
 
#def fib(n):
#    if n<0:
#        print("The input is incorrect")
#    elif n==1:
#        return 0
#    elif n==2:
#        return 1
#    else:
#        return fib(n-1) + fib(n-2)
#print(fib(7))


#Q) print fibonacci series using iteration

#a=0
#b=1
#n=int(input("Enter the number of terms in the sequence:"))
#print(a , b , end=" ")
#while (n-2):
#    c=a+b
#    a , b=b ,c
#    print(c , end=" ")
#    n=n-1

#Q) implement a calculator to do basic operations

#def add(x, y):
#    print(x+y)
#def sub(x ,y):
#    print(x-y)
#print("Enter two numbers")
#n1=input()
#n2=input()
#print("Enter the operations +, - , * , /")
#op=input()
#if op=='+':
#    add(int(n1) , int(n2))
#elif op=='-':
#    sub(int(n1) , int(n2))
#else:
#    print("Invalid entry")



#Q) draw a circle of squares using turtle

import turtle
x=turtle.Turtle()

def square(angle):
    x.forward(100)
    x.right(angle)
    x.forward(100)
    x.right(angle)
    x.forward(100)
    x.right(angle)
    x.forward(100)
    x.right(angle+10)

for i in range(36):
    square(90)

