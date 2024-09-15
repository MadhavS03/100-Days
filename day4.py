# randomisation
import random

# random_integer =  random.randint(1,10)
# print(random_integer)

# generates a random float no between 0.0 to 1.0
# random_float = random.random()
# print(random_float)

# lists

# fruits = ['apple', 'mango', 'pear']
# print(fruits[1])
#
# fruits[2] = 'banana'
# fruits.append('grapes')
# fruits.extend(['orange', 'watermelon'])
# print(fruits)
#
# vegetables = ['potato', 'spinach']
#
# eatables = [fruits, vegetables]
# print(eatables)

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
comp_choice = random.randint(0,2)
print(f"Computer chose {comp_choice}")

if player_choice >= 3 or player_choice < 0:
    print('invalid')
elif player_choice == 0 and comp_choice == 2:
    print('You win!')
elif comp_choice == 0 and player_choice == 2:
    print('You lose!')
elif comp_choice > player_choice:
    print('You lose.')
elif player_choice > comp_choice:
    print('You win!')
elif comp_choice == player_choice:
    print('draw')

