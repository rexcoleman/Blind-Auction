from art import logo
# from replit import clear
#HINT: You can call clear() to clear the output in the console.

print(logo)


bids = {}

winner = ""

def find_highest_bidder(bidding_record):
    highest_bid = int(0)
    winner = ""
    # clear()
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            winner = bidder
            highest_bid = bid_amount
            print(highest_bid)        
    print(f"The winner is: {winner} with a bid of: ${highest_bid}")
    

def bidding_process():
    collate_bids = True
    while collate_bids == True:
        name = input("What is your name?:\n")
        bid = int(input("What is your bid?: $\n"))
        bids[name] = bid
        # print(bids)
        add_bidder = input('Are there any other bidders: "yes" or "no"?\n')
        if add_bidder == "no":
            collate_bids = False
            find_highest_bidder(bids)
        # elif add_bidder == "yes":
            # clear()
        # print(bids)
      

bidding_process()






