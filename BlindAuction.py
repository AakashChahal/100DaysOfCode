from replit import clear
logo = ''' ######                               #                                        
 #     # #      # #    # #####       # #   #    #  ####  ##### #  ####  #    # 
 #     # #      # ##   # #    #     #   #  #    # #    #   #   # #    # ##   # 
 ######  #      # # #  # #    #    #     # #    # #        #   # #    # # #  # 
 #     # #      # #  # # #    #    ####### #    # #        #   # #    # #  # # 
 #     # #      # #   ## #    #    #     # #    # #    #   #   # #    # #   ## 
 ######  ###### # #    # #####     #     #  ####   ####    #   #  ####  #    # 
'''

#HINT: You can call clear() to clear the output in the console.
print(logo)
auction = {}

def winner():
    highest_bid = 0
    for name, bid in auction.items():
        if bid > highest_bid:
            highest_bid = bid
            highest_bidder = name
    return f"The winner is {highest_bidder} with a bid of ${highest_bid}"


while True:
    name = input("What is your name?: ")
    bid = int(input(f"what is your bid {name}:  $"))
    auction[name] = bid
    print("Are there any other bidders? Type yes or no: ")
    bidders = input().lower()
    if bidders != "yes":
        print(winner())
        break
    else:
        clear()