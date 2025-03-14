#Q) print n to 1 backwards
def show(n):
    if(n==0):
        return 
    print(n)
    show(n-1)

#Q) return n!
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n* fact(n-1)
print(fact(5))

#Q) recursive fnction to cal the sum of first natural no
def cal_sum(n):
    if(n==0):  
        return 0
    return cal_sum(n-1)+n
sum=cal_sum(5)
print(sum)


#Q) recursive function to print all ele in list

def print_list(list, idx=0):
    if idx == len(list):
        return
    print(list[idx])
    print_list(list, idx + 1)

# Example usage
my_list = [1, 2, 3, 4, 5]
print_list(my_list)
