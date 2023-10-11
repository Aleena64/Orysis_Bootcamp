def sum(a,b):
    return a+b
def difference(a,b):
    return a-b
def product(a,b):
    return a*b
def quotient(a,b):
    return a/b
def remainder(a,b):
    return a%b
def calculate(n1,n2,choice):
    if(choice=="sum"):
        print(f"{sum(n1,n2)}")
    elif(choice=="difference"):
        print(f"{difference(n1,n2)}")
    elif(choice=="product"):
        print(f"{product(n1,n2)}")
    elif(choice=="quotient"):
        print(f"{quotient(n1,n2)}")
    elif(choice=="remainder"):
        print(f"{remainder(n1,n2)}")
n1=int(input("Enter a number:"))
n2=int(input("Enter a number:"))
choice=input("Type of operation:")
calculate(n1,n2,choice)