print("Welcome to MGM team park!!!")

height = int(input("What is your height in cm? : "))
bill = 0

if height >= 120:
    print("you have a good height to ride the rollercoster")
    age = int(input("Now please enter your age: "))
    if age < 12:
        bill = 5
        print("Hi!, you needs to pay $5")
    elif age <= 18:  # (or)
    #elif age > 12 or age < 18:
        bill = 7
        print("You have to pay $7 ")
    else:
        bill = 12
        print("You have to pay $12 ")
    wants_photo = input("You want to take a Photo? Y or N. ")
    if wants_photo == "Y":
       bill += 3
    print(f"Your final result: {bill}")

else:
    print("Sorry,you dont have enough height to take a raids")