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
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  total_bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")

  if should_continue == "no":
    bid_end = True
    highest_bidder(bid_end)
  elif should_continue == "yes":
    clear()