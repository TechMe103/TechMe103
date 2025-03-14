#num from 1 to 100
for i in range(1 , 101):
    print(i)

# from 100 to 1
for i in range(100 , 0 , -1):
    print(i)

#multiplication for n
n=int(input("Enter number:"))
for i in range(1 , 11):
    print(n * i)


#sum of first n numbers
n=5
sum=0
for i in range(1 , n+1):
    sum+=i
    print("Sum:" , sum)