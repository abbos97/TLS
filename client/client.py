import ssl, socket
from crypto.encryption import encrypt_message

context = ssl._create_unverified_context()  

with socket.create_connection(('127.0.0.1', 8443)) as sock:
    with context.wrap_socket(sock, server_hostname='localhost') as ssock:

        print(ssock.recv(1024).decode(), end='')
        ssock.send(input().encode())

        print(ssock.recv(1024).decode(), end='')
        ssock.send(input().encode())
        msg = input("Message to encrypt and send: ")
        enc = encrypt_message(msg)  
        ssock.send(enc)


        response = ssock.recv(1024).decode()
        print(response)

        if "403" in response:
            print("❌ You are not authorized or not registered.")
            ssock.close()
            exit()