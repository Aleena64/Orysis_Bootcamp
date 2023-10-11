class calculator:
    def sum(self, x, y):
        return x + y
    def difference(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def divide(self, x, y):
        return x / y
cal = calculator()
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
addition = cal.sum(a, b)
print(f"{a} + {b} = {addition}")
subtraction = cal.difference(a, b)
print(f"{a} - {b} = {subtraction}")
multiplication = cal.multiply(a, b)
print(f"{a} * {b} = {multiplication}")
division = cal.divide(a, b)
print(f"{a} / {b} = {division}")