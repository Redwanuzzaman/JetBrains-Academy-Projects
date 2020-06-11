class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.disposable_cups = 9
        self.money = 550

    def main(self):
        action = input("Write action (buy, fill, take, remaining, exit):\n")
        while action != "exit":
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.remaining()
            else:
                print("Invalid Option. Choose Again")

            action = input("\nWrite action (buy, fill, take, remaining, exit):\n")

    def remaining(self):
        print("The coffee machine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.beans) + " of coffee beans")
        print(str(self.disposable_cups) + " of disposable cups")
        print("$" + str(self.money) + " of money")

    def buy(self):
        choice = (input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"))

        if choice == "1":
            if self.water >= 250 and self.beans >= 16:
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.disposable_cups -= 1
            elif self.water < 250:
                print("Sorry, not enough water!")
            elif self.beans < 16:
                print("Sorry, not enough coffee beans!")
        elif choice == "2":
            if self.water >= 350 and self.milk >= 75 and self.beans >= 20:
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.disposable_cups -= 1
            elif self.water < 350:
                print("Sorry, not enough water!")
            elif self.milk < 75:
                print("Sorry, not enough milk!")
            elif self.beans < 20:
                print("Sorry, not enough coffee beans!")
        elif choice == "3":
            if self.water >= 200 and self.milk >= 100 and self.beans >= 12:
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.disposable_cups -= 1
            elif self.water < 200:
                print("Sorry, not enough water!")
            elif self.milk < 100:
                print("Sorry, not enough milk!")
            elif self.beans < 12:
                print("Sorry, not enough coffee beans!")
        elif choice == "back":
            return

    def fill(self):
        new_water = int(input("Write how many ml of water do you want to add:"))
        new_milk = int(input("Write how many ml of milk do you want to add:"))
        new_beans = int(input("Write how many grams of coffee beans do you want to add:"))
        new_disposable_cups = int(input("Write how many disposable cups of coffee do you want to add:"))

        self.water += new_water
        self.milk += new_milk
        self.beans += new_beans
        self.disposable_cups += new_disposable_cups

        print()

    def take(self):
        print("I gave you $" + str(self.money))
        self.money = 0


coffee_machine = CoffeeMachine()
coffee_machine.main()
