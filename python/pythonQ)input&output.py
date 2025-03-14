#Q1 accept no from user
num1=int(input("Enter a first no:"))

num2=int(input("Enter a second no:"))
                                           
res=num1 * num2
print("multiplicaton is " , res )

#Q2 Display three string “Name”, “Is”, “James” as “Name**Is**James”\
print('my' , 'name' , 'is' , 'sanika' , sep='**')

#Q3 Exercise 3: Convert Decimal number to octal using print() output formatting
num=8
print('&o' % num)

#Exercise 4: Display float number with 2 decimal places using print()
num=547.54895
print('%.2f' % num)

#Exercise 5: Accept a list of 5 float numbers as an input from the user
numbers=[]

for i in range(0 , 5):
    print("Enter number at location" , i , ":")
    item=float(input())
    numbers.append(item)
print("User List:" , numbers)


#Exercise 6: Write all content of a given file into a new file by skipping line number 5

with open(r"C:\Users\LENOVO\OneDrive\Desktop\coding\python\test.txt" , "r") as f:
    lines=f.readlines()

with open(r" C:\Users\LENOVO\OneDrive\Desktop\coding\python\sample.txt" , "w") as f:
    count=0
    for line in lines:
        #skip 5th lines
        if count==4:
            count+=1
            continue
        else:
            f.write(line)
            count+=1


#Exercise 7: Accept any three string from one input() call
str1 , str2 , str3 =input("enter three strings").split()
print("name1:" , str1)
print("name2:" , str2)
print("name3:" , str3 )

#Exercise 8: Format variables using a string.format() method.
quantity=3
totalmoney=1000
price=450
statement1="I have {1} dollars so i can buy {0} football for {2:.2f} dollars"
print(statement1.format(quantity , totalmoney , price))

#Exercise 9: Check file is empty or not
import os
size=os.stat(r"C:\Users\LENOVO\OneDrive\Desktop\coding\python\test.txt").st_size
if size==0:
    print("File is empty")


#Exercise 10: Read line number 4 from the following file
with open(r"C:\Users\LENOVO\OneDrive\Desktop\coding\python\new_file.txt", "r") as f:
    lines=f.readlines()
    print(lines[2])