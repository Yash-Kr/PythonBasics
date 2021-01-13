MENU = {
    "expresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 60,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 90,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when Order can be Made,False if ingredients are insufficient"""
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry there is not enough {item}")
            return False

    return True


def process_money():
    """Returns the total amount inserted"""
    print("Please Insert Amount ?")
    total = 10 * int(input("How many 10s :"))
    total += 20 * int(input("How many 20s :"))
    total += 50 * int(input("How many 50s :"))
    return total


def is_money_sufficient(money, drink_cost, ):
    if money < drink_cost:
        print("Sorry! that's not enough Money. Money Refunded.")
        return False
    else:
        global profit
        profit += drink_cost
        print(f"Transaction Successful . Here is your {money - drink_cost}Rs. change .")
        return True


def make_drink(drink):
    for item in drink["ingredients"]:
        resources[item] -= drink["ingredients"][item]


is_on = True
profit = 0

while is_on:
    choice = input('What would you like ? (expresso/latte/cappuccino) : ')

    if choice == "off":
        is_on = False;
        continue;
    elif choice == "report":
        print(f"water: {resources['water']}")
        print(f"milk:   {resources['milk']}")
        print(f"coffee: {resources['coffee']}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            money = process_money()
            """If User has enough money to purchase"""
            if is_money_sufficient(money, drink["cost"]):
                make_drink(drink)
