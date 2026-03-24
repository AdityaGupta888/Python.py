#//== Just a program to Find the average cost spended by 3 friends ,know who spent the most amount and  the amount spended by each in percentage  ===//

a = int(input("Enter the Money spent by Aditya:"))
b = int(input("Enter the Money spent by Pranav:"))
c = int(input("Enter the Money spent by Dev:"))
if a > b and a > c:
    print("Aditya spent the most money ,So he is the King")
elif b > a and b > c:
   print("Pranav spent the most money , So he is the GOAT")
elif c > a and c > b:
   print("Dev spent the most money ,So he is the Boss" )
print("Total money spent by Aditya, Pranav and Dev is", a + b + c)
print("Money spent by Aditya in percentage is", (a / (a + b + c)) * 100, "%")
print("Money spent by Pranav in percentage is", (b / (a + b + c)) * 100, "%")
print("Money spent by Dev in percentage is", (c / (a + b + c)) * 100, "%")
print("Average money spent by  all = Aditya, Pranav and Dev is", (a + b + c) / 3)
