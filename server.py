import socket

new_socket = socket.socket()
new_socket.bind(("127.0.0.1", 50), )
new_socket.listen()

print("Server is on!")

name = input("Your name: ")
conn, add = new_socket.accept()

user = (conn.recv(1024)).decode()
print("add", user)
conn.send(name.encode())

while True:
    message = input("Me: ")
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(user, ":", message)