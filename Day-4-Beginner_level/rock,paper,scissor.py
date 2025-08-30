import random

rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

paper = ('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')

scissor = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

game = [rock, paper, scissor]

print("Welcome to Rock, Paper, Scissors!")

user = int(input("For Rock type 0, for Paper type 1, and for Scissors type 2: "))

if user >= 0 and user <= 2:
    print("You chose:")
    print(game[user])

computer = random.randint(0, 2)
print("Computer chose:")
print(game[computer])

if user >= 3 or user < 0:
    print("You chose invalid, you lose")

elif user == 0 and computer == 2:
    print("You win!")

elif user == 2 and computer == 0:
    print("You lose!")

elif user > computer:
    print("You win")

elif computer > user:
    print("You lose")

elif user == computer:
    print("It's a draw")

