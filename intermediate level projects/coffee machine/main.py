MENU = {
    "espresso": {
        "ingredients": {
            "milk": 0,
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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def selection():
    resources['water'] -= int(MENU[choice]['ingredients']['water'])
    resources['milk'] -= int(MENU[choice]['ingredients']['milk'])
    resources['coffee'] -= int(MENU[choice]['ingredients']['coffee'])
    global profit
    profit += MENU[choice]['cost']

def money():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def check_money(amount):
    if amount > MENU[choice]['cost']:
        change = amount - MENU[choice]['cost']
        print(f"Here's your {choice}. Take your change {change}. Have a nice day!")
    else:
        print("I'm sorry. Amount is insufficient. You'll get your refund shortly")




continue_game = True
while continue_game:
    choice = input("What would you like? (espresso/ latte/ cappuccino): ").lower()
    if choice == "off":
        break
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Profit: {profit}")
    else:
        if (resources['water'] >= MENU[choice]['ingredients']['water'] and resources['milk'] >= MENU[choice]['ingredients']['milk'] and resources['coffee'] >= MENU[choice]['ingredients']['coffee']):
            amount = money()
            check_money(amount)
            selection()
        else:
            print("I'm sorry. Insufficient resources")
            continue_game = False









