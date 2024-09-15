# control flow with if/else
# if condition:
#     do this
# else:
#     do this

# comparision operator:
# > greater than
# < less than
# >= greater than equal to
# <= less than equal to
# == equal to
# != not equal to

# nested if/else:
#
# if condition:
#     if another condition:
#         do this
#     else :
#         do this
# else :
#     do this

# if / elif / else:
#
# if cond1:
#     do a
# elif cond2:
#     do b
# else:
#     do c

# leap year code:
# year = int(input("write year here:"))
# if year%4 == 0 :
#   if year%100 == 0:
#     if year%400 == 0:
#       print("Leap year")
#     else:
#       print("Not leap year")
#   else:
#     print("Leap year")
# else:
#   print("Not leap year")

# logical operators
# A and B
# A or B
# not B

# print("The Love Calculator is calculating your score...")
# name1 = input("What is your name?")
# name2 = input("name?")
#
#
# name = name1 + name2
# lower_name = name.lower()
# t = lower_name.count("t")
# r = lower_name.count("r")
# u = lower_name.count("u")
# e = lower_name.count("e")
# first = t + r + u + e
#
# l = lower_name.count("l")
# o = lower_name.count("o")
# v = lower_name.count("v")
# e = lower_name.count("e")
# second = l + o + v + e
#
# score = int(str(first) + str(second))
#
# if (score<10) or (score>90):
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score>=40) and (score<=50):
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")

print("Welcome to treasure isalnd.\nYour mission is to find the treasure.")

road = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' \n").lower()

if road == "left":
    lake = input("You came to a lake. There is an island in the middle of lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if lake == "wait":
        door = input("You arrive at the island uharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if door == "yellow":
            print("You win!")
        else:
            print("Game over.")
    else:
        print("Game over.")
else:
    print("Game over.")
