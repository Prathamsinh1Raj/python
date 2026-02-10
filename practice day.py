#Create a program that reads a file and counts how many lines, words, and characters it contains

# def count_file_contents(filename):
#     line_count = 0
#     word_count = 0
#     char_count = 0

#     try:
#         with open(filename, "r") as file:
#             for line in file:
#                 line_count += 1
#                 word_count += len(line.split())
#                 char_count += len(line)

#         print("Lines:", line_count)
#         print("Words:", word_count)
#         print("Characters:", char_count)
#     except FileNotFoundError:
#         print("File not found.")
# filename = input("Enter file name: ")
# count_file_contents(filename)


# Create a dictionary of students and their scores, then print names of students who scored above 75.

students_scores = {
    "prathamsinh": 82,
    "raj": 68,
    "rachit": 90,
    "yash": 74,
    "vatsal": 78
}

print("Students who scored above 75:")
for name, score in students_scores.items():
    if score > 75:
        print(name)



