#Create a list of 5 numbers and print the largest number


# numbers = [3, 7, 2, 9, 5]
# print(max(numbers))


#Write a program to remove duplicates from a list.

# numbers = [1, 2, 3, 2, 4, 1, 5]

# unique_numbers = list(set(numbers))

# print(unique_numbers)


#Reverse a list without using .reverse()

# numbers = [1, 2, 3, 4, 5]
# reversed_list = numbers[::-1]
# print(reversed_list)

#Find the sum of all elements in a list.

# numbers = [1, 2, 3, 4, 5]
# total = sum(numbers)
# print(total)



# Create a tuple of 5 elements
# my_tuple = (10, 20, 30, 40, 50)
# print(my_tuple[2])  # 30
# my_list = list(my_tuple)
# print(my_list)
# print(30 in my_tuple)  # True
# print(my_tuple.count(30))  # 1



# Create two sets
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# union_set = set1.union(set2)
# print("Union:", union_set)  
# intersection_set = set1.intersection(set2)
# print("Intersection:", intersection_set)  
# set1.discard(2)  
# print("Set1 after removing 2:", set1) 
# my_list = [1, 2, 2, 3, 3, 3]
# unique_set = set(my_list)
# print("Unique elements:", unique_set)  


# Create a dictionary with student names and marks
# students = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78
# }
# students["David"] = 88
# print("Updated dictionary:", students)
# print("Students and marks:")
# for name, marks in students.items():
#     print(name, ":", marks)
# top_student = max(students, key=students.get)
# print("Top student:", top_student, "with marks", students[top_student])


# Function to check if a number is even or odd
# def is_even_or_odd(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# def factorial(n):
#     if n < 0:
#         return "Factorial is not defined for negative numbers"
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
# def max_of_two(a, b):
#     if a > b:
#         return a
#     else:
#         return b
# def sum_of_list(lst):
#     total = 0
#     for num in lst:
#         total += num
#     return total
# print(is_even_or_odd(7))        
# print(factorial(5))             
# print(max_of_two(10, 20))       
# print(sum_of_list([1, 2, 3, 4])) 
 



# Lambda function to add two numbers
# add = lambda x, y: x + y
# is_positive = lambda x: x > 0
# square = lambda x: x ** 2
# max_of_two = lambda a, b: a if a > b else b
# print(add(5, 3))          
# print(is_positive(-4))  
# print(square(6))         
# print(max_of_two(10, 20)) 


# Square all numbers in a list
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(lambda x: x ** 2, numbers))
# print(squared_numbers)  
# words = ["apple", "banana", "cherry"]
# uppercase_words = list(map(lambda s: s.upper(), words))
# print(uppercase_words)  
# nums = [5, 10, 15, 20]
# added_ten = list(map(lambda x: x + 10, nums))
# print(added_ten) 
# celsius = [0, 20, 37, 100]
# fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
# print(fahrenheit) 



#Get only even numbers from a list
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)  
# nums = [10, 55, 23, 75, 60, 42]
# greater_than_50 = list(filter(lambda x: x > 50, nums))
# print(greater_than_50)  
# words = ["apple", "banana", "orange", "grape", "umbrella"]
# vowel_words = list(filter(lambda w: w[0].lower() in 'aeiou', words))
# print(vowel_words)  
# mixed_numbers = [-10, 5, -3, 8, 0, -2, 7]
# positive_numbers = list(filter(lambda x: x > 0, mixed_numbers))
# print(positive_numbers)  



#Find the sum of all elements in a list
# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# sum_numbers = reduce(lambda x, y: x + y, numbers)
# print(sum_numbers)  
# product_numbers = reduce(lambda x, y: x * y, numbers)
# print(product_numbers)  
# max_number = reduce(lambda x, y: x if x > y else y, numbers)
# print(max_number)  
# words = ["Hello", "world", "from", "Python"]
# concatenated = reduce(lambda x, y: x + " " + y, words)
# print(concatenated)  
