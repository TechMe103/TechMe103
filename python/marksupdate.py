marks={}
x=input("Enter marks of phy:")
marks.update({"phy": x})
y=input("Enter marks of chem:")
marks.update({"phy": y})
z=input("Enter marks of math:")
marks.update({"phy": z})

print(marks)


#Q) store 9 and 9.0 as separate values in set
val={9, "9.0"}
print(val)

val={
    ("float" , 9.0),
    ("int" , 9)
}
print(val)
