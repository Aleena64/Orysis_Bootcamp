#from list finding max
def highest(a):
    b=0
    for i in range(len(a)):
        if(a[i]>b):
            b=a[i]
    return b
def total(a):
    total=0
    for i in range(len(a)):
        total+=a[i]
    return total
a=[2, 3, 6, 8, 9]
maximum_d=highest(a)
total_d=total(a)
average_d=total_d/4
print(maximum_d)
print(total_d)
print(average_d)

# class object using calculator task