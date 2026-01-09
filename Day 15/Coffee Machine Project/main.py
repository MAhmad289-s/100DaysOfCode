from random import choice

from math import trunc

MENU = {
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
}
def enough_ingredients(order_ingredients):
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry, {ingredient} is not sufficient.")
            return False
    return True
def transaction():
    total_money_input = 0
    print("Please enter the coins required: ")
    total_money_input += int(input("How many quarters?: ")) * 0.25
    total_money_input += int(input("How many dimes?: ")) * 0.1
    total_money_input += int(input("How many nickles?: ")) * 0.05
    total_money_input += int(input("How many pennies?: ")) * 0.01
    return total_money_input
def transaction_sucessful(drink_cost,total_money_input ):
    if total_money_input >= drink_cost:
        change = round( total_money_input - drink_cost,2)
        print(f"That's enough money now here is your {change} dollars.")
        profit = 0
        profit += drink_cost
        return True
    else:
        print(f"Sorry, that's not enough money. Money refunded.")
        return False
def make_coffee(order_ingredients):
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]
        print(f"Here is your coffe")
        break

machine_one = True

while machine_one:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        machine_one = False
    elif choice == "report":
        print(f"Your coffe: {resources['water']}")
        print(f"Your coffe: {resources['milk']}")
        print(f"Your coffe: {resources['coffee']}")
    else:
        drink = MENU[choice]
        if enough_ingredients(drink["ingredients"]):
            payment = transaction()
        if transaction_sucessful(drink["cost"],payment):
            make_coffee(drink["ingredients"])




