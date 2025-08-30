print("Welcome to the pizza delelivery")

size= input("what is the size would you like to order?S,M or L \n").lower()
peperoni=input("would you like to add peperoni? Rs-10 type'yes'\n")
extra_cheez=input("would you like to add extra cheez? Rs-10 type'yes'\n")
bill=0
if size == 's':
    bill += 150
    print("you chose Small it cost Rs.150")
    if peperoni == 'yes':
        bill+=10
        print("peperoni is added of Rs.10")
    if extra_cheez== 'yes':
        bill +=10
        print("extra cheeze is added of Rs.10")    

elif size == 'm':
    bill += 200
    print("you chose medium it cost Rs.200")
    if peperoni == 'yes':
        bill+=10
        print("peperoni is added of Rs.10")
    if extra_cheez== 'yes':
        bill +=10
        print("extra cheeze is added of Rs.10") 

elif size == 'l':
    bill += 250
    print("you chose Large it cost Rs.250")  
    if peperoni == 'yes':
        bill+=10
        print("peperoni is added of Rs.10")
    if extra_cheez== 'yes':
        bill +=10
        print("extra cheeze is added of Rs.10")   

else:
    print("Ivalid size")

print(f"your total bill is {bill}")

