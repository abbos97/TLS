import json
import os
from getpass import getpass
from crypto.hashing import hash_password

users_file = os.path.join("server", "users.json")

username = input("Enter new username: ").strip()
password = getpass("Enter password: ").strip() 

hashed = hash_password(password)

if os.path.exists(users_file):
    with open(users_file, "r") as f:
        users = json.load(f)
else:
    users = {}

if username in users:
    print(f"[!] Username '{username}' already exists!")
else:
    users[username] = hashed
    with open(users_file, "w") as f:
        json.dump(users, f, indent=2)
    print(f"[+] User '{username}' added successfully!")
