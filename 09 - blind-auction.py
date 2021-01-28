import os
#HINT: You can call os.system('clear') to clear the output in the console.
from art_bid import logo

print(logo)
print("Welcome to the secret auction program.\n")
auction_final = {}
bidders = True


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


while bidders:
    name = input("What is your name?: ")
    bid_price = int(input("What is the bid?: $"))
    auction_final[name] = bid_price
    other = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if other == "yes":
        os.system('clear')
    elif other == "no":
        os.system('clear')
        bidders = False
        find_highest_bidder(auction_final)

#

