start_game = True
while start_game:
    user_password = input("please enter the correct password ").lower()
    if user_password == 'opensesame':
        print("password is correct")
        break
    else:
        print("incorrect password")
