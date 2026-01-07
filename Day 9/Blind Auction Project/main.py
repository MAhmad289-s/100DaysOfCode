# TODO-1: Ask the user for input
def find_highest_bid(bids):
    winner = ""
    highest_bid = 0
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner}.")

bids = {}
bid = float(input("What is your bid?: "))
name = str(input("What is your name?:"))
# TODO-2: Save data into dictionary {name: price}
bids[name] = bid
print(bids)
should_continue = input("Would you like to continue? (Y/N): ")
if should_continue == "Y":
    should_continue = True
else:
    should_continue = False
# TODO-3: Whether if new bids need to be added
while should_continue:
    name = str(input("What is your name?: "))
    bid = float(input("What is your bid?: "))
    should_continue = input("Would you like to continue? (Y/N): ")
    if should_continue == "Y":
        should_continue = True
    else:
        should_continue = False
    bids[name] = bid
    find_highest_bid(bids)
# TODO-4: Compare bids in dictionary




