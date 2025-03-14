#Q) create file 
with open(r"C:\Users\LENOVO\OneDrive\Desktop\coding\python\sample.txt", "w" )  as f:
    f.write("Hi everyone\n we are learning file\n using java\t i like programming\n")


#Q) waf that replaces all occurences of java with python in file

with open(r"C:\Users\LENOVO\OneDrive\Desktop\coding\python\sample.txt" , "r") as f:
    data=f.read()
    new_data=data.replace("i" , "e")
    print(new_data)


with open(r"C:\Users\LENOVO\OneDrive\Desktop\coding\python\sample.txt" , "w") as f:
    f.write(new_data)

#Q) search java exists or not
with open(r"C:\Users\LENOVO\OneDrive\Desktop\coding\python\sample.txt" , "r") as f:
    data=f.read()
    if(data.find("java") != -1):
        print("Found")
    else:
        print("Not found")

#Q) which line of the file does "java" occur first
def first_for_line():
    word="java"
    data=True
    line_no=1

    with open(r"C:\Users\LENOVO\OneDrive\Desktop\coding\python\sample.txt" , "r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                line_no+=1
                return -1
            print(first_for_line())

            