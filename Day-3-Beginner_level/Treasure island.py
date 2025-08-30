print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to the treasure is island your mission to find tressure.")

choice_1= input("which direction would you like to go? type 'left' or 'right'\n")

if choice_1 == 'left':
    choice_2 = input('You have successfully crossed the road n. '\
    'now you have to cross the shore type "swim" if you want to swim '\
    'or type "wait" if you want to wait for boat\n')
    if choice_2 == 'wait':
        choice_3= input('you have succussfully crossed the shore.' 
        ' now you have 3 choice"red","yellow"or"blue".only' 
        ' one can save you from danger.\n')
        if choice_3 == 'red':
            print("You have been eaten by a gorilla.better luck next time.\n GMAE OVER")
        elif choice_3 =='yellow':
            print("You have fallen into Crocodile lake.Better luck next time.\n GAME OVER")
        elif choice_3 == 'blue':
            print("You have found the Tresure.Now you have become the King of the  Pirete\n Congradtulation you WON \n Hurrai!!")       
        else:
            print("Invalid Door.GAME OVER")
    else:
        print("invalid you have drawn to river.\n GAME OVER")    


else:
    print("invalid you took wrong direction.\n GAME OVER")