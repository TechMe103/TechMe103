#Q) factorial using recursion
#def fact(n):
#    if n==1:
#        f=1
#    else:
#        f=n* fact(n-1)
#    return f
#num= int(input("Enter an integer:"))
#result=fact(num)
#print("The factorial of" , num , "is:" , result)

#Q) sum of no using list
#numbers=[]
#num=int(input('how many numbers:'))
#for n in range(num):
#    x=int(input('enter number:'))
#    numbers.append(x)
#    print("sum of numbers in the given list is:" , sum(numbers))


#Q) implement linear search

#numbers=[2 , 4, 5,6 ,3 , 9 , 7 , 8 ,10]
#f=0 #flag
#x=int(input("Enter the numbers to be found out:"))
#for i in range (len(numbers)):
#    if(x==numbers[i]):
#        print("Successful search , the element is found at position" , i)
#        f=1
#        break
#if(f==0):
#    print("oops ! search unsuccessful")

#Q)  implement binary search
#def binarySearch(numbers, low, high, x):
#    if (high >= low):
#        mid = low + (high - low)//2
#        if (numbers[mid] == x):
#            return mid
#        elif (numbers[mid] > x):
#            return binarySearch(numbers, low, mid-1, x)
#        else:
#            return binarySearch(numbers, mid+1, high, x)
#    else:
#        return -1
#numbers = [ 1,4,6,7,12,17,25 ]   #binary search requires sorted numbers
#x = 7
#result = binarySearch(numbers, 0, len(numbers)-1, x)
#if (result != -1):
#    print("Search successful, element found at position ", result)
#else:
#    print("The given element is not present in the array")


#Q)  find odd numbers in an array
#numbers=[1 , 2, 3 ,4 , 5 ,6 ]
#count=0
#for i in range(len(numbers)):
#    if(numbers[i]%2 !=0) :
#        count=count+1
#        print("The numbers of odd numbers in the list are: " , count)

#Q)  largest no. in a list without using built in functions

#numbers=[1 , 2, 4 ,5, 6, 7 ,8]
#big=numbers[0]
#position=0
#for i in range(len(numbers)):
#    if(numbers[i] > big):
#        big=numbers[i]
#        position=i
#print("the largest element is" , big , "which is found at position " , position)


#Q) insert a number to any position in a list
#numbers=[1 , 2 ,4, 5, 6 ,7 ,8]
#print(numbers)
#x=int(input("Enter the numbers to be inserted:"))
#y=int(input("Enter the position:"))
#numbers.insert(y, x)
#print(numbers)


#Q) delete an ele from a list by index
#numbers=[1 , 2, 3, 4 ,5 ,6 ,7, 8]
#print(numbers)
#x=int(input("Enter the position of the element to be deleted:"))
#numbers.pop(x)
#print(numbers)

#Q) string is palindrome or not

#def rev(inputstring):
#    return inputstring[::-1]
#def isPalindrome(inputstring):
#    reverseString=rev(inputstring)
#    if(inputstring==reverseString):
#        return True
#    return False
#s=input("Enter a string:")
#result=isPalindrome(s)
#if result==1:
#    print("The string is palindrome")
#else:
#    print("The string is not palindrome")


#Q) implement a matrix addition

#x=[[1 , 2, 3],
#   [4, 5, 6],
#   [7 ,8, 9]]

#y=[[9 , 8 , 7],
#   [6 , 5, 4],
#   [3 , 2 ,1]]

#result=[[0 , 0, 0],
#        [0 , 0, 0],
#        [0 , 0, 0]]

#for i in range(len(x)):
#    for j in range(len(x[0])):
#        result[i][j]=x[i][j]+y[i][j]
#for k in result:
#    print(k)

#Q) matrix multiplication
x=[[1 , 2, 3],
    [4, 5, 6],
    [7 ,8, 9]]

y=[[9 , 8 , 7],
    [6 , 5, 4],
    [3 , 2 ,1]]

result=[[0 , 0, 0],
        [0 , 0, 0],
        [0 , 0, 0]]

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j]+=x[i][j] * y[k][j]
for x in result:
    print(x)     
           
    
        