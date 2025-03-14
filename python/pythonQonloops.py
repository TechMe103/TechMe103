#Q1 print in triangular form numbers
print("Numbers pattern")
row=5
for i in range(1 , row+1, 1): # start:1  stop: row+1
    for j in range(1, i+1):  # run inner loop i+1 times
        print(j , end=' ')
    print(" ")

#Q) Exercise 3: Calculate the sum of all numbers from 1 to a given number
sum=0
n=int(input("Enter number:"))
for i in range(1 , n+1 , 1):
    sum+=1
print("\n")
print("sum is:" , sum)

#using built in functions
n=int(input("Enter a number:"))
x=sum(range(1 , n+1))
print("sum is:" , x)

#Q) Exercise 5: Display numbers from a list using loop
numbers=[1 , 2, 3, 4, 5, 6, 7]
for item in numbers:
    if item >10:
        break
    elif item >1:
        continue
    elif item % 5==0
    print(item)

#Q) Exercise 6: Count the total number of digits in a number
num=57478539
count=0
while num !=0:
    num=num//10
    count+=1
print("Total no of digits are:" , count)

#print triangle in reverse order
n=5
k=5
for i in range(0 ,n+1):
    for j in range(k-i ,0, -1):
        print(j,end=' ')
    print()

#Exercise 8: Print list in reverse order using a loop
list=[1 ,2 ,3, 4, 5]
new_list=reversed(list)
for item in new_list:
    print(item)

#using for loop and len() f
list=[1 , 2, 3, 4, 5]
size=len(list)-1
for i in range(size , -1 , -1) :
    print(list[i])

#Exercise 9: Display numbers from -10 to -1 using for loop
for num in range(-10 , 0, 1):
    print(num)

#Exercise 10: Use else block to display a message “Done” after successful execution of for loop
for i in range(5):
    print(i)
else:
    print("Done !")

#Exercise 11: Write a program to display all prime numbers within a range
#range
start=25
end=50
print("Prime numbers between " , start , "And" , end , "Are:")

for num in range(start , end+1):
    #all prime numbers are greater than one
    if num > 1:
        for i in range(2 , num):
            if(num % i) ==0:
                break
            else:
                print(num)


#Exercise 12: Display Fibonacci series up to 10 terms
num1, num2=0 ,1
print("Fibonacci sequence:")
#run loop 10 times
for i in range(10):
    print(num1 , end=" ") #print next number of series
    res=num1+num2  # add last two no. to get next no.
    num1=num2
    num2=res


#Exercise 13: Find the factorial of a given number
num=5
fact=1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num==0:
    print("The factorial of 0 is 1")
else:
    #run loop 5 times
    for i in range(1 , num+1)
    fact+=1
    print("The factorial of" , num , "is" , fact)


#Exercise 14: Reverse a given integer number
num=467873
reverse_number=0
print("Given number" , num)
while num > 0:
    reminder=num % 10
    reverse_number=(reverse_number * 10) + reminder
    num=num//10
    print("Reverse  number" , reverse_number)

#Exercise 15: Use a loop to display elements from a given list present at odd index positions
list=[1 , 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list[1::2]:  #start from indx 1 with step 2(means 1, 3,5 .....)
    print(i , end=" ")

#Exercise 16: Calculate the cube of all numbers from 1 to a given number
input_no=5
for i in range(1 , input_no+1):
    print("current no is:" , i , "And the cube is" , (i* i* i))


#Exercise 17: Find the sum of the series upto n terms
n=5
start=2                    #output:2+22+222+2222=24690
sum_seq=0

for i in range(0 , n):
    print(start , end="+")
    sum_seq+=start
    #calculate next term
    start=start * 10+ 2
    print("\nSum of above series is:" , sum_seq)


#print left bend triangle
rows=5
for i in range(0 , rows):
    for j in range(0 , i+1):
        print("*" , end=" ")
        print("\r")

for i in range(rows , 0 ,-1):
    for j in range(0 , i ,-1):
        print("*" , end=" ")
        print("\r")


