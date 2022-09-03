# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇


heigh_score = 0
for maxscore in student_scores:
    if heigh_score < maxscore:
        heigh_score = maxscore
print(f"This is the maximum{heigh_score}")
