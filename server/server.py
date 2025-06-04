import sys, os
import ssl, socket, json

# --- 🔧 crypto modulini import qilish uchun yo‘l qo‘shish
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from crypto.hashing import verify_password
from crypto.encryption import decrypt_message

# --- 📁 Fayl yo‘llari
base_dir = os.path.dirname(__file__)
users_file = os.path.join(base_dir, "users.json")
cert_file = os.path.join(base_dir, "server.crt")
key_file = os.path.join(base_dir, "server.key")

# --- 🔐 TLS sozlamasi
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=cert_file, keyfile=key_file)

# --- 👥 Foydalanuvchilarni yuklash
with open(users_file, "r") as f:
    users = json.load(f)

# --- 🧠 Mijoz bilan ishlash funksiyasi
def handle_client(conn):
    try:
        conn.send(b"Username: ")
        username = conn.recv(1024).decode().strip()
        conn.send(b"Password: ")
        password = conn.recv(1024).decode().strip()

        print(f"[>] Login attempt from {username}")

        if username in users and verify_password(password, users[username]):
            conn.send(b"Authenticated! Send encrypted message:\n")
            enc_msg = conn.recv(2048)

            try:
                dec = decrypt_message(enc_msg)
                print(f"[✓] Decrypted message from {username}: {dec}")
                conn.send(b"Decrypted: " + dec.encode())
            except Exception as e:
                print(f"[X] Decryption error for {username}: {e}")
                conn.send(b"Decryption error: " + str(e).encode())
        else:
            print(f"[X] Authentication failed for {username}")
            conn.send(b"403 - Unauthorized: Invalid username or password")
    except Exception as e:
        print(f"[!!] Server error: {e}")
    finally:
        conn.close()


# --- 🚀 TLS serverni ishga tushirish
with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind(('localhost', 8443))
    sock.listen(5)
    with context.wrap_socket(sock, server_side=True) as ssock:
        print("[+] TLS server listening on port 8443...")
        while True:
            conn, addr = ssock.accept()
            print(f"[+] Client connected: {addr}")
            handle_client(conn)


