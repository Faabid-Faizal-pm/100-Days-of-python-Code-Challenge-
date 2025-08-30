print("Welcome to the rollercoster")
height= int(input("what is your height?\n"))
age= int(input("what is your age?\n"))
wants_photo= str(input("would you want photo?\n"))

bill=0

if height>120:
    print("you can ride the rollercoster")
    if age <= 12:
        bill += 30
        print("kids price is Rs.30 added")
    elif age <= 18:
        bill += 50
        print("youth price is RS.50 added")
    else:
        bill +=100
        print("Adult price is Rs.100 added")
    if wants_photo == 'yes':
        bill+=10
        print("photo price is Rs.10 is added")
    
    print(f"your total price is : Rs.{bill}")


else:
    print("you can't ride rollercoster")    