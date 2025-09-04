import random 
print("Welcome to py password generator!")

letter = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
          'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
          'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

symbol = ('!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '=', '+', ';', ':', '<', '>', ',', '.', '?', '/', '|', '~')

number = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

nr_letter = int(input("Enter how many letters would you like in your password = "))
nr_symbol = int(input("Enter how many symbols would you like in your password = "))
nr_number = int(input("Enter how many numbers would you like in your password = "))

password_list = []

for char in range(nr_letter):
    password_list.append(random.choice(letter))

for char in range(nr_symbol):
    password_list.append(random.choice(symbol))

for char in range(nr_number):
    password_list.append(random.choice(number))

random.shuffle(password_list)

password = ''.join(password_list)

print(f"Your password is = {password}")
