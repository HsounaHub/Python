#1
def countdown(num):
    x=[]
    for i in range(num,-1,-1):
        x.append(i)
    return x
print(countdown(9))

#2
def print_and_return(lis):
    print(lis[0])
    return lis[1]
print(print_and_return([1,5]))

#3
def first_plus_length(lis):
    return lis[0]+len(lis)
print(first_plus_length([10,2,3,4,5]))

#4
def values_greater_than_second(lis):
    x=[]
    if len(lis)==1 or len(lis)==2 :
        return False
    for item in lis:
        if item > lis[1]:
            x.append(item)
    print(len(x))
    return x
print(values_greater_than_second([3]))

#5
def length_and_value(size,value):
    x=[]
    for i in range(size):
        x.append(value)
    return x
print(length_and_value(6,2))