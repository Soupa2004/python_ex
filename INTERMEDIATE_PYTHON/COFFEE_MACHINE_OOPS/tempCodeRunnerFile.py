from payment import money
from make_coffee import coffee
from menu import make_list

payment = money()
make_coffee = coffee()
list = make_list()

is_on = True  # Initialize as True to start the loop
while is_on:
    choice = str(input(f"Enter the coffee needed: {list} ")).lower()
    choice.lower()
    # Handle input
    if choice == "off":
        is_on = False  # End the program
    elif choice == "report":
        make_coffee.report()
        payment.report()
        # Call the report method
    else:
        make_coffee.make_coffee(choice)