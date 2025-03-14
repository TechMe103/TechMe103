#Exercise 1A: Create a string made of the first, middle and last character
#output: "james" -> jms
str="Sanika"
print("Original string is" , str)

res=str[0] #get first char
l=len(str)
mi=int(l/2)
res=res+ str[mi]
res=res+str[l-1]
print("New String:" , res)

#Exercise 1B: Create a string made of the middle three characters
#"jhondippeta"->dip
def get_middile_three_chars(str):
    print("Original String is" , str)
    mi=int(len(str)/2)

    res=str[mi-1 : mi+2]
    print("Middle three chars are:" , res)

get_middile_three_chars("Sanika")
get_middile_three_chars("sakshi")


#Exercise 2: Append new string in the middle of a given string
#s1=sult s2=kelly -> sukellylt
def append_middle(s1 ,s2):
    print("Original strings are" , s1 , s2)
    mi=int(len(s1)/2)

    x=s1[:mi:]
    x=x+s2
    x=x+s1[mi:]
    print("After appending new string in middle:" , x)
append_middle("Ault" , "kelly")

#Exercise 3: Create a new string made of the first, middle, and last characters of each input string
#s1=america s2=japan -> ajrpan

def mix_string(s1 , s2):
    first_char=s1[0] +s2[0]
    middle_char=s1[int(len(s1)/ 2) : int(len(s1) / 2) +1] + s2[int(len(s2) / 2) : int(len(s2) / 2) + 1]
    last_char=s1[len(s1)-1] +s2[len(s2) -1]

    res=first_char+middle_char+last_char
    print("mix string is " , res)

s1="America"
s2="Japan"
mix_string(s1 , s2)

#Exercise 4: Arrange string characters such that lowercase letters should come first
#str=pyNaTive->yaivePNT

str="PYnAtivE"
print("Original string:" , str)
lower=[]
upper=[]
for char in str:
    lower.append(char)
else:
    upper.append(char)

sorted_str=''.join(lower+upper)
print('Result:' , sorted_str)


#Exercise 5: Count all letters, digits, and special symbols from a given string
#&^%#)@)#)@
def find_digit_char_symbols(sample_str):
    char_count=0
    digit_count=0
    symbol_count=0
    for char in sample_str:
        if char.isalpha():
            char_count+=1
        elif char.isdigit():
            digit_count+=1
        else:
            symbol_count+=1
    print("char=" , char_count , "Digits=" , digit_count , "symbol=" , symbol_count)

sample_str="P@*$ER(#33fnH)"
print("Total counts of chars , digits , and symbols \n")
find_digit_char_symbols(sample_str)

#Exercise 6: Create a mixed String using the following rules
#abc xyz->azbycx
s1="abc"
s2="xyz"
s1_length=len(s1)
s2_length=len(s2)

#get len of the bigger string
length=s1_length if s1_length > s2_length else s2_length
result=""

#reverse s2
s2=s2[::-1]

#s1 ascending ans s2 descending
for i in range(length):
    if i< s1_length:
        result=result+s1[i]
    if i< s2_length:
        result=result + s2[i]

print(result)

#Exercise 7: String characters balance Test
#"Yn" "pYnative"-> True
def string_bal_test(s1 , s2):
    flag=True
    for char in s1:
        if char in s2:
            continue
        else:
            flag=False
    return flag

s1="Yn"
s2="pYnative"
flag=string_bal_test(s1 , s2)
print("s1 and s2 are balanced:" , flag)

s1="Ynf"
s2="pYnative"
flag=string_bal_test(s1 , s2)
print("s1 and s2 are balanced:" , flag)


#Exercise 8: Find all occurrences of a substring in a given string by ignoring the case

str1="Welcome to India. india is awesome , isnt it?"
sub_string="INDIA"
#convert string-> lowercase
temp_str=str1.lower()

#use count function
count= temp_str.count(sub_string.lower())
print("The india count is:" , count)


#Exercise 9: Calculate the sum and average of the digits present in a string

input="PYnaur$43785"
total=0
count=0
for char in input:
    if char.isdigit():
        total+=int(char)
        count+=1

avg=total / count
print("Sum is:" , total , "Average is" , avg)

#solution2
import re

input="FOdpf47433865"
digit_list=[int(num) for num in re.findall(r'\d' , input)]

print("Digits:" , digit_list)

total=sum(digit_list)
avg=total / len(digit_list)
print("Sum is:" , total ,"Average is" , avg)

#Exercise 10: Write a program to count occurrences of all characters within a string
#Apple-> A=1 p=2 l=1 e=1
str="Apple"
char_dict=dict()  #create empty dictionary
for char in str:
    count=str.count(char)
    char_dict[char]=count
print("Result:" , char_dict)

#Exercise 11: Reverse a given string
str2="Prbufsdnf"
print("Original string is:" , str2)

str2=str2[::-1]
print("Reversed string is:" , str2)

#Exercise 12: Find the last position of a given substring
#and the last position of a substring “Emma” in a given string.
str3="Emma is a data scientist who knows python. Emma works at google. "
print("Original string is: " , str3)

index=str3.rfind("Emma")
print("The last occurence of emma starts at index:" , index)

#Exercise 13: Split a string on hyphens

str4="Emma-is-a-data-scientist"
print("Original string is:" , str4)

sub_string=str4.split("-")

print("Displaying each substring")
for sub in sub_string:
    print(sub)


#Exercise 14: Remove empty strings from a list of strings
str_list=["Sanika" , "sakshi" , " " , "Snehal" , None , "Madhura" , ""]
res_list=[]            #->using loop and if condition
for s in str_list:
    if s:
        res_list.append(s)
print(res_list)

#using built in function
str_list=["Sanika" , "sakshi" , " " , "Snehal" , None , "Madhura" , ""]
new_str_list=list(filter(None , str_list))

print("After removing empty strings")
print(new_str_list)

#Exercise 15: Remove special symbols / punctuation from a string
#using translate() and maketrans()
import string

str5="/*jon is a @developer & musician"
print("Original string is:" , str5)

new_str=str5.translate(str.maketrans('', '' , string.punctuation))

print("New string is" , new_str)


#using regex replace pattern in a string
import re
str5="/*john is a @developer & musician"
print("Original string is" , str5)

  #replace special symbol with ''
res = re.sub(r'[^\w\s]', '', str5)

print("New string is" , res)


#Exercise 16: Removal all characters from a string except integers
str6="I am 17 years old and 10 months old"
print("Original string is" , str6)
#using list comprehension + join()+ isdigit
res="".join([item for item in str6 if item.isdigit()])
print(res)


#Exercise 17: Find words with both alphabets and numbers
#Emma13  scientist50
str7="Emma13 is a data scientist50 and ai expert"
print("Original string is:" + str7)

res=[]
temp=str7.split()

#isdigit() for no. + isalpha() for alphabets
#use any() to check each character

for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)

print("Displaying words with alphabets and numbers")
for i in res:
    print(i)


#Exercise 18: Replace each special symbol with # in the following string
import string

str8 = '/*Jon is @developer & musician!!'
print("The original string is:" , str8)

#replace punctuation with #
replace_char='#'
#string.punctuation to get the list of all special symbols

for char in string.punctuation:
    str8=str8.replace(char , replace_char)

print("The strings after replacement:" , str8)

