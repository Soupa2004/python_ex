from menu import coffeee
class money :
    global initial_cost
    initial_cost=0
    
    def money_list(self,choice) :
        global initial_cost
        if choice == "latte" :
            num = 3.50 
        elif choice =="espresso" :
            num = 2.50
        elif choice ==  "americano" :
            num = 2.80
        elif choice =="cappacino" :
            num = 1.50

        ten=int(input("enter the number 0f 10 $ coins "))
        five=int(input("enter the number 0f 5 $ coins "))
        two=int(input("enter the number 0f 2 $ coins "))
        one=int(input("enter the number 0f 1 $ coins "))
        amount=ten *10+five*5+two*2+one*1
        if num > amount :
            return False
        else :
            change=amount-num
            print(f"heres your change of $ {change}")
            initial_cost+=num
            
    def report(self) :
        global initial_cost
        print(f"total money in machine is : $ {initial_cost}")