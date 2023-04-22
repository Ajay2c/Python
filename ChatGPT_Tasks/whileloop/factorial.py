start_factorial = True

while start_factorial:
    user_input = int(input("please enter your factorial number in correct positive integer: "))
    factorial = 1
    count = 1
    if user_input >= 0:
        while count <= user_input:
            factorial = factorial * count
            count += 1
        print(factorial)
    else:
        print("please enter the valid number in positive inter")
        continue
