#  I am trying to write a code that will ask the user to enter the day and then it will print the workout for that day. I want to use if, elif and else statements to achieve this. Here is my code:

a = input("Enter the day: ").capitalize()
if a == "Tuesday" or a == "Wednesday":
    print("Today is Stamina Building day Do Sprints")

elif a == "Thursday" or a == "Friday" or a == "Saturday" or a== "Sunday":
    print("Today is Calisthenics day Do Pushups, Pullups, Dips, Squats, Lunges")

else:    print("Today is Rest Day")


#=== Explanation of that why we used elif not just if and else and how it works ===


'''💡 Why this works
if → checks first condition
elif → checked ONLY if first condition is false
else → runs ONLY if all above fail

👉 So only ONE block runs, never multiple.

⚡ Pro Insight (Important Concept)

Think like this:

Keyword	Meaning
if	Start a new independent check
elif	Continue the same decision chain
else	Final fallback of that chain'''

#===🔥 Ultra Clean Version (Recommended)===


a = input("Enter the day: ").capitalize()

if a in ["Tuesday", "Wednesday"]:
    print("Today is Stamina Building day Do Sprints")

elif a in ["Thursday", "Friday", "Saturday", "Sunday"]:
    print("Today is Calisthenics day Do Pushups, Pullups, Dips, Squats, Lunges")

else:
     print("Today is Rest Day")


#=== Explanation of that why we used .capitalize() and how it works ===

''' 🔤 What is capitalize()?

capitalize() is a string method in Python.

👉 It converts:

First letter → Capital (Uppercase)
Rest of the letters → Small (Lowercase)

🎯 Why we used it in your code

User can type anything:

Enter the day: wednesday
Enter the day: WEDNESDAY
Enter the day: WeDnEsDaY

Without capitalize() ❌
→ Your condition fails (because "wednesday" != "Wednesday")

With capitalize() ✅
→ It becomes "Wednesday" and matches perfectly'''
