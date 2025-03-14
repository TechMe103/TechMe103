#Exercise 1: Reverse the tuple
tuple1=(1 , 2, 3, 4, 5)
tuple1=tuple1[::-1]
print(tuple1)

#Exercise 2: Access value 20 from the tuple
tuple1=("Orange" , [10 , 20, 30] , (5 , 15, 25))
# understand indexing
# tuple1[0] = 'Orange'
# tuple1[1] = [10, 20, 30]
# list1[1][1] = 20
print(tuple1[1][1])

#Exercise 3: Create a tuple with single item 50
tuple1=(50 ,)
print(tuple1)

#Exercise 4: Unpack the tuple into 4 variables
tuple1=(10 , 20 , 30 , 40)

a, b, c,d=tuple1
print(a)
print(b)
print(c)
print(d)

#Exercise 5: Swap two tuples in Python
tuple1=(11 , 22)
tuple2=(99 , 88)
tuple1 , tuple2=tuple2 , tuple1
print(tuple2)
print(tuple1)


#Exercise 6: Copy specific elements from one tuple to a new tuple
#output: (44 , 55)
tuple1=(11 ,22, 33, 44, 55, 66)
tuple2=tuple1[3:-1]
print(tuple2)

#Exercise 7: Modify the tuple
tuple2=(11 , [22, 33] , 44, 55)
tuple2[1][0]=222
print(tuple2)

#Exercise 8: Sort a tuple of tuples by 2nd item
tuple1=(('a' , 23) , ('b' , 37) , ('c' , 11) , ('d' , 29))
tuple1=tuple(sorted(list(tuple1) , key=lambda x: x[1]))
print(tuple1)

#output: (('c' , 11) , ('a' , 23) , ('d' , 29) , ('b' , 37))

#Exercise 9: Counts the number of occurrences of item 50 from a tuple
tuple1=(10 , 20 ,30, 50, 40 , 50)
print(tuple1.count(50))

#Exercise 10: Check if all items in the tuple are the same
def check(tuple1) :
    return all(i== tuple1[0] for i in tuple1)

tuple2=(45 , 45, 45, 45)
print(check(tuple2))

