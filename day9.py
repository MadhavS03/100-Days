# Dictionary
from replit import clear
# {key:value}

# dictionary = {
# "a":"hello",
# "b":"bye",
# }
#
# print(dictionary["a"])

# dictionary["c"] = "how is u"

# dictionary = {}

# dictionary["b"] = "no"

# print(dictionary)

# loop through a dictionary
# for key in dictionary:
#     print(key)
#     print(dictionary[key])

#Nesting list in a dictionary

# travel_log = {
# "India": ["gurgaon", "delhi", "mumbai"],
# "US": ["LA", "NYC"],
# }

#Nesting dictionary in dictionary

# travel_log = {
# "India": {"cities_visited": ["gurgaon", "delhi", "mumbai"], "total_visits": 11},
# "US": ["LA", "NYC"],
# }

# Nesting dictionary in a list
#
# travel_log = [
#     {"country":"India",
#      "cities_visited": ["gurgaon", "delhi", "mumbai"],
#      "total_visits": 11
#      },
#     {"country":"US",
#      "cities_visited": ["LA", "NYC"],
#      "visits": 2
#      }
# ]

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
print("Welcome to the secrect auction program")

# bidders = {}
# def new_user():
#     name = input("What is your name?\n")
#     bid = input("What is your bid?\n")
#     bidders[name] = bid
#
# new_user()
# new = input("Are there any other biders? types 'yes' or 'no'\n")
# while new == 'yes':
#     new_user()
#     new = input("Are there any other biders? types 'yes' or 'no'\n")
#     print(bidders)

bidders= {}
bidding_finished =False

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with bid {highest_bid}")

while not bidding_finished:
    name = input("What is your name?")
    bid = int(input("What is your bid?"))
    bidders[name] = bid
    new = input("Are there any more bidders? Type yes or no")
    if new == 'no':
        bidding_finished = True
        highest_bidder(bidders)
    elif new == 'yes':
        clear()
