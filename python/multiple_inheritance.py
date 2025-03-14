class A:
    varA="Welcome to class A"

class B:
    varB="Welcome to class B"

class C(A, B):
    varC="welcome to class C"

c1=C()
print(c1.varC)
print(c1.varB)
print(c1.varA)

