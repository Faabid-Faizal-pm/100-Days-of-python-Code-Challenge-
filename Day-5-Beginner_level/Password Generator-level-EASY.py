import random
print("Welcome to py password Generator!")

letters=('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
          'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
)
symbols=('!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '=', '+',  ';', ':', '"', "'", '<', '>', ',', '.', '?', '/', '|','~')
number=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')


nr_letters=int(input("enter how many letters you want in your password ="))
nr_symbols=int(input("enter how many symbols would you like to be in you password ="))
nr_number=int(input("enter how many symbols would you like to be in you password ="))


password=''
for char in range(0,nr_letters):
    password += random.choice(letters)

for char in range(0,nr_symbols):
    password += random.choice(symbols)

for char in range(0,nr_number):
     password += random.choice(number)

print(f"Your password is ={password}")
              
