from menu import MENU, resources

# variables declare
end_game = True
money = 0

# coins
penny = 0.001
nickel = 0.005
dime = 0.01
quarter = 0.25
change = 0

# resource variable
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]

# espresso variable
espresso_water = MENU["espresso"]["ingredients"]["water"]
espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]
espresso_cost = MENU["espresso"]["cost"]

# latte variable
latte_water = MENU["latte"]["ingredients"]["water"]
latte_milk = MENU["latte"]["ingredients"]["milk"]
latte_coffee = MENU["latte"]["ingredients"]["coffee"]
latte_cost = MENU["latte"]["cost"]

# cappuccino variable
cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
cappuccino_cost = MENU["cappuccino"]["cost"]


def report(resources):
    return f"Water: {water} \nMilk: {milk} \nCoffee:{coffee} \nMoney:{money}"


def transaction(coins):
    if coins < espresso_cost:
        return "Sorry that's not enough money. Money refunded."
    elif coins < latte_cost:
        return "Sorry that's not enough money. Money refunded."
    elif coins < cappuccino_cost:
        return "Sorry that's not enough money. Money refunded."


def resources_check(user_input, water, milk, coffee):
    # espresso
    if user_input == "espresso":
        if water < espresso_water:
            return "Sorry there is not enough water."
        elif coffee < espresso_coffee:
            return "Sorry there is not enough coffee."
    # latte
    if user_input == "latte":
        if water < latte_water:
            return "Sorry there is not enough water."
        elif coffee < latte_coffee:
            return "Sorry there is not enough coffee."
        elif milk < latte_milk:
            return "Sorry there is not enough milk."
    # cappuccino
    if user_input == "cappuccino":
        if water < cappuccino_water:
            return "Sorry there is not enough water."
        elif coffee < cappuccino_coffee:
            return "Sorry there is not enough coffee."
        elif milk < cappuccino_milk:
            return "Sorry there is not enough milk."


while end_game:
    # user input dialog
    input_prompt = input("What would you like? (espresso/latte/cappuccino): ")

    # Turn off the Coffee Machine
    if input_prompt == "off":
        end_game = False
    # print resource report
    elif input_prompt == "report":
        print(report(resources=resources))
    else:
        enter_penny = int(input(f"How many penny?: "))
        enter_nickel = int(input(f"How many nickel?: "))
        enter_dime = int(input(f"How many dime?: "))
        enter_quarter = int(input(f"How many quarter?: "))
        coins = (enter_penny * penny) + (enter_nickel * nickel) + (enter_dime * dime) + (enter_quarter * quarter)

        if input_prompt == "espresso":
            if water < espresso_water or coffee < espresso_coffee:
                print(resources_check(user_input=input_prompt, water=water, milk=milk, coffee=coffee))
            elif coins < espresso_cost:
                print(transaction(coins))
            else:
                water = water - espresso_water
                coffee = espresso_coffee
                money = espresso_cost
                change = coins - espresso_cost
                print(f"Here is ${round(change, 2)} dollars in change.")
                print("Here is your espresso. Enjoy!")

        elif input_prompt == "latte":
            if water < latte_water or coffee < latte_coffee or milk < latte_milk:
                print(resources_check(user_input=input_prompt, water=water, milk=milk, coffee=coffee))
            elif coins < latte_cost:
                print(transaction(coins))
            else:
                water = water - latte_water
                coffee = latte_coffee
                money = latte_cost
                change = coins - latte_cost
                print(f"Here is ${round(change, 2)} dollars in change.")
                print("Here is your latte. Enjoy!")

        elif input_prompt == "cappuccino":
            if water < cappuccino_water or coffee < cappuccino_coffee or milk < cappuccino_milk:
                print(resources_check(user_input=input_prompt, water=water, milk=milk, coffee=coffee))
            elif coins < cappuccino_cost:
                print(transaction(coins))
            else:
                water = water - cappuccino_water
                coffee = cappuccino_coffee
                money = cappuccino_cost
                change = coins - cappuccino_cost
                print(f"Here is ${round(change, 2)} dollars in change.")
                print("Here is your cappuccino. Enjoy!")