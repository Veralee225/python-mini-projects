from art import logo
from replit import clear
print(logo)

total_bids = {}
bid_end = False

# This function finds the highest bidder
def highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""

# record of bidders
for bidder in bidding_record:
  bid_amount = bidding_record[bidder]
  if bid_amount > highest_bid:
    highest_bid = bid_amount
    winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bid_end:

user_name = int(input("What is your name"))

bid_price = ("What is your bidding price? ")

total_bid = {
    "Mathew": "100",
    "zen": "200",
    "Cynthia": 50
}
