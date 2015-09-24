__author__ = 'streamsadmin'


import socket
import sys
s = socket.socket()
s.bind(("localhost",23145))
s.listen(10) # Acepta hasta 10 conexiones entrantes.

while True:
    sc, address = s.accept()

    print(address)
    i=1
    # f = open('file_'+ str(i)+".csv",'wb') #open in binary
    i=i+1
    while (True):
    # recibimos y escribimos en el fichero
        l = sc.recv(1024)
        while (l):
                #f.write(l)
                
                print(l)
                l = sc.recv(1024)
    f.close()


    sc.close()

s.close()


