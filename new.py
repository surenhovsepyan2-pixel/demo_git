import random 
import json
from pathlib import Path

FILE = Path(__file__).parent / "passwords.json"

if FILE.exists():
    with open(FILE, "r") as f:
        passwords = json.load(f)
else:
    passwords = []

tver = ["1","2","3","4","5","6","7","8","9","0"]
nshanner = ["=","+","-","!","@","#","$","%","&","*"]
uppercase_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lowercase_letters = list("abcdefghijklmnopqrstuvwxyz")


def password_generator():
    password = []
    for i in range(2):
        password.append(random.choice(tver))
        password.append(random.choice(nshanner))
        password.append(random.choice(uppercase_letters))
        password.append(random.choice(lowercase_letters))

    return "".join(password)
    
password = password_generator()

while password in passwords:
    password = password_generator()

passwords.append(password)

with open(FILE, "w") as f:
    json.dump(passwords, f, indent=4)

print(FILE.absolute())








