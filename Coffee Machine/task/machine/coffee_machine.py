class CoffeeDrink:
    def __init__(self, name, coffee=0, milk=0, water=0, price=0):
        self.name = name
        self.coffee = coffee
        self.milk = milk
        self.water = water
        self.price = price


class CoffeeMachine:
    def __init__(self, coffee=120, milk=540, water=400, cups=9, money=550):
        self.coffee = coffee
        self.milk = milk
        self.water = water
        self.cups = cups
        self.money = money
        self.drinks = []

    def add_drink(self, drink: CoffeeDrink):
        self.drinks.append(drink)

    def buy(self, n_drink):
        drink = self.drinks[n_drink-1]
        if self.water < drink.water:
            fault = "water"
        elif self.milk < drink.milk:
            fault = "milk"
        elif self.cups < 1:
            fault = "cups"
        elif self.coffee < drink.coffee:
            fault = "coffee"
        else:
            self.money += drink.price
            self.water -= drink.water
            self.milk -= drink.milk
            self.cups -= 1
            self.coffee -= drink.coffee
            return "I have enough resources, making\nyou a coffee!\n"
        return f"Sorry, not enough {fault}!\n"

    def fill(self):
        print("Write how many ml of water do you want to add:")
        self.water += int(input("> "))
        print("Write how many ml of milk do you want to add:")
        self.milk += int(input("> "))
        print("Write how many grams of coffee beans do you want to add:")
        self.coffee += int(input("> "))
        print("Write how many disposable cups of coffee do you want to add:")
        self.cups += int(input("> "))
        print()

    def take(self):
        print(f'I gave you ${self.money}\n')
        self.money = 0

    def __str__(self):
        return (f"""The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee} of coffee beans
{self.cups} of disposable cups
${self.money} of money\n""")

    def __repr__(self):
        return f"CoffeeMachine({self.water}, {self.milk}, {self.coffee}, {self.cups}, {self.money})"


coffee_machine = CoffeeMachine()
coffee_machine.add_drink(CoffeeDrink("espresso", 16, 0, 250, 4))
coffee_machine.add_drink(CoffeeDrink("latte", 20, 75, 350, 7))
coffee_machine.add_drink(CoffeeDrink("cappuccino", 12, 100, 200, 6))


def menu():
    while True:
        print("Write action (buy, fill, take, remaining, exit):")
        option = input('> ')
        print()
        if option == "buy":
            while True:
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
                option = input("> ")
                if option == "back":
                    break
                elif option in ["1", "2", "3"]:
                    print(coffee_machine.buy(int(option)))
                    break

        elif option == "fill":
            coffee_machine.fill()

        elif option == "take":
            coffee_machine.take()

        elif option == "remaining":
            print(coffee_machine)

        elif option == "exit":
            break


if __name__ == '__main__':
    menu()
