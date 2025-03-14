#Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second
list1=[3 , 6, 9, 12, 15, 18, 21]
list2=[4, 8, 12, 16, 20, 24, 28]
res= list()

odd_ele=list1[1 ::2]
print("Element at odd index position from list one")
print(odd_ele)

even_ele=list2[0::2]
print("Elements at even index position from list two")
print(even_ele)

print("Printing final third list ")
res.extend(odd_ele)
res.extend(even_ele)
print(res)


#Exercise 2: Remove and add item in a list
#Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.

list=[34, 54, 67, 89, 11, 43, 94]

print("original list" , list)
element=list.pop(4)
print("List after removing element at index 4" , list)

list.insert(2 , element)
print("List after adding element at index 2" , list)

list.append(element)
print("List after adding element at last" , list)

#Exercise 3: Slice list into 3 equal chunks and reverse each chunk
sample_list=[11 , 45 ,8, 23, 14, 12, 78, 45, 89]
print("Original list" , sample_list)

length= len(sample_list)
chunk_size=int(length/3)
start=0
end=chunk_size
#run loop 3 times

for i in range(3):
    indexes=slice(start , end)

    #get chunk
    list_chunk=sample_list[indexes]
    print("Chunk" , i , list_chunk)

    #reverse chunk
    print("After reversing it" , list(reversed(list_chunk)))

    start=end
    end+=chunk_size


#Exercise 4: Count the occurrence of each element from a list

list1=[1 , 2 ,3, 4, 3, 3, 1, 2 , 4 , 4, 5, 5]
print("Original list" , list1)

count_dict=dict()
for item in list1:
    if item in count_dict:
        count_dict[item] +=1
    else:
        count_dict[item]=1

print ("Printing count of each item" , count_dict)


#Exercise 5: Create a Python set such that it shows the element from both lists in a pair
first_list=[2 , 3, 4, 5, 6, 7, 8]
print("first List" , first_list)

second_list=[4 ,9, 16, 25, 36, 49, 64]
print("Second list" , second_list)

result=zip(first_list , second_list)
result_set=set(result)
print(result_set)

#Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set
first_set={23 , 42,65, 57, 78, 98, 56}
second_set={57, 83, 23 , 78 ,44, 66, 77}

print("first set:" , first_set)
print("second set:" , second_set)

intersection=first_set.intersection(second_set)
print("Intersection is" , intersection)

for item in intersection:
    first_set.remove(item)

print("First set after removing common element" , first_set)


#Exercise 7: Checks if one set is a subset or superset of another set. If found, delete all elements from that set
first_set={57 , 83, 29}
second_set={57, 83, 29, 67, 73, 43, 48}

print("First set:" , first_set)
print("Second set:" , second_set)

print("First set is subset of second set-" ,first_set.issubset(second_set))
print("second set is subset of first set-" , second_set.issubset(first_set))

print("first set is super set of second set-" , first_set.issuperset(second_set))
print("second set is super set of first set-" , second_set.issuperset(first_set))

if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()

print("first set:" , first_set)
print("second set:" , second_set)

#Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
roll_no=[1 , 2, 3, 4, 5, 6, 7, 8]
sample_dict={'jhon': 4 , 'emma': 6 , 'sanika': 1 , 'Raj': 2 , 'sakshi':3} 

print("List:" , roll_no)
print("dictionary:" , sample_dict)

roll_no[:]= [item for item in roll_no if item in sample_dict.values()]
print("After Removing unwanted elements from lists:" , roll_no)



#Exercise 9: Get all values from the dictionary and add them to a list but don’t add duplicates
speed= {'jan': 47 , 'feb': 52 , 'march' : 47 , 'april': 44 , 'may': 52 , 'june':53 , 'july': 54 ,'aug' :44 , 'sept': 54}

print("Dictionary is values-" , speed.values())

speed_list=list()

for val in speed.values():
    if val not in speed_list:
        speed_list.append(val)
print("Unique list" , speed_list)


# Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number
list2=[87 ,52, 44, 53, 87, 52, 53]

print("Original list" , list2)

list2=list(set(list2))
print("Unique list" , list2)

t=tuple(list2)
print("tuple" , t)

print("Minimum number is:" , min(t))
print("Maximum number is:" , max(t))

