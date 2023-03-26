student_score = {
    "Harry": 81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62,
}

student_geade = {}

for key in student_score:
    the_mark = student_score[key]
    if the_mark >= 71 and the_mark <= 80:
        student_geade[key] = "Acceptable"
    elif the_mark >= 81 and the_mark <= 90:
        student_geade[key] = "Exceeds Expectations" 
    elif the_mark >= 91 and the_mark <=100:
            student_geade[key] = "Outstanding"
    else:
         student_geade[key] = "Fail"

print(student_geade)

print(student_score)