logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""



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

def calculator():
    print(logo)
    print("Welcome to the calculator program!")
    f_number = int(input("Please enter your first number: "))
    cal_again = True
    while cal_again:
        operation_symb = input("Choose an operation (+, -, *, /, **, %): ")
        s_number = int(input("Please enter your next number: "))
        function_op = operations[operation_symb]
        function_op_output = function_op(f_num=f_number,s_num=s_number)

        print(f"{f_number} {operation_symb} {s_number} = {function_op_output}")

        want_cal_another = input(f"Type 'y' to continue calculating with {function_op_output}, or type 'n' to exit.: ")
        if want_cal_another == "y":
                f_number = function_op_output
        else:
            cal_again = False
            calculator()
calculator()