age=21
if(age>= 18):
    print("can vote and drive")
elif(age<=18):
    print("they are not eligible to vote")



light="Green"
if(light=="red"):
    print("stop")
elif(light=="Green"):
    print("go")
elif(light=="yellow"):
    print("Wait")
else:
    print("light is broken")



#Q3
marks=93
if(marks>=90):
    grade="A"
elif(marks>= 80 and  marks< 90):
    grade="B"
elif(marks>=70  and  marks<80):
    grade="c"
else:
    grade="D"
print("grade of student->" , grade)


#nesting statement
age=24
if(age>=18):
    if(age>=80):
    print("cannot vote")
    else:
    print("can vote")
    else:
    print("cannot vote")