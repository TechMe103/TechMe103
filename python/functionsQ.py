#Q) print length of a list
cities=["Vangani" , "badlapur", "kharghar", "Airoli", "Ambernath"]

def length(list):
    print(len(list))
length(cities)  # call

#Q) print ele of list in single line
cities=["Vangani" , "badlapur", "kharghar", "Airoli", "Ambernath"]

print(cities[0] , end=" ")
print(cities[1] , end=" ")
def print_len(list):
    print(len(list))
print_len(cities)

#diff pattern
cities=["Vangani" , "badlapur", "kharghar", "Airoli", "Ambernath"]

def print_list(list):
    for item in list:
        print(item , end=" ")
print_list(cities)

#Q)  find factorial of n

def cal_fact(n):
    fact=1
    for i in range(1 , n+1):
        fact*=i
        print(fact)
cal_fact(5)

#Q) convert usd-> inr

def converter(usd_val):
    inr_val=usd_val* 83
    print(usd_val , "USD=" , inr_val , "Inr")
converter(100)