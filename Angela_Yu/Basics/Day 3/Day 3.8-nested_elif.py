print("Welcome to MGM team park!!!")

height = int(input("What is your height in cm? : "))

if height >= 120:
    print("you have a good height to ride the rollercoster")
    age = int(input("Now please enter your age: "))
    if age < 12:
        print("Hi!, you needs to pay $5")
    elif age <= 18:  # (or)
    #elif age > 12 or age < 18:
        print("You have to pay $7 ")
    else:
        print("You have to pay $12 ")
else:
    print("Sorry,you dont have enough height to take a raids")