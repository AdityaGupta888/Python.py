#//===Just a code for basic calculator in python ===//

print("Welcome to your calculator")
print("Enter the first number :")
a = float(input())
print("Enter the second number :")
b = float(input())
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
