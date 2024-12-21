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

profit = 0
user_coins = 0
resources = {
    "water" : 1000,
    "milk" : 900,
    "coffee" : 100,
}

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]

def check(water,milk,coffee):
    if ask == "latte":
        if water < 200 or milk < 150 or coffee < 24:
           print("Sorry there is not enough water.")
    elif ask == "espresso":
        if water < 50 or  coffee < 18:
           print("Sorry there is not enough water.")
    elif ask == "cappuccino":
        if water < 250 or milk < 100 or coffee < 24:
            print("Sorry there is not enough water.")

def trans():
    if ask == "latte":
        if user_coins < MENU["latte"]["cost"]:
            print(f"Sorry that's not enough money. ${user_coins} refunded.")
        else :
            return ask == "latte"
    elif ask == "espresso":
        if user_coins < MENU["espresso"]["cost"]:
            print(f"Sorry that's not enough money. ${user_coins} refunded.")
        else :
            return ask == "espresso"

    elif ask == "cappuccino":
        if user_coins < MENU["cappuccino"]["cost"]:
            print(f"Sorry that's not enough money. ${user_coins} refunded.")
        else:
            return ask == "cappuccino"

def make (water,milk,coffee,profit):
    if ask == "espresso":
        water -= (MENU[ask]["ingredients"]["water"])
        coffee -= (MENU[ask]["ingredients"]["coffee"])
        profit += MENU[ask]["cost"]
        return water, coffee, profit
    else:
        water -= (MENU[ask]["ingredients"]["water"])
        milk -= (MENU[ask]["ingredients"]["milk"])
        coffee -= (MENU[ask]["ingredients"]["coffee"])
        profit += MENU[ask]["cost"]
        return water,milk,coffee,profit

def report():
    return f"Water:{water}ml\nMilk:{milk}\nCoffee:{coffee}g\nMoney:${profit}"

def coincount(user_coins):
    print("Please insert coins:")
    quart = float(input("how many quarters?:"))*0.25
    dimes = float(input("how many dimes?:"))*0.10
    nick = float(input("how many nickles?:"))*0.05
    pen = float(input("how many pennies?:"))*0.01
    user_coins = quart+dimes+nick+pen
    return user_coins
start = True
while start:
    ask = input("What would you like?.(espresso/latte/cappuccino)\n").lower()
    if ask == "report":
      print(report())
    else:
        check(water,milk,coffee)
        user_coins= coincount(user_coins)
        is_good = trans()
        if is_good:
            if ask == "espresso":
                water, coffee, profit = make(water, milk, coffee, profit)
                change = round((user_coins - profit), 2)
                if change > 0:
                    print(f"Here is ${change} in change")
                print("Here is your Coffe Enjoy")
            else:
                water, milk, coffee, profit = make(water, milk, coffee, profit)
                change = round((user_coins - profit), 2)
                if change > 0:
                    print (f"Here is ${change} in change")
                print("Here is your Coffe Enjoy")

# TODO : 1. Prompt user by asking What would you like?.
# TODO : 2. Turn off the Coffee Machine by entering “off” to the prompt.
# TODO : 3. Print report.
# TODO : 3. Check resources sufficient?.
# TODO : 4. Process coins.
# TODO : 6. Check transaction successful?.
# TODO : 7. Make Coffee,