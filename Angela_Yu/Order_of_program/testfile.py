from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bids = {}

def the_final(bids):
    win_bid_amount = 0
    win_bid_name = ""
    for key in bids:
            the_high_bid = bids[key]
            if the_high_bid > win_bid_amount:
                win_bid_amount = the_high_bid
                win_bid_name += key
                print(f"the winner is {win_bid_name}, and the bid is {win_bid_amount}")


start_the_bid = False

while not start_the_bid:
    name = input("What is your name?: ")
    bid = input("what is your bid?: $")
    bids[name] = bid
    other_bid = input('Are they any other bid? Type "yes" or "no" ')

    if other_bid == "yes":
        clear()
    elif other_bid == "no":
        the_final()    