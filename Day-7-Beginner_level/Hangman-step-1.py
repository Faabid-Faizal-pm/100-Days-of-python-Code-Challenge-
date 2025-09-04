import random

names = ["Giraffe", "Godzilla", "Spiderman", "Superman", "Ironman"]
choice = random.choice(names).lower()  
print(choice)  

guess = input("Guess a letter = ").lower()

for letter in choice:
    if letter==guess:    
        print("Right! ✅")
    else:
        print("Wrong ❌")

