#Create a dictionary with keys: 'brand', 'model', 'year'. Print each value


cars = [
    {'brand': 'Toyota', 'model': 'Corolla', 'year': 2020},
    {'brand': 'Honda', 'model': 'Civic', 'year': 2019},
    {'brand': 'Ford', 'model': 'Mustang', 'year': 2021},
    {'brand': 'Tesla', 'model': 'Model 3', 'year': 2022}
]


for car in cars:
    print(f"Brand: {car['brand']}, Model: {car['model']}, Year: {car['year']}")

# Add a new key 'color' to the dictionary and update the value of 'year'

car = {'brand': 'Toyota', 'model': 'Corolla', 'year': 2020}


car['color'] = 'Red'


car['year'] = 2022

print(car)


# Delete the key 'model' and print the updated dictionary

# Original dictionary
car = {
    'brand': 'Toyota',
    'model': 'Corolla',
    'year': 2020
}

# Deleting the 'model' key
del car['model']

# Printing the updated dictionary
print(car)


## Current dictionary
car = {
    'brand': 'Toyota',
    'year': 2020
}

# Trying to access a key that doesn't exist ('model')
model_value = car.get('model', 'Unknown')

# Printing the result
print(model_value)




