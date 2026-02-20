#Create a list of even numbers from 1 to 20 using list comprehension

even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)



#Create a dictionary of numbers and their cubes from 1 to 5


cubes = {num: num**3 for num in range(1, 6)}
print(cubes)