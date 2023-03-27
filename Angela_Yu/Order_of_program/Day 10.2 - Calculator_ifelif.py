def operation(f_number, s_number, operation_symb):
    if operation_symb == "+":
        return f_number + s_number
    elif operation_symb == "-":
        return f_number - s_number
    elif operation_symb == "*":
        return f_number * s_number
    elif operation_symb == "/":
        return f_number / s_number
    elif operation_symb == "**":
        return f_number ** s_number
    elif operation_symb == "%":
        return f_number % s_number
    else:
        return "Invalid operator choice"


print("Welcome to the calculator program!")
f_number = int(input("Please enter your first number: "))
s_number = int(input("Please enter your second number: "))
operation_symb = input("Choose an operation (+, -, *, /, **, %): ")

output = operation(f_number, s_number, operation_symb)

print(f"{f_number} {operation_symb} {s_number} = {output}")
