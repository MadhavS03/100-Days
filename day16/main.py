### Object Orientated Programming ###
### Splitting up big task to smaller modules, such that even in the future it is reuseable  ###
### Attributes - variables associated with modeled object - piece of data ###
### Methods - function a modeled object can do - functionallity  ###
### In OOP we model an obejct that has things (attributes) and can do things (methods) ###
### Object - Attributes(piece of data) + Methods (functionallity) ###
### can also generate multiple objects from the same type or same blueprint ###
###  blueprint - called CLASS , individual objects generated from blueprint - called OBJECT ###

### Object = Class() ###
### car = CarBlueprint() ###

### Object - Method ###
### car.stop() ###

from turtle import Turtle, Screen


# timmy =  Turtle()
# print(timmy)
#
# my_screen = Screen()
# print(my_screen.canvheight)
#
# timmy.shape('turtle')
# timmy.color('blue', 'red')
# timmy.forward(150)
# timmy.left(90)
# timmy.forward(150)
# timmy.left(90)
# timmy.forward(150)
# timmy.left(90)
# timmy.forward(150)
# timmy.left(90)
# my_screen.exitonclick()

# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("City Name",["Gurgaon", "Mumbai"])
# table.add_column("State", ["Harayana", "Maharashtra"])
# table.align = 'l'
#
# print(table)

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

