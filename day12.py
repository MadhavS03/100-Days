# # scope
#
# enemies = 1
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function {enemies}")
#
# increase_enemies()
# print(enemies)
#
# #local scope
#
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
# drink_potion()
# print(potion_strength)
#
# #global scope
#
# player_health = 10
#
# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)
#
#     drink_potion()
#
# print(player_health)
#
# # There is no block scope
#
# game_level = 3
# enemies = ['zombie', 'alien']
#
# if game_level < 5:
#     new_enemy = enemies[0]
#
# print(new_enemy)

# game_level = 3
# def game():
#     enemies = ['zombie', 'alien']
#     if game_level < 5:
#         new_enemy = enemies[0]
#
# print(new_enemy)

#### MODIFYING GLOBAL SCOPE

# enemies = 1
#
# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"enemies inside function {enemies}")
#
# increase_enemies()
# print(enemies)

#### AVOID TO MODIFY GLOBAL SCOPE

# enemies = 4
# def increase_enemies():
#     print(f"enemies inside function {enemies}")
#
# increase_enemies()
# print(enemies)

# enemies = 1
# def increase_enemies():
#     print(f"enemies inside function {enemies}")
#     return enemies + 1
#
# enemies = increase_enemies()
# print(enemies)


#global constanst

# PI = 3.14

import random
logo = """
  _____                   __  __                         __          
 / ___/_ _____ ___ ___   / /_/ /  ___   ___  __ ____ _  / /  ___ ____
/ (_ / // / -_|_-<(_-<  / __/ _ \/ -_) / _ \/ // /  ' \/ _ \/ -_) __/
\___/\_,_/\__/___/___/  \__/_//_/\__/ /_//_/\_,_/_/_/_/_.__/\__/_/   
                                                                     
"""

the_number = random.randint(1, 100)
game_won = False
attempts = 0
print(the_number)
print(logo)
print("Welcome to the number guessing game! \nI'm thinking of a number between 1-100.")


def guess():
    global game_won
    guess_number = int(input("Make a guess: "))
    if attempts == 0 and guess_number > the_number:
        print(f"Too high\nYou've run out of attempts, you lose, the number was {the_number}")
        game_won = True
    if attempts == 0 and guess_number < the_number:
        print(f"Too low\nYou've run out of attempts, you lose, the number was {the_number}")
        game_won = True
    if guess_number > the_number and attempts > 0:
        print("Too high\nGuess again")
    if guess_number < the_number and attempts > 0:
        print("Too low\nGuess again")
    if guess_number == the_number:
        print(f"You got it!, The answer was {the_number}")
        game_won = True

def easy():
    global attempts
    attempts = 10
    global game_won
    while not game_won:
       print(f"You have {attempts} attempts remaining to guess the number")
       attempts -= 1
       guess()
       if attempts == 0:
           game_won = True

def hard():
    global attempts
    attempts = 5
    global game_won
    while not game_won:
        print(f"You have {attempts} attempts remaining to guess the number")
        attempts -= 1
        guess()
        if attempts == 0:
            game_won = True



difficulty = input("Choose a difficulty easy or hard: ")
if difficulty == 'easy':
    easy()
elif difficulty == 'hard':
    hard()

