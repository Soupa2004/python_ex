
def my_function():
    num1=float(input("enter the number 1 : "))
    num2=float(input("enter the number 2 : "))
    inp=str(input(" what do you want to do '+','-','*','/' : "))
    if inp == '+':
         return num1+num2
    elif inp == '-':
        return num1-num2
    elif inp == '*':
        return num1*num2
    elif  inp == '/':
        if num2 ==0:
            return "infinity"
        return num1/num2
    else:
        print("enter valid operation")
def my_function1(my_function,num2):
    num1=my_function
    inp=str(input(" what do you want to do '+','-','*','/' : "))
    if inp == '+':
        res=num1+num2
        return res
    elif inp == '-':
        res=num1-num2
        return res
    elif inp == '*':
        res=num1*num2
        return res
    elif  inp == '/':
        if num2==0:
            return "infinity"
        return num1/num2
    else:
        print("enter valid operation")
game_over =False
num_count=0
num1=0
while game_over != True :
    if num_count==0 :
        num1=my_function()
        print(num1)
        num_count+=1
    elif num_count>=1:
        choice=str(input("enter 'y' to continue 'n' to start over 'x' to exit : "))
        if choice == 'y':
            num2=float(input("enter the number 2 : "))
            result=my_function1(num1,num2)
            num1=result
            print(num1)
        elif choice == 'n':
            num_count=0
            print("\n"*506)
        elif choice == 'x':
            print("THANK YOU !!!!!")
            game_over =True
        else:
            print("YOU DID NOT ENTER VALID CHOICE !! EXITED")
    else:
        game_over=True
                