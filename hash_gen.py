from crypto.hashing import hash_password

plain_password = "password123"
hashed = hash_password(plain_password)
print(f"Hashed password for '{plain_password}':\n{hashed}")
