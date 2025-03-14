#Q) check given number is even or not

#num=int(input("Enter a number:"))
#x=int(num)%2
#if x==0:
#   print("The number is even")
#else:
#   print("The number is odd")



#Q) covert temperature in degree to fahrenheit

#c=input("Enter temperature in centigrade:")
#f=(9*(int (c))/5) + 32
#print("Trmperature in fahrenheit is:" , f)

#Q) find area of triangle whose sides given

#import math
#a=float(input("Enter length of side a:"))
#b=float(input("Enter length of side b:"))
#c=float(input("Enter length of c:"))

#s=(a+b+c)/2
#area=math.sqrt(s*(s-a)*(s-b)*(s-c))
#print("Area of the triangle is:" , area)

#Q) avg of a set of integers
#count=int(input("Enter the count of no.:"))
#i=0
#sum=0
#for i in range(count):
#    x=int(input("Enter an integers:"))
#    sum=sum+x

#avg=sum/ count
#print("the avg is:" , avg)

#Q) product of a set of real numbers
#i=0
#product=1
#count=int(input("Enter the number of real no:"))
#for i in range(count):
#    x=float(input("enter a real no:"))
#    product=product*x
#    print("The product of the numbers is:" , product)


#Q) find the circumference and ares of circle with radius

#import math
#r=float(input("Enter radius od circle:"))
#c=2* math.pi*r    #2pir
#area=math.pi*r*r   #pir^2
#print("The circumference of circle is:" , c)
#print("The ara of circle is:" , area) 

#Q) check given int is a multiple of 5

#num=int(input("Enter an integer:"))
#if(num % 5 ==0):
#    print("it is multiple of 5" , num)
#else:
#    print("it is not multiple of 5")

#Q) multiple of 5 & 7
#num=int(input("enter an integer:"))
#if((num%5==0) and (num % 7==0)):
#    print(num , "is a multiple of both 5 & 7")
#else:
#    print(num , "is not multiple of both..")

#Q) find avg of 10 numbers using while looop

#count=0
#sum=0
#while (count< 10):
#    num=float(input("enter a real number:"))
#    count+=1
#    sum=sum+num
#    avg=sum/10
#    print("Avg is:" , avg)

#Q) display the integers in a reverse manner
#num=int(input("Enter a positive integer:"))
#rev=0
#while (num !=0):
#    digit=num%10
#    rev=(rev*10) + digit
#    num=num/10
#print(rev)

#Q) find geometric mean of n numbers
#c=0
#p=1.0
#count=int(input("Enter the number of values:"))
#while (c < count):
#    x=float(input("Enter a real number:"))
#    c+=1
#    p=p*x
#gm=pow(p , 1.0/count)
#print("The geometric mean is:" , gm)


#Q) sum of digits of an integers using a while loop

#sum=0
#num=int(input("Enter an integers:"))
#while ( num != 0):
#    digit=num % 10
#    sum=sum+digit
#    num=num//10
#    print("Sum of digits is:" , sum)

#Q) display all multiple of 3 within range 10 to 50

#for i in range(10 , 50):
#    if(i % 3==0):
#        print(i)

#q) display all int within the range 100 to 200 whose sum of digits is even number

#for i in range(100 , 200):
#    num=i
#   sum=0
#  while (num !=0):
#        digit=num % 10
#        sum=sum+ digit
#       num=num // 10
#   if(sum %2 ==0):
#       print(i)

#q) check prime or not
#num=int(input("enter an integer greater than 1:"))
#isprime=1
#for i in range(2 , num//2):
#    if(num%i==0):
#        isprime=0
#        break
#    if(isprime==1):
#        print(num  , "is a prime  number")
#    else:
#        print(num , "is not a prime number")

#q) generate the prime no from 1 to n

#num=int(input("Enter the range:"))
#for n in range(2 , num):
#    for i in range(2 , n):
#        if(n%i==0):
#            break
#    else:
#        print(n)

#Q) print numbers from a given numbers n till 0 using recursion

def print_till_zero(n):
    if(n==0):
        return
    print(n)
    n=n-1
    print_till_zero(n)
print_till_zero(8)