
import socket

# AF_INET address format default value
# SOCK_STREAM sequential reliable two way connection based byte streams
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to an ip address and port number evven URL can be used in place of ipaddress
client.connect(('0.0.0.0', 8080))

# send some data towards server
client.send("I am CLIENT \n".encode())

# receive number of bytes specified as input
from_server = client.recv(4096).decode()

# Closing socket connecction if data has to be received or send from same socket 
# use send or receive multiple times without closing
client.close()

print(from_server)