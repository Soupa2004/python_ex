import random
import stagesss
import wordlist
lives=0
res_string=[]


word_choice=random.choice(wordlist.word_list)
length=len(word_choice)
und_length="_ " * length
game_over=False
print(und_length)
while game_over != True:
    fun_string=""
    input_user=input("enter the character you guessed : ").lower()
    
    if input_user in res_string:
        print("you have entered the letter " +input_user+" "+"already !! DONT WORRY YOU WONT LOSE A LIFE")
    for ind_char in word_choice:
        if ind_char == input_user:
            fun_string+= ind_char 
            res_string.append(ind_char)
        elif ind_char in res_string:
            fun_string+=ind_char
        
        else:
            fun_string+=" _ "
    if input_user not in word_choice:
        print("you have entered the letter " +input_user+" "+"which is not present in the word .YOU LOSE A LIFE")
        lives+=1
        print("*********************you have <"+str(6-lives)+ ">/6 left***********************************")
        if lives == 6:
            print("****************************you lost***************************************")
            print("YOU WERE TRYING TO GUESS THE WORD : "+word_choice)
            game_over=True
                
        
    
    print(''+fun_string+'')
    if '_' not in fun_string:
        print("*******************you won*************************")
        game_over=True
    
    print(stagesss.stages[lives])      
    
    