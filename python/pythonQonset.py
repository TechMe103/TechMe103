#Exercise 1: Add a list of elements to a set
set1={"yellow" , "Orange" , "pink"}
set2={"Blue" , "green" , "red"}

set1.update(set2)
print(set1)

#Exercise 2: Return a new set of identical items from two sets
set1={1 , 3, 2, 4, 5, 6}
set2={3,4, 5, 6, 7, 9,8}
print(set1.intersection(set2))

#Exercise 3: Get Only unique items from two sets

set1={1, 2, 3, 4, 5, 6}
set2={4 ,5, 6, 7, 8,9}

print(set1.union(set2))

#Exercise 4: Update the first set with items that don’t exist in the second set
set1={10 , 20, 30}
set2={20 , 40 , 50}

set1.difference_update(set2)
print(set1)


#Exercise 5: Remove items from the set at once
set1={ 1 , 2, 3,4 , 5, 6}
set1.difference_update({1, 2, 3})
print(set1)


#Exercise 6: Return a set of elements present in Set A or B, but not both
set1={1 , 2, 3, 4, 5, 6}
set2={3 , 4, 5, 6, 7}
print(set1.symmetric_difference(set2))

#Exercise 7: Check if two sets have any elements in common. If yes, display the common elements
set1={ 1, 2, 3, 4, 5,6}
set2={6 ,7, 8, 9, 10}

if set1.isdisjoint(set2):
    print("Two sets have no items in common")
else:
    print("Two sets have items in common")

    print(set1.intersection(set2))


#Exercise 8: Update set1 by adding items from set2, except common items
set1={1 , 2,3, 4, 5, 6}
set2={3 ,4, 5, 6,7,8}

set1.symmetric_difference_update(set2)
print(set1)

#Exercise 9: Remove items from set1 that are not common to both set1 and set2
set1={1 , 2, 3, 4, 5}
set2={3, 4, 5, 6, 7, 8}

set1.intersection_update(set2)
print(set1)


#