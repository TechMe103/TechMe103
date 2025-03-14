#Exercise 2: Create a function with variable length of arguments
def func1(*args):
    for i in args:
        print(i)
func1(1 , 2,3)
func1(4 ,5)

#Exercise 3: Return multiple values from a function
def calculation(a , b):
    add=a+b
    sub=a-b
    return add , sub
res=calculation( 20 , 50)
print(res)

#solution2
def calculation(a ,b):
    return a+b , a-b
add , sub = calculation(40 , 20)
print(add , sub)


#Exercise 4: Create a function with a default argument

def show_employee(name , salary=90000):
    print("Name:" , name , "Salary:" , salary)

show_employee("Sanika" , 89999)
show_employee("raj")

#Exercise 5: Create an inner function to calculate the addition in the following way
def outer_fun(a , b):
    square=a**2

    def addition(a , b):
        return a+b
    add=addition(a , b)
    return add+5
res=outer_fun(5 , 10)
print(res)


#Exercise 6: Create a recursive function.recursive function to calculate the sum of numbers from 0 to 10.

def addition(num):
    if num:
        return num+addition(num-1)
    else:
        return 0
    
res=addition(10)
print(res)

#Exercise 7: Assign a different name to function and call it through the new name

def display_student(name , age):
    print(name , age)

display_student("Sanika" , 17)

show_student=display_student
show_student("Sanika" , 17)


#Exercise 8: Generate a Python list of all the even numbers between 4 to 30
print(list(range(4 , 30 , 2)))

#Exercise 9: Find the largest item from a given list
x=[1 , 3, 4, 56, 7]
print(max(x))

#
