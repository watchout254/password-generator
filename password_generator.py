import random

print("\t\t\tWelcome to 🌍Cole world🌏 password generator")

letters = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v',
           'w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
           'S','T','U','V','W','X','Y','Z',]
numbers = ['0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣']
symbols = ['#️⃣','*️⃣','💲','!','%','&','(',')','^']

letters2 = int(input("How many letters would you like in your password?\n"))
symbols2 = int(input("How many symbols would you like in your password?\n"))
numbers2 = int(input("How many numbers would you like in your password?\n"))

password = ""
for a in range(1,letters2+1):
    bro = random.choice(letters)
    password = password + bro

for b in range(1,symbols2+1):
    mahn = random.choice(symbols)
    password = password + mahn

for c in range(1,numbers2+1):
    mtasis = random.choice(numbers)
    password = password + mtasis

print(password)
print("There you go, Daniel's program got you ma mehn 🤳🏿🤜🏿🤛🏿")
#######More secure password
#random.shuffle(password_in)
#print(password_in)

#password = """"""""""
#for bro in password_in:
 #   password += bro
#print(password)
