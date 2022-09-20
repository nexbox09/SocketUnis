import socket
import sys
import pickle



class Mensaje:
    emoji =""
    text = ""

s = socket.socket()
host = socket. gethostname()
print(" server will start on host : ", socket.gethostbyname(socket.gethostname()))
port = 8080
s.bind((host,port))
name = input(str("Please enter your username: "))
print("")
print("Server is waiting for incoming connections")
print("")
s.listen(1)
conn, addr = s.accept()
print("Recieved connection")
print("")
s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat room")
conn.send(name.encode())

while 1:
    mensaje = Mensaje()
    mensaje.emoji=  input(str("Please enter your emoji: "))
    mensaje.text =  input(str("Please enter your text "))
    message = pickle.dumps(mensaje)
    conn.send(message)
    print("Sent")
    print("")
    data = conn.recv(4096)
    data_variable = pickle.loads(data)
    print(s_name, ":" ,data_variable.emoji,data_variable.text)
    print("")

    