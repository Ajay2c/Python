year = int(input("which year you want to calculate?: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        elif year % 400 !=0:
            print("Not Leap year")    
    elif year % 100 != 0:
        print("Not Leap year")
elif year % 4 != 0:
    print("Not Leap year")            