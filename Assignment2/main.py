import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    ###  write the rest of the codes ###
    while (True):
        sandwich_machine = sandwich_maker_instance
        print("Welcome to the Sandwich Machine!")
        choice = input("What would you like? (small/ medium/ large/ off/ report)").lower()
        if choice in recipes:
            sandwich = recipes[choice]
            if sandwich_machine.check_resources(sandwich["ingredients"]):
                print(f"You owe ${sandwich['cost']}")
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, sandwich["cost"]):
                    sandwich_machine.make_sandwich(choice, sandwich["ingredients"])
        elif choice == "off":
            exit(0)

        elif choice == "report":
            print(resources)
if __name__=="__main__":
    main()
