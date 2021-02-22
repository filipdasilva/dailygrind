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

HTML language

#hackers use command lines to use protocol, understand whats going on better than creators

QQ = 'What is command line?'
