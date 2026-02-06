# Create a nested dictionary for 2 students and print the grade of the second student

# Creating a nested dictionary for 2 students




students = {
    "student1": {"name": "Alice", "grade": 88},
    "student2": {"name": "Bob", "grade": 92},
    "student3": {"name": "Charlie", "grade": 85},
    "student4": {"name": "Diana", "grade": 90}
}


second_student_key = list(students.keys())[1]  
second_student_grade = students[second_student_key]["grade"]

print(f"Grade of the second student ({students[second_student_key]['name']}): {second_student_grade}")




students = {
    "student1": {"name": "Alice", "grade": 88},
    "student2": {"name": "Bob", "grade": 92},
    "student3": {"name": "Charlie", "grade": 85}
}


for student_id, info in students.items():
    print(f"{student_id}: {info}")

#Use pop() to remove an element and print the remaining dictionary.


students = {
    "student1": {"name": "Alice", "grade": 88},
    "student2": {"name": "Bob", "grade": 92},
    "student3": {"name": "Charlie", "grade": 85}
}


removed_student = students.pop("student2")
print(f"Removed student: {removed_student}")


print("Remaining students:", students)

# Create a dictionary from two lists: one of keys and one of values.


keys = ["name", "age", "grade"]
values = ["Alice", 20, 88]


student_dict = dict(zip(keys, values))


print(student_dict)

