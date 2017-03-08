#!/usr/bin/python3
# Ejercicio 14.4 Aplicacion redirectora
# Christian Bermejo Guerrero

"""
Simple HTTP Server
Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket
import random

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)

try:
    while True:

        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Let the port be reused if no process is actually using it
        mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Bind to the address corresponding to the main name of the host
        mySocket.bind(('localhost', 1234))
        # Queue a maximum of 5 TCP connection requests
        mySocket.listen(5)

        print ('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print ('HTTP request received:')
        print (recvSocket.recv(1024))
        randomInt = random.randint(1,99999999)
        urlredirect = "http://localhost:1234/" + str(randomInt)
        recvSocket.send(bytes("HTTP/1.1 301 \r\n\r\n" +
                        "<html><meta http-equiv= 'Refresh'" +
                        "content='3;url='" + urlredirect + # <meta http-equiv="Refresh" content="10;url=http://www.dominio.com">
                        "><body<p>Hemos cambiado de direccion. En 3 segundos enlazaras a la nueva pagina: " +
                        urlredirect + ". En caso contrario, pulsa en el " +
                        "<a href=" + urlredirect + ">siguiente enlace.</a></p></body></html>\r\n","utf-8"))
        mySocket.close()

except KeyboardInterrupt:
    print ("\nClosing binded socket")
    mySocket.close()
