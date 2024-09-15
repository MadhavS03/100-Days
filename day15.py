### Coffee machine project ###

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

coffe_machine = True

latte = menu["latte"]
latte_ing = latte["ingredients"]

espresso = menu["espresso"]
espresso_ing = espresso["ingredients"]

cappuccino = menu["cappuccino"]
cappuccino_ing = cappuccino["ingredients"]

while coffe_machine:

    def report():
        """prints the currently available resources in the coffee machine"""
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gm")
        print(f"Money: ${resources['money']}")


    def resources_check(prompt):
        """Checks the resources available for the coffee chosen and prints if some ingredient is not enough"""
        if prompt == 'latte':
            if resources["water"] >= latte_ing["water"]:
                if resources["milk"] >= latte_ing["milk"]:
                    if resources["coffee"] >= latte_ing["coffee"]:
                        coin_check(prompt)
                    else:
                        print("Sorry not enough coffee")
                else:
                    print("Sorry not enough milk")
            else:
                print("Sorry not enough water")
        if prompt == 'espresso':
            if resources["water"] >= espresso_ing["water"]:
                if resources["coffee"] >= espresso_ing["coffee"]:
                    coin_check(prompt)
                else:
                    print("Sorry not enough coffee")
            else:
                print("Sorry not enough water")
        if prompt == 'cappuccino':
            if resources["water"] >= cappuccino_ing["water"]:
                if resources["milk"] >= cappuccino_ing["milk"]:
                    if resources["coffee"] >= cappuccino_ing["coffee"]:
                        coin_check(prompt)
                    else:
                        print("Sorry not enough coffee")
                else:
                    print("Sorry not enough milk")
            else:
                print("Sorry not enough water")


    def coin_check(prompt):
        """checks if the total money in coins is sufficient for the selected coffee, if yes then gives coffee if not then refunds money"""
        print("Please insert coins:")
        quarter = int(input("How many quarters?: "))
        dime = int(input("How many dimes?: "))
        nickle = int(input("How many nickles?: "))
        penny = int(input("How many pennies?: "))
        quarters = quarter * 0.25
        dimes = dime * 0.10
        nickles = nickle * 0.05
        pennies = penny * 0.01
        total = quarters + dimes + nickles + pennies
        if prompt == 'latte':
            if total >= latte['cost']:
                print(f"Here is ${total - latte['cost']} your change.")
                print("Here is your latte, Enjoy!")
                make_coffee(prompt)
            else:
                print("Sorry that's not enough money. Money refunded.")
        if prompt == 'espresso':
            if total >= espresso['cost']:
                print(f"Here is ${total - espresso['cost']} your change.")
                print("Here is your espresso, Enjoy!")
                make_coffee(prompt)
            else:
                print("Sorry that's not enough money. Money refunded.")
        if prompt == 'cappuccino':
            if total >= cappuccino['cost']:
                print(f"Here is ${total - cappuccino['cost']} your change.")
                print("Here is your cappuccino, Enjoy!")
                make_coffee(prompt)
            else:
                print("Sorry that's not enough money. Money refunded.")


    def make_coffee(prompt):
        """Deducts the ingredients quantity used of the selected coffee type from the resources"""
        if prompt == 'latte':
            resources["money"] += latte['cost']
            resources["water"] -= latte_ing['water']
            resources["milk"] -= latte_ing['milk']
            resources["coffee"] -= latte_ing['coffee']
        if prompt == 'espresso':
            resources["money"] += espresso['cost']
            resources["water"] -= espresso_ing['water']
            resources["coffee"] -= espresso_ing['coffee']
        if prompt == 'cappuccino':
            resources["money"] += cappuccino['cost']
            resources["water"] -= cappuccino_ing['water']
            resources["milk"] -= cappuccino_ing['milk']
            resources["coffee"] -= cappuccino_ing['coffee']

    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if prompt == "off":
        coffe_machine = False
    if prompt == 'latte' or prompt == 'cappuccino' or prompt == 'espresso':
        resources_check(prompt)
    if prompt == 'report':
        report()



### ALTERNATIVE ###

# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
# profit = 0
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
#
# def is_resource_sufficient(order_ingredients):
#     """Returns True when order can be made, False if ingredients are insufficient."""
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"​Sorry there is not enough {item}.")
#             return False
#     return True
#
#
# def process_coins():
#     """Returns the total calculated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total
#
#
# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False
#
#
# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️. Enjoy!")
#
#
# is_on = True
#
# while is_on:
#     choice = input("​What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])









