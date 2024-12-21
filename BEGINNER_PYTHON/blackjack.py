import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
player=[]
computer=[]
p_sum=0
c_sum=0
def black():
    global p_sum,c_sum
    p_1=random.choice(cards)
    p_2=random.choice(cards)
    player.append(p_1)
    player.append(p_2)
    print("players cards are :" ,player)
    p_sum=sum(player)
    print("sum is :" ,p_sum)
    p_3=random.choice(cards)
    p_4=random.choice(cards)
    computer.append(p_3)
    computer.append(p_4)
    c_sum=sum(computer)
    print ("the computer cards are : [",computer[0],", x] ")
def blacked():
    global p_sum
    p_3=random.choice(cards)  
    player.append(p_3)
    p_sum=sum(player)
    print("now your cards are :" ,player)
    print("sum is : ",p_sum)
game_over=False
count=0
while game_over != True:
        if count == 0:
            choice=str(input("do you want to play black jack press 'y' else press 'n'  : "))
            if choice =='y':
                black()
                if p_sum == 21  :
                    print(" YOU WIN BY BLACK JACK !!!!!!!!!!")
                    count=0
                elif c_sum ==21 :
                    print("COMPUTER WINS BY BLACK JACK ! ! ! ! ! ")
                    count=0
                elif p_sum ==21 and c_sum == 21 :
                    print("you both have black jacks !!!!!!!! D R A W")
                    count=0
            else:
                print("GAME OVER !!! THANK YOU !!")
                game_over=True
            count+=1
        elif count>=1 :
            if p_sum > 21 :
                print("computer sum is ",c_sum)
                print ("COMPUTER WINS !!!!!!")
                game_over=True
            else :
                choice2=str(input("enter 'hit' to pull a card or enter 'call' to pull out : "))
                if choice2 == 'hit' :
                    blacked()
                    if p_sum == 21  :
                        print(" YOU WIN BY BLACK JACK !!!!!!!!!!")
                        game_over=True
                    if p_sum > 21 :
                        print("computer sum is ",c_sum)
                        print ("COMPUTER WINS !!!!!!")
                        game_over=True
                elif choice2 == 'call' :
                    if p_sum > c_sum :
                        print("computer sum is ",c_sum)
                        print(" YOU WIN !!!!!!!!!!")
                        game_over=True
                    elif p_sum < c_sum :
                        print("computer sum is ",c_sum)
                        print("COMPUTER WINS !!!!!!!!!!!")
                        game_over=True
                    elif p_sum == c_sum :
                        print("computer sum is ",c_sum)
                        print ("both have equal count D R A W !!!!!!!")
                        game_over=True
                else:
                    print("enter valid choice ")
        else:
            game_over=True
                
                
                
                
              
    