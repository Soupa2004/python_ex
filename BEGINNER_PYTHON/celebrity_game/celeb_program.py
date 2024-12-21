from celeb_list import celebrities_followers
import random
celebrities=celebrities_followers

def compare_again(celeb1,celeb3) :
    global chances
    global game_over
    global celeb,celeb2
    print(f"{celeb1}")
    try :
        choice=int(input(f"enter 1 for {celeb1} enter 2 for {celeb3} : "))
        if choice == 1 :
            celeb=celeb1
            other_celeb=celeb3
        elif choice ==2 :
            celeb = celeb3
            other_celeb=celeb1
        else :
            print("enter valid number between 1 and 2 : ")
    except ValueError :
        print("Type a NUMERIC VALUE 1 or 2    Ex : 1")
        choice=int(input(f"enter 1 for {celeb1} enter 2 for {celeb2} : "))
        if choice == 1 :
            celeb=celeb1
            other_celeb=celeb3
        elif choice == 2 :
            celeb = celeb3
            other_celeb=celeb1
        else :
            print("enter valid number between 1 and 2 : ")          
    follow1=0
    follow2=0
    follow1=celebrities_followers.get(celeb)
    follow2=celebrities_followers.get(other_celeb)
    if follow1 > follow2 :
        print(f"{celeb} has {follow1} followers and {other_celeb} has {follow2} followers . ")
        print("you choose right !!!! ")
        chances+=1
        
    elif follow2 > follow1 :
        print(f" {other_celeb} has {follow2} followers and {celeb} has {follow1} followers . ")
        print(f"you lost your score is {chances} . ")
        game_over=True
    


chances=0
used_celeb=[]
celeb1=""
celeb2=""
game_over=False
count=0
global celeb
celeb=""
celeb3=""
other_celeb=""
while game_over != True :
    if count==0 :
        celeb1=random.choice(list(celebrities_followers.keys()))
        celeb2=random.choice(list(celebrities_followers.keys()))
        used_celeb.append(celeb1)
        used_celeb.append(celeb2)
        while celeb1 == celeb2 :
           celeb1=random.choice(list(celebrities_followers.keys()))
           celeb2=random.choice(list(celebrities_followers.keys())) 
        count+=1
        compare_again(celeb1, celeb2)
    elif count >=1 :
        celeb3=random.choice(list(celebrities.keys()))
        while celeb3 in used_celeb :
           celeb3=random.choice(list(celebrities.keys())) 
        used_celeb.append(celeb3)
        compare_again(celeb,celeb3)
        if len(used_celeb) >= len(celebrities_followers):
            print("you beat the game !!!! WOAH")
            game_over =True
            
        
        
        
    
    
    
