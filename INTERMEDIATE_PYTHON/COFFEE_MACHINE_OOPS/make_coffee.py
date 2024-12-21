from menu import coffeee
class coffee:
    global total_milk,total_water,total_caffee  
    total_water=1000
    total_caffee=800
    total_milk=1000
    
    def make_coffee(self,choice):
        
        global total_milk,total_water,total_caffee 
        water = coffeee[choice]["water"]
        milk = coffeee[choice]["milk"]
        caffee= coffeee[choice]["caffee"]
            
        if total_water >= water and total_milk >= milk and total_caffee >= caffee :
            print(f"Here is your coffee {choice}")
            total_water-=water
            total_milk-=milk
            total_caffee-=caffee
        
            
    def report(self) :
        global total_milk,total_water,total_caffee
        print("total water left : " , total_water , "ml" )
        print("total milk left : " , total_milk , "ml")
        print("total caffee left :", total_caffee , "ml")
    def is_there_enough(self,choice) :
        water = coffeee[choice]["water"]
        milk = coffeee[choice]["milk"]
        caffee= coffeee[choice]["caffee"]
        if total_water < water or total_milk < milk or total_caffee < caffee :
            if total_water < water:
                print("insufficient water. ")
                
            if total_milk < milk:
                print("insufficient milk. ")
                
            if total_caffee < caffee:
                print("insufficient caffee. ")
            return False
            