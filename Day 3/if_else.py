# if condition: 
#     do this    - indented block of code, its exected if its met the upper condition
# else:
#     do this


water_level = int(input("Please enter the water level"))


if water_level > 80:
    print("Trun of the tap,the water is over flow")
else:
    print("no need to turn off the tap,the water is not fill")




water_level = int(input("Please enter the water level"))        #Assignment

if water_level == 80:                                           #Check Equality
    print("Trun of the tap,the water is over flow")
else:
    print("no need to turn off the tap,the water is not fill")