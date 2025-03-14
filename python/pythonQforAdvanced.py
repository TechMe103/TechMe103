#Exercise 1: Reverse each word of a string
def reverse_words(sentence):
    #split string
    words=sentence.split(" ")

    #iterate list and reverse each word
    new_word_list= [word[::-1] for word in words]

    #joining the new list 
    res_str=" ".join(new_word_list)
    return res_str

str1="My name is sanika"
print(reverse_words(str1))


#Exercise 2: Read text file into a variable and replace all newlines with space
with open('sample.txt' , 'r') as file:
    data=file.read().replace('\n' , ' ')
    print(data)


#Exercise 3: Remove items from a list while iteratingIn this question, You need to remove items from a list while iterating but without creating a different copy of a list.

#Remove numbers greater than 50

#using while loop
num_list=[10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90 ,100]
i=0
n=len(num_list)
while i <n:
    if num_list[i] > 50:
        del num_list[i]
        n=n-1  # reduce list size
    else:
        i=i+1  # move to next item
print(num_list)

#using for loop and range()

num_list=[ 1, 2, 3, 4, 5, 6, 7, 8, 9,10]
for i in range(len(num_list) -1 , -1 , -1):
    if num_list [i] > 50:
        del num_list[i]
print(num_list)

#Exercise 4: Reverse Dictionary mapping
ascii_dict={'A' : 65 , 'B' : 66 , 'C': 67 , 'D' :68}
new_dict={value: key for key , value in ascii_dict.items()}
print(new_dict)

#Exercise 5: Display all duplicate items from a list
import collections

list1=[1, 2, 3, 3, 2, 1, 4, 5, 6]
duplicates=[]
for item, count in collections.Counter(list1).items():
    if count > 1:
        duplicates.append(item)
print(duplicates)


#Exercise 6: Filter dictionary to contain keys present in the given list
d1={'a' : 65 , 'b' : 66 , 'c': 67 , 'd': 68 , 'e': 69 }
l1=['a' , 'c' ,'e'] #filter
new_dict={key :d1[key]  for key in l1}
print(new_dict)

#Exercise 7: Print the following number pattern
rows=5
x=0
for i in range( rows , 0 , -1) : # reverse
    x+=1
    for j in range(1 , i+1):
        print(x , end=' ')
    print('\r')


#Exercise 8: Create an inner function
def manipulate(x , y):
    def inner_fun(x , y):
        return x+y
    z=inner_fun(x , y)
    return z+ 'Developers'

result = manipulate("Sanika")
print(result)


#Exercise 9: Modify the element of a nested list inside the following list
list1=[5 ,[10 , 15, [20, 25, [30, 35] , 40] , 45] , 50]
list1[1][2][2][1]= 3500
print(list1)

#Exercise 10: Access the nested key increment from the following dictionary


emp_dict={
    "Company" : {

        "Employee" : {
            "name": "Sanju",
            "payable":{
                "salary": 90000 ,
                "increment": 12
            }
        }
    }
}
print(emp_dict['Company'] ['employee'] ['payable'] ['increment'])
