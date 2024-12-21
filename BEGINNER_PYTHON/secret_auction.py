bidders={}
winners={}
stop=False
top_value=0
name=""

while stop != True:
    name=str(input("enter your name : "))
    bid=int(input("enter your bid : "))
    bidders[bid]=name
    choice=str(input("enter 'yes' if you have other bidders else 'no' :  "))
    if choice == 'yes' :
        stop=False
        print("\n"*30)
    elif choice == 'no' :
        stop=True 
    else:
        print("enter valid choice")
for i in bidders:
    if top_value < i :
        top_value=i
        name=bidders[i]
        
print(f"the top bid is :{top_value} from {name}")    