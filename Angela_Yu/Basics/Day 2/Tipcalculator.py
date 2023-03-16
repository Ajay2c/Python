print("Welcome to tip calculator.")
bill = input("What was the total bill? ")
tip_percent = input("What percentage tip would like to give? 10, 12, or 15? ")
split_people = input("How many people to split the bill? ")

tip_calculate = (int(tip_percent) / 100) * float(bill) 

bill_and_tipamount = float(bill) + float(tip_calculate)

split_total_bill = bill_and_tipamount / int(split_people)

final_amount=(round(split_total_bill,2))

final_amount = "{:.2f}".format(split_total_bill) 
#now when we run this again, using the same inputs, we now get a .60 at
#the very end and this is basically turned this bill_per_person, which is a float into a string. 
# And that string is abiding by this particular format, which is the two decimal places

print(f"Each person should pay: ${final_amount}")






