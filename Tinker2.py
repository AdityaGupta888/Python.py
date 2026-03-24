a = int(input("Enter the Money spent by Aditya:"))
b = int(input("Enter the Money spent by Pranav:"))
c = int(input("Enter the Money spent by Dev:"))
if a > b and a > c:
    print("Aditya spent the most money")
elif b > a and b > c:
    print("Pranav spent the most money")
elif c > a and c > b:
    print("Dev spent the most money")
    print("Total money spent by Aditya, Pranav and Dev is", a + b + c)
    print("Average money spent by  all = Aditya, Pranav and Dev is", (a + b + c) / 3)
