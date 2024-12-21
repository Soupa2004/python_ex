alpha=[' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt():
    name=str(input("enter the word to be encrpted : "))
    shift=int(input("enter the amount of shift : "))
    j=""
    for i in name:
        sigma=0
        if i in alpha:
            sigma=alpha.index(i)
            gamma=sigma+shift
            gamma=gamma%len(alpha) # 4%25=4 but 34%25=9 using modulus we always get right index within bounds
            j+=alpha[gamma]
        else:
            j+=str(i)
    print(j)
def decrypt():
    name=str(input("enter the word to be decoded : "))
    shift=int(input("enter the amount of shift : "))
    j=""
    for i in name:
        if i in alpha:
            sigma=0
            sigma=alpha.index(i)
            gamma=sigma-shift  
            gamma=gamma%len(alpha) # 4%25=4 but 34%25=9 using modulus we always get right index within bounds
            j+=alpha[gamma]
        else:
            j+=str(i)
    print(j)
game_over=False
while game_over != True :
    choice=str(input("enter 'encode' to encryption and 'decode' to decryption and 'exit' to terminate :\n"))
    if choice== 'encode':
        encrypt()
    elif choice== 'exit':
        print('THANK YOU !!!!')
        game_over=True
    elif choice == 'decode':
        decrypt()
    else:
        print("enter a valid choice")
    

