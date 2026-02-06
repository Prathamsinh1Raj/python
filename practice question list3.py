#Take 5 inputs from the user and store them in a list. Then print the reversed list

numbers = []

for i in range(5):
    value = input("Enter a value: ")
    numbers.append(value)

numbers.reverse()
print(numbers)
