# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇


# total_height = n + 1

# student_total = 0
# for student_total in student_heights:
#     print(student_total + student_heights)


# height_devisible = int(n + 1)
total_height = 0

for height in student_heights:
    total_height += height
print(total_height)

number_of_student = 0
for student in student_heights:
    number_of_student += 1
print(number_of_student)


Average_height = round(total_height/number_of_student)

print(Average_height)

# Numbers = [90, 78, 34, 50, 100, 99]
# higest_number = 0
# for number in Numbers:
#     if number > higest_number:
#         higest_number = number
# print(higest_number)
