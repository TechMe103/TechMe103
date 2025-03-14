#Exercise 1: Reverse a list in Python
list=[1 , 2, 3, 4, 5]
list.reverse()
print(list)

list1=[4 ,5, 6, 7]
list1=list1[::-1]
print(list1)

#Exercise 2: Concatenate two lists index-wise
list1=["m" , "na" , "i" , "san"]
list2=["y" , "me" , "s" , "ika"]
list3=[ i + j for i , j in zip(list1 , list2)]
print(list3)

#Exercise 3: Turn every item of a list into its square
num=[1 ,2 , 3, 4, 5, 6, 7, 8]
res=[]
for i in num:
    res.append(i*i)
print(res)


#Exercise 4: Concatenate two lists in the following order
#output: hello dear , hello sir, take dear , take sir

list1=["Hello" , "take"]
list2=["Dear" , "sir"]

res=[x + y for x in list1 for y in list2 ]
print(res)


#Exercise 5: Iterate both lists simultaneously
list1=[10 , 20 , 30 , 40 , 50]
list2=[100 , 200, 300 , 400 , 500]

for x, y in zip(list1 , list2[::-1]):
    print(x, y)


#Exercise 6: Remove empty strings from the list of strings
list1=["Sanika" , "raj" , " " , "Sakshi" , "snehal" , " "]

res=list(filter(None , list1))
print(res)

#Exercise 7: Add new item to list after a specified item
list1=[10 , 20, [300 , 400, [5000, 6000] , 500] , 30, 40]

# understand indexing
# list1[0] = 10
# list1[1] = 20
# list1[2] = [300, 400, [5000, 6000], 500]
# list1[2][2] = [5000, 6000]
# list1[2][2][1] = 6000

list1[2][2].append(7000)
print(list1)

#Exercise 8: Extend nested list by adding the sublist
list1=["a" , "b", ["c", ["d" , "e" , ["f" , "g" ], "k"] , "l"] , "m", "n" ]
sub_list=["h" , "i" , "j"]

# understand indexing
# list1[2] = ['c', ['d', 'e', ['f', 'g'], 'k'], 'l']
# list1[2][1] = ['d', 'e', ['f', 'g'], 'k']
# list1[2][1][2] = ['f', 'g']

list1[2][1][2].extend(sub_list)
print(list1)


#Exercise 9: Replace list’s item with new value if found
list1=[5 , 10, 15, 20, 25, 50, 20]

index=list1.index(20)

list1[index] = 200
print(list1)

#Exercise 10: Remove all occurrences of a specific item from a list.
list1=[5 , 20, 15, 20, 25, 50, 20 ]

def remove_value(sample_list, val):
    return[i for i in sample_list if i!= val]

res=remove_value(list1 , 20)
print(res)



#using while loop sol 2
list1=[5 , 20, 15, 20, 25, 50, 20]

while 20 in list1:
    list1.remove(20)
print(list1)