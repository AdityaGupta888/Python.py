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

#====if want more efficient or in short format====

x = input("Enter your name :")
print("Welcome to your calculator ,", x)
a = float(input("Enter the first number :"))
b = float(input("Enter the second number :"))
print("Enter the operator (+ , - , * , /) : ")
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

