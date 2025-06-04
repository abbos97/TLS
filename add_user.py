import json
import os
from getpass import getpass
from crypto.hashing import hash_password

# Fayl yo'li
users_file = os.path.join("server", "users.json")

# Foydalanuvchi kiritish
username = input("Enter new username: ").strip()
password = getpass("Enter password: ").strip()  # parol ko‘rinmaydi

# Hashlash
hashed = hash_password(password)

# users.json mavjud bo‘lsa – yuklaymiz, bo‘lmasa yangi dict
if os.path.exists(users_file):
    with open(users_file, "r") as f:
        users = json.load(f)
else:
    users = {}

# Foydalanuvchi mavjudligini tekshir
if username in users:
    print(f"[!] Username '{username}' already exists!")
else:
    users[username] = hashed
    with open(users_file, "w") as f:
        json.dump(users, f, indent=2)
    print(f"[+] User '{username}' added successfully!")
