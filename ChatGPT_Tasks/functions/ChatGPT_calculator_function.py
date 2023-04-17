def convert_mark_tograde (the_mark):
    grade_letter =[]

    for i in the_mark:
            
        if i >= 90 and i <= 100:
            grade_letter.append("A")
        elif i >= 80 and i <= 89:
            grade_letter.append("B")
        elif i >= 70 and i <= 79:
            grade_letter.append("C")
        elif i >= 60 and i <= 69:
            grade_letter.append("D")
        elif i == 0 and i <= 59:
            grade_letter.append("F")    
    return grade_letter    

def calculate_gpa(new_grade_list):
    gpa_list = []
    for i in new_grade_list:
        if i == "A":
            gpa_list.append(4.0)
        elif i == "B":
            gpa_list.append(3.0)
        elif i == "C":
            gpa_list.append(2.0)
        elif i == "D":
            gpa_list.append(1.0)
        elif i == "F":
            gpa_list.append(0.0)                
    return gpa_list    
    
def average_grade(new_gpa_list):
    total_count =len(new_gpa_list)
    total_average = 0
    for i in new_gpa_list:
        total_average += float(i)
    avg_gpa = total_average / total_count    
    return avg_gpa


grades = [85, 93, 75, 72, 88]
new_grade_list = convert_mark_tograde(grades)
new_gpa_list = calculate_gpa(new_grade_list)
average_gpa= average_grade(new_gpa_list)  


print(new_gpa_list)
print(f"The GPA is: {average_gpa}")