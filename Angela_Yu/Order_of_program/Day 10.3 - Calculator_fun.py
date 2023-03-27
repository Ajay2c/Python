#ADD
def add(f_num,s_num):
    return f_num + s_num
#SUB
def sub(f_num,s_num):
    return f_num - s_num
#MULTI
def multi(f_num,s_num):
    return f_num * s_num
#DIVISION
def div(f_num,s_num):
    return f_num / s_num
#SQURE
def squre(f_num,s_num):
    return f_num ** s_num
#MODULE
def mod(f_num,s_num):
    return f_num % s_num

operations = {
    "+":add,
    "-":sub,
    "*":multi,
    "/":div,
    "**":squre,
    "%":mod,         
}



print("Welcome to the calculator program!")
f_number = int(input("Please enter your first number: "))
operation_symb = input("Choose an operation (+, -, *, /, **, %): ")
s_number = int(input("Please enter your second number: "))

first_cal = operations[operation_symb]
first_output = first_cal(f_num=f_number,s_num=s_number)

print(f"{f_number} {operation_symb} {s_number} = {first_output}")

cal_again = False
while not cal_again:
    want_cal_another = input(f"Type 'y' to continue calculating with {first_output}, or type 'n' to exit.: ")

    if want_cal_another == "y":
                
            operation_symb = input("Choose an operation (+, -, *, /, **, %): ")
            t_number = int(input("Please enter your second number: "))
            sec_cal = operations[operation_symb]
            sec_output = sec_cal(first_output,t_number)

            print(f"{first_output} {operation_symb} {t_number} = {sec_output}")
    else:
        cal_again = True

