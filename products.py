import csv

with open('products csv.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

        