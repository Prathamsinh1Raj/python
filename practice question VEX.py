#Write a Python RegEx pattern to validate an email like

import re
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|in|org)$'
email = input("Enter your email: ")
if re.fullmatch(pattern, email):
    print("Valid Email ✅")
else:
    print("Invalid Email ❌")



#From the text below, extract all Indian mobile numbers:


pattern = r'\b[6-9]\d{9}\b'
import re

text = input("Enter the text: ")

pattern = r'\b[6-9]\d{9}\b'

numbers = re.findall(pattern, text)

if numbers:
    print("Valid Mobile Numbers Found:")
    for num in numbers:
        print(num)
else:
    print("No valid mobile numbers found.")



#Check if String Contains Only Alphabets


pattern = r'^[A-Za-z]+$'
import re
text = input("Enter a string: ")
pattern = r'^[A-Za-z]+$'
if re.fullmatch(pattern, text):
    print(True)
else:
    print(False)



#Validate Password Strength

pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
import re

password = input("Enter your password: ")

pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

if re.fullmatch(pattern, password):
    print("Strong Password ✅")
else:
    print("Weak Password ❌")



#Takes user input

import re

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|in|org)$'
phone_pattern = r'^[6-9]\d{9}$'
url_pattern = r'^(https?:\/\/)?(www\.)?[a-zA-Z0-9-]+\.(com|in|org)(\/\S*)?$'
date_pattern = r'^(0[1-9]|[12][0-9]|3[01])[\/-](0[1-9]|1[0-2])[\/-]\d{4}$'

text = input("Enter input: ")

if re.fullmatch(email_pattern, text):
    print("It is an Email ✅")

elif re.fullmatch(phone_pattern, text):
    print("It is a Phone Number ✅")

elif re.fullmatch(url_pattern, text):
    print("It is a URL ✅")

elif re.fullmatch(date_pattern, text):
    print("It is a Date ✅")

else:
    print("Invalid Format ❌")





