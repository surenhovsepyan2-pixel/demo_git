import random 
import json
from pathlib import Path

FILE = Path("passwords.json")

if FILE.exists():
    with open(FILE, "r") as f:
        passwords = json.load(f)
else:
    passwords = []

tver = [1,2,3,4,5,6,7,8,9,0]
nshanner = ["=","+","-","!","@","#","$","%","&","*"]
uppercase_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowercase_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


def password_generator():
    password = []
    for i in range(2):
        password.append(random.choice(tver))
        password.append(random.choice(nshanner))
        password.append(random.choice(uppercase_letters))
        password.append(random.choice(lowercase_letters))

    return password
password = password_generator()

while password in passwords:
    password_generator()

passwords.append(password)

with open(FILE, "w") as f:
    json.dump(passwords, f, indent=4)







