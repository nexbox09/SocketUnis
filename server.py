import socket
import sys
import pickle
import time
import random

## Definición de la clase Mensaje ##
class IDP:
    callingPartyNumber =""
    mscAddress = ""
    calledPartyNumber = ""
## Definición de la clase Mensaje ##

class Cue:
    continuar = ""

class RRB:
    o_answer = bool
    o_disc = bool

class ERB:
    o_answer = bool
    o_disc = bool

class ACH:
    tiempo = int

class ACR:
    tiempo = int

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
    # mensaje = IDP()                                         #definir mensaje de clase Mensaje
    # mensaje.callingPartyNumber =  "3506013309"              #recibir parámetros
    # mensaje.mscAddress =  "91655340000512"   
    # mensaje.calledPartyNumber =  "3144582356"  
    # message = pickle.dumps(mensaje)                             #Serializar jerarquía de objetos
    # conn.send(message)                                          
    # print("Sent")
    # print("")
    data = conn.recv(4096)                                      #Recibir mensaje de cliente
    data_variable = pickle.loads(data)                          #Des-serializar el flujo de datos
    print(s_name, ":" ,data_variable.callingPartyNumber,data_variable.mscAddress, data_variable.calledPartyNumber)  #Imprimir los parámetros emoji y text de la variable data_variable
    print("")
    time.sleep(2)
    cue = Cue()
    cue.continuar =  "Continuar"
    cue = pickle.dumps(cue)  
    conn.send(cue)                       
    print("Sent")
    print("")
    time.sleep(2)
    rrb = RRB()
    rrb = pickle.dumps(rrb)  
    conn.send(rrb) 
    print("RRB enviado")
    print("")
    data = conn.recv(4096)
    data_variable = pickle.loads(data)                          #Des-serializar el flujo de datos
    print(s_name, ":" ,data_variable.o_answer)
    print("ERB recibido (o_answer)")
    print("")
    if data_variable.o_answer == True:
        ach = ACH()
        periodo = 6
        ach.tiempo = periodo
        ach = pickle.dumps(ach)
        conn.send(ach) 
        print("ACH( 6 )")
        print("")
        time.sleep(periodo) 
        conn.send(ach) 
        print("ACH( 6 )")
        print("")
        time.sleep(periodo)
        ach = ACH()
        ach.tiempo = 3
        ach = pickle.dumps(ach)
        conn.send(ach) 
        print("ACH( 3 )")
        print("")
        time.sleep(3)

    else:
        exit()

    data = conn.recv(4096)
    data_variable = pickle.loads(data)                          #Des-serializar el flujo de datos
    print(s_name, ":" ,data_variable.o_disc)
    print("ERB recibido (o_disc)")
    print("")

    if data_variable.o_disc == True:
        print("Llamada finalizada")
        exit()


    exit()

    