# Program to classify age group

age = int(input("Enter your age: "))

if age < 18:
    print("Minor")
elif 18 <= age <= 59:
    print("Adult")
else:
    print("Senior Citizen")