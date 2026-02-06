x = 5
name = 'Alice'
price = 125.25
print(name)
print(price)

age = 25
height = 5.9
is_student = True
hobbies = ['reading', 'gaming']
print(type(age))
print(type(height))
print(type(is_student))
print(type(hobbies))

print(age)

print(height)

print(is_student)

print(hobbies)

name = input('Enter Your Name: ')
print('Hello,', name)

age = input('Enter your age: ')
age = int(age)
print('Next year you will be', age + 1)


a = True
b = False
print(a and b)  
print(a or b)   
print(not a)

text = 'Hello World'
print(text[0])     
print(text[-1])    
print(text[0:5])   
print(text[6:])    
print(text[:5]) 

fruits = ['apple', 'banana', 'cherry']
print('banana' in fruits)      
print('grape' not in fruits)   

x = [1,2,3]
y = x
z = [1,2,3]
print(x is y)     
print(x is z)      
print(x is not z)

a = 10
b = 3
print('Add:', a + b)
print('Subtract:', a - b)
print('Multiply:', a * b)
print('Divide:', a / b)
print('Modulus:', a % b)
print('Floor Division:', a // b)
print('Exponent:', a ** b)


x = 10
if x > 0:
    print('Positive')
elif x == 0:
    print('Zero')
else:
    print('Negative')

   


age = 25
has_id = True
if age >= 18 and has_id:
    print('Entry allowed')
else:
    print('Entry denied')

a = 10
b = 3
print('Add:', a + b)
print('Subtract:', a - b)
print('Multiply:', a * b)
print('Divide:', a / b)
print('Modulus:', a % b)
print('Floor Division:', a // b)
print('Exponent:', a ** b)

x = 5
y = 10
print(x == y)  # False
print(x != y)  # True
print(x > y)   # False
print(x < y)   # True
print(x >= y)  # False
print(x <= y)  # True

num = 10
num += 5  # num = num + 5
print(num)  # 15
num *= 2   # num = num * 2
print(num)  # 30

msg = 'hello world'
print(msg.upper())        
print(msg.lower())        
print(msg.replace('world', 'Python'))  
print(msg.find('o'))      
words = msg.split()       
print(words)              
joined = '-'.join(words)
print(joined)      

print('Hello\nWorld')   
print('It\'s a sunny day')  
print("He said \"Hi!\"")

x, y = input("Enter two numbers separated by a space: ").split()
print(f"You entered: {x} and {y}")


num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
sum = num1 + num2
print('Sum:', sum)

length = float(input('Enter length: '))
breadth = float(input('Enter breadth: '))
area = length * breadth
print('Area of rectangle:', area)

from datetime import datetime
birthdate_str = input("Enter your birthdate (DD-MM-YYYY): ")
birthdate = datetime.strptime(birthdate_str, "%d-%m-%Y")
today = datetime.today()
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
print("Your age is:", age)

def filter_even_numbers(numbers):
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    return even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_even_numbers(numbers)
print("Even Numbers:", even_numbers)

name = input("Enter your name: ")
age = input("Enter your age: ")
with open("user_info.csv", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")

count = 1
while count <= 5:
    print('Count:', count)
    count += 1

for i in range(5):
    print(i)   

for i in range(1, 6):
    print(i)   

for i in range(0, 10, 2):
    print(i)

for i in range(1, 4):
    for j in range(1, 4):
        print(f'{i},{j}', end=' ')
    print()


for i in range(1, 6):
    if i == 3:
        continue
    print(i) 

