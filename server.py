import socket
import sys
import pickle


## Definición de la clase Mensaje ##
class Mensaje:
    emoji =""
    text = ""
## Definición de la clase Mensaje ##


s = socket.socket()                                                                 #Crear socket
host = socket. gethostname()                                                        #Método para obtener el hostname
print(" server will start on host : ", socket.gethostbyname(socket.gethostname()))  #Mostrar dirección IP del servidor
port = 8080
s.bind((host,port))                                                                 #vincular
name = input(str("Please enter your username: "))                           
print("")
print("Server is waiting for incoming connections")
print("")
s.listen(1)                                                                         #Escuchar las comunicaciones entrantes, 1 significa que solo 1 conexión es aceptada
conn, addr = s.accept()                                                             #initiates a connection with the clien
print("Recieved connection")
print("")
s_name = conn.recv(1024)                                                            #Receive data from the socket. The return value is a bytes object representing the data received. 
s_name = s_name.decode()                                                            #The maximum amount of data to be received at once is specified by bufsize
print(s_name, "has joined the chat room")                                           #Recibir e imprimir nombre de usuario del cliente
conn.send(name.encode())                                                            #Enviar nombre de usuario del servidor                                      

while 1:
    mensaje = Mensaje()                                         #definir mensaje de clase Mensaje
    mensaje.emoji=  input(str("Please enter your emoji: "))     #recibir parámetros
    mensaje.text =  input(str("Please enter your text "))       
    message = pickle.dumps(mensaje)                             #Serializar jerarquía de objetos
    conn.send(message)                                          
    print("Sent")
    print("")
    data = conn.recv(4096)                                      #Recibir mensaje de cliente
    data_variable = pickle.loads(data)                          #Des-serializar el flujo de datos
    print(s_name, ":" ,data_variable.emoji,data_variable.text)  #Imprimir los parámetros emoji y text de la variable data_variable
    print("")

    