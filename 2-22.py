TCP = 'Transport Contol Protocol'

#stack connections

#application -> transport -> transport -> application

#socket - connecting point from one process to another, such as internet

import socket
#creates socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#assigns socket
mysock.connect( ('data.pr4e.org', 80) )

HTTP = 'Hypertext Transfer Protocol'

protocol = 'http://'
host = 'www.dr-chuck.com'
document = '/pagel.htm'

#whenever the user clicks anchor tag with href = value, the browser makes a connection to the web server an issues a 'Get' request - to 'Get' the content of the page at the specified URL
#brings document to user

hyperlink = 'request Get and response second page'

#standards are RFC - request for comments

# $ telnet www.dr-chuck.com 80

#HTML language

#hackers use command lines to use protocol, understand whats going on better than creators

QQ = 'What is command line?'


print('An HTTP Request in Python')
print('this is literally an entire web browser written in 10 lines of python')

import socket
thesock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#thesock.connect(('data.pr4e.org',80))
#cmd = 'GET https://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()


#my attempt at doing this with walmart (doesnt work) request reJeCTed
#thesock.connect(('walmart.com',80))
#cmd = 'GET https://walmart.com/.txt HTTP/1.0\n\n'.encode()

#400 bad request again - this is the page im learning from what am i doing wrong?
thesock.connect(('freecodecamp.org',80))
cmd = 'GET https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/networking-write-a-web-browser HTTP/1.0\n\n'.encode()



thesock.send(cmd)

while True:
    data = thesock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

#DOes this just pull shit straight from any website? Like walmart.com??

#why was this request rejected??

#also got access to anaconda on my work laptop, jupyterlabs here we go - very applicable to my day to day

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.connect(('data.pr4e.org', 80))
#cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()


#keeps getting rejected
#mysock.connect(('walmart.com', 80))
#cmd = 'GET https://walmart.com/.txt HTTP/1.0\r\n\r\n'.encode()

#also doesnt work
thesock.connect(('freecodecamp.org',80))
cmd = 'GET https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/networking-write-a-web-browser HTTP/1.0\n\n'.encode()

mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()