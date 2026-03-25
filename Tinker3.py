print("Welcome to your calculator")
print("Enter the first number :")
a = int(input())
print("Enter the second number :")
b = int(input())
print("Enter the operator :")
c = input()
if c == "+":
    print("The sum of", a, "and", b, "is", a + b)
elif c == "-":
    print("The difference of", a, "and", b, "is", a - b)
elif c == "*":
    print("The product of", a, "and", b, "is", a * b)
elif c == "/":
    print("The quotient of", a, "and", b, "is", a / b)
else:
    print("Invalid operator")
