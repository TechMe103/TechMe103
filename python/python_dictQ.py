#Exercise 1: Convert two lists into a dictionary
keys=["ten" , "twenty" , "thiry"]
values=[10 , 20, 30]

res_dict=dict(zip(keys , values))
print(res_dict)

#using loop 
keys=["ten" , "twenty" , "thiry"]
values=[10 , 20, 30]

res_dict=dict()

for i in range(len(keys)):
    res_dict.update({keys[i]: values[i]})
print(res_dict)

#Exercise 2: Merge two Python dictionaries into one
dict1={'ten' : 10 , 'twenty': 20 , 'thirty': 30}
dict2={'thirty': 30 , 'fourty': 40 , 'fifty': 50}

dict3={**dict1 , **dict2}
print(dict3)

#sol2
dict1={'ten' : 10 , 'twenty': 20 , 'thirty': 30}
dict2={'thirty': 30 , 'fourty': 40 , 'fifty': 50}

dict3=dict1.copy()
dict3.update(dict2)
print(dict3)

#Exercise 3: Print the value of key ‘history’ from the below dict
sampleDict={
    "class":{
        "student":{
            "name": "sanika",
            "marks": {
                "phy": 90, 
                "history":89
            }
        }
    }
}
print(sampleDict['class'] ['student']['marks']['history'])


#Exercise 4: Initialize dictionary with default values
employees=['sanika' , 'sakshi']
defaults={"designation": 'developer' , "salary" : 90000}

res=dict.fromkeys(employees , defaults)
print(res)

#individual data
print(res["Sanika"])


#Exercise 5: Create a dictionary by extracting the keys from a given dictionary
dict={
    "name": "sanika",
    "age": 17,
    "salary": 90000,
    "city": "MUMBAI"

}
keys=["name" , "salary"]
new_dict={k : dict[k] for k in keys}
print(new_dict)


#using update method
dict1={
    "name": "sanika",
    "age": 17,
    "salary": 90000,
    "city": "MUMBAI"

}
keys=["name" , "salary"]
res=dict()
for k in keys:
    res.update({k : dict1[k]})
print(res)


#Exercise 6: Delete a list of keys from a dictionary
dict1={
    "name" : "sanika",
    "age": 23 ,
    "salary": 80000,
    "city" : "pune"
}
keys=["name" , "salary"]

for k in keys:
    dict1.pop(k)
print(dict1)

#using dict comprehension
dict1={
    "name" : "sanika",
    "age": 23 ,
    "salary": 80000,
    "city" : "pune"
}
keys=["name" , "salary"]

dict1={k: dict1[k] for k in dict1.keys() - keys}
print(dict1)

#Exercise 7: Check if a value exists in a dictionary
dict1={'a' : 100 , 'b' : 200 , 'c':300}
if 200 in dict1.values():
    print("200 present in a dict")


#Exercise 8: Rename key of a dictionary
dict1={
    "name" : "sanika",
    "age": 23 ,
    "salary": 80000,
    "city" : "pune"
}
dict1['location']=dict1.pop('city')
print(dict1)


#Exercise 9: Get the key of a minimum value from the following dictionary
dict1={
    "phy": 98,
    "chem": 76,
    "math": 97 
}
print(min(dict1 , key=dict1.get))

#Exercise 10: Change value of a key in a nested dictionary

dict1={
    "emp1" : {"name": "sanika" , "salary" : 90000},
    "emp2" : {"name" : "sakshi" , "salary" : 85000},
    "emp3" : {"name" : "madhura" , "salary": 80000}
}

dict1["emp3"]["salary"]=85000
print(dict1)

