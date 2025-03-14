#for loop
list=[1 , 2, 3]
for ele in list:
    print(ele)


#for loop with else
for ele in list:
    print(ele)
else:
    print("End")


nums=[4 , 5, 6, 7]
for val in nums:
    print(val)


str="SanuSalunkhe"
for char in str:
    print(char)

num=(3, 6, 9 , 12)
x=12
idx=0
for ele in num:
    if(ele==x):
        print("No is found" , idx)
        break
    idx+=1
    