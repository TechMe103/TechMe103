f = open(r"C:\Users\LENOVO\OneDrive\Desktop\coding\python\sample.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()


f=open(r"C:\Users\LENOVO\OneDrive\Desktop\coding\python\demo.txt", "r")
data=f.read(5)
line=f.readline()
print((line))
f.close()

#Writing to a file
f=open(r"C:\Users\LENOVO\OneDrive\Desktop\coding\python\demo.txt", "w")
f.write("abc")
print(f.read())
f.close()

#with syntax
with open(r"C:\Users\LENOVO\OneDrive\Desktop\coding\python\demo.txt" , "a") as f:
    data=f.read()
    print(data)
    print(f.write("hello"))