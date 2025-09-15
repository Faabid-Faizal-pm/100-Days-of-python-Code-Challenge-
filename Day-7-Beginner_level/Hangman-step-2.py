import random

names = ["Giraffe", "Godzilla", "Spiderman", "Superman", "Ironman"]
choice=random.choice(names)

print(choice)
positionholder=""
word_length=len(choice)
for position in range(word_length):
    positionholder += "_"
print(positionholder)

guess=input("Guess the word: ")
display=""
for letter in choice:
    if letter == guess:
        display+=letter
    else:
        display+="_"
print(display)            