def compatable(name1,name2):
    name=""
    true="true"
    love="love"
    count1=0
    count2=0
    count=0
    name=name1+name2
    for i in name:
        if i in true:
            count1+=1
    for i in true:
        counter=0
        if i in name:
            counter = name.count(i)
            print(f"the letter {i} is present {counter} times")
            
        else:
            counter = name.count(i)
            print(f"the letter {i} is present {counter} times")
            
    print(count1)
    for i in name:
        if i in love:
            count2+=1
    for i in love:
        counter=0
        if i in name:
            counter = name.count(i)
            print(f"the letter {i} is present {counter} times")
            
        else:
            counter = name.count(i)
            print(f"the letter {i} is present {counter} times")
        
    print(count2) 
    count=(count1*10)+count2
    print(f"love compatability of the two is {count}")
    if count<10 or count > 90:
        print("Your score is", count,  "you go together like coke and mentos.")
    elif count > 40 and count < 50:
        print("Your score is", count, "you are alright together.")
    else:
        print("your score is", count) 
name1=str(input("enter your name : ")) 
name2=str(input("enter your partners name : "))       
            
compatable(name1,name2)