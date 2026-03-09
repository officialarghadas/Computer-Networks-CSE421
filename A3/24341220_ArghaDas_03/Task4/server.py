# Task04

import socket

HEADER=16
PORT=5176
SERVER=socket.gethostbyname(socket.gethostname())

#bind the address
ADDR=(SERVER, PORT) #binding IP and port
FORMAT="utf8"
DISCONNECT_MSG="Task End."

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # (ipv4, TCP)

server.bind(ADDR)


server.listen()
print("server is Listening")

conn, addr= server.accept()

connected=True

while connected: #client is connected
    msg_length=conn.recv(HEADER).decode(FORMAT)
    if msg_length:
        msg_length= int(msg_length)
        msg=conn.recv(msg_length).decode(FORMAT) # how many length of messages
        if msg==DISCONNECT_MSG:
            connected=False
            print("Goodbye")
            conn.send(DISCONNECT_MSG.encode(FORMAT))
        else:
            hours = float(msg)
            if hours <= 40:
                salary = hours * 200
            else:
                salary = 8000 + (hours - 40) * 300
            conn.send(f"Salary: Tk {salary}".encode(FORMAT))
conn.close()
