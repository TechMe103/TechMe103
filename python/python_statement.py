l=3
b=4
print("Area of triangle is:" , l* b)

#Multiline statement
add=1+2+\
    3+4+\
    7+8   #=>explict continuation
print(add)

#implicit continuation
add=(1+2+
     3+4+
     5+6+7)

print(add)

#eg
#list of string
names=["Emma" , 
       "sanika",
       "sakshi"]
print(names)

students={"Emma" : 32,
          "sanika": 48,
          "sakshi" : 45}
print(students)


#Compound statement => conditional + loop  statement
#control statement
#1) conditional statement=> if , if-else , if-elif-else , nested if-else
number = 6
if number > 5:
    print(number * number)
print("Next line of code")

password=input("Enter a password")

if password == "Sanika":
    print("correct password")
else:
    print("Incorrect password")


def user_check(choice):
    if choice ==1:
        print("Admin" )
    elif choice ==2:
        print("Editor")
    elif choice ==3:
        print("Guest") 
    else:
        print("Wrong entry")

user_check(1)
user_check(2)
user_check(3)
user_check(4)

num1= int(input("Enter first number"))
num2= int(input("Enter second no"))

if num1 > num2 :
    if num1 == num2:
        print(num1 , "and" , num2 , "are equal")
    else:
        print(num1 , "is greater than" , num2)
else:
    print(num1 , "is smaller than" , num2)


#pass statement
months=["jan" , "feb" , "march" , "april" ]
for mon in months:
    pass
print(months)

#