import random
lr=['a','b','c','d','e','f','g','h','i','j','k']
num=['1','2','3','4','5','6','7','8','9']
symb=['!','@','#','%','&']
tot=int(input("enter the number of character in password"))
lr_l=random.randint(0,tot)
lr_n=random.randint(0,tot-lr_l)
lr_s=random.randint(0,tot-(lr_l+lr_n))
password=""
password_list=[]
for i in range(0,lr_l):
    password_list.append(random.choice(lr))
for i in range(0,lr_n):
    password_list.append(random.choice(num))
for i in range(0,lr_s):
    password_list.append(random.choice(symb))
random.shuffle(password_list)
for i in password_list:
    password+=i  
print(f"the password is:{password}")
