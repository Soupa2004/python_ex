from coffee_types import coffeee
from os import system
initial_cost=0
total_water=300
total_caffee=200
total_milk=300
num=0
def cost(amount) :
    global initial_cost
    amount=0
    change=0
    ten=int(input("enter the number 0f 10 $ coins "))
    five=int(input("enter the number 0f 5 $ coins "))
    two=int(input("enter the number 0f 2 $ coins "))
    one=int(input("enter the number 0f 1 $ coins "))
    amount=ten *10+five*5+two*2+one*1
    print(amount)
    if num > amount :
        print("insufficient funds")
    else :
        change=amount-num
        print(f"heres your change of {change}")
        initial_cost+=amount
        
def allocation(choice) :
    water=0
    caffee=0
    milk=0
    global num
    global total_water
    global total_caffee
    global total_milk  
    water = coffeee[choice]["water"]
    caffee= coffeee[choice]["caffee"]
    milk= coffeee[choice]["milk"]
    num=coffeee[choice]["cost"]
    if water > total_water or caffee > total_caffee or milk > total_milk :
        if water > total_water :
            print("insufficient water")
        if caffee > total_caffee :
            print("insufficient caffee")
        if milk > total_milk :
            print("insufficient milk")
    else :
        print(f"here is your {choice}")
        total_water-=water
        total_caffee-=caffee
        total_milk-=milk
        print(water)
        print(caffee)
        print(milk)
        print(total_water)
        print(total_caffee)
        print(total_milk)
        cost(num)

def report() :
    print("total water left : ",total_water)
    print("total milk left : ",total_milk)
    print("total caffine left : ",total_caffee)

game_over = False
while game_over != True :
    global choice
    choice=str(input("enter the type of coffee : (Espresso / Latte / Americano) : "))
    choice.lower()
    if total_water < 30 and total_caffee <64 and  total_milk == 0 :
        print("insufficient items in the coffee_maker to make any coffee ! sorry !") 
        system.exit()
    if choice == 'report' :
        report()
    else :
        allocation(choice)