def sum(a,b):
    s=a+b
    return s
print(sum(1 , 3))

def cal_sum(a, b):
    return a+b
sum=cal_sum(2 ,4)
print(sum)

def cal_avg(a, b, c):
    sum=a+b+c
    avg= sum/3
    print(avg)
    return avg
cal_avg(1 , 2, 3)

#default parameters
def null(b , a=2):
    print(a*b)
    return a*b
null(1)