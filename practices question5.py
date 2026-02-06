# Simple login system

stored_username = "admin"
stored_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

if username == stored_username and password == stored_password:
    print("Welcome")
else:
    print("Access Denied")



    # Login system with 3 attempts and hidden password


#import getpass
'''stored_username = "admin"
stored_password = "1234"

attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ") # getpass.getpass(for hidden password)

    if username == stored_username and password == stored_password:
        print("Welcome")
        break
    else:
        attempts -= 1
        print(f"Access Denied. Attempts left: {attempts}")

if attempts == 0:
    print("Account locked. Too many failed attempts.")'''
