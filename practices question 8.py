# Input marks for 5 subjects
m1 = float(input("Enter marks for subject 1: "))
m2 = float(input("Enter marks for subject 2: "))
m3 = float(input("Enter marks for subject 3: "))
m4 = float(input("Enter marks for subject 4: "))
m5 = float(input("Enter marks for subject 5: "))

# Calculate total and percentage
total = m1 + m2 + m3 + m4 + m5
percentage = (total / 250) * 100   # assuming each subject is out of 50

# Print results
print("Total Marks:", total)
print("Percentage:", percentage, "%")
