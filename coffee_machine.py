from data import MENU, resource

profit = 0


def is_recourse_sufficient(order):
    for item in order:
        if order[item] >= resource[item]:
            print(f"sorry there is not enough {item}.")
            return False
    return True


def process_coin():
    print("Please insert coin.")
    total = int(input("How many quarters? :")) * 0.25
    total += int(input("How many quarters? :")) * 0.1
    total += int(input("How many quarters? :")) * 0.05
    total += int(input("How many quarters? :")) * 0.01
    return total


def is_transaction_successful(payment_received, drink_cost):
    if drink_cost <= payment_received:
        change = round(payment_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not a enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resource[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy")


is_on = True
while is_on:
    choice = input("What whould you like? (espresso/latte/cappuccino) :")
    if choice == 'off':
        print('Turning off...')
        is_on = False
    elif choice == 'report':
        print(f"water: {resource['water']}ml")
        print(f"milk: {resource['milk']}ml")
        print(f"coffee: {resource['coffee']}g")
        print(f"money: ${profit}")
    else:
        drink = MENU[choice]
        if is_recourse_sufficient(drink['ingredients']):
            payment = process_coin()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
