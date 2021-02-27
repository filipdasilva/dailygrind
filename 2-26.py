#American Standard Code for Information Interchange

print(ord('R'))
print(ord('r'))

#find the numerical represation for a character in Python

#Unicode is millions of possible for characters
#UTF-8 is 1-4 bytes per character
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd = 'GET https://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    mystring = data.decode()
    print(mystring)
    
#take a byte and decode or take a string and code it