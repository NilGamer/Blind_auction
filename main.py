from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
bidders = {}
print(logo)
print('Welcome to the secret auction program.')
gameNotEnded = True

def maxBid():
  high_bid = 0
  for key in bidders:
    bid_amount = bidders[key]
    
    if(bid_amount > high_bid):
      high_bid = bid_amount
      winner = key
  
  print(f"The winner is {winner} with a bid of ${high_bid}")
  # bidMax = max(bidders,key = bidders.get)
  # return bidMax


while gameNotEnded:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  bidders[name] = bid
  isContinue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  
  if(isContinue == 'no'):
    # bidMax = maxBid()
    # print(bidList)
    clear()
    # print(f"The winner is {bidMax} with a bid of ${bidders[bidMax]}.")
    maxBid()
    gameNotEnded = False
  else:
    clear()

