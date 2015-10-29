'''
This is a very low level and basic server client project to visualise the basics how server and client interacts each other.
Let's Hands on:
1. Make sure Your Pc is connected to your home network eg router.
2. Make sure the remote device (your android, laptop etc) on which the client is running is connected with the same home network
3. Get Private and Public firewall permissions for Python, the remote device
4. use the ip of the machine where server.py is running
5. now run client.py on remote device
6. holla interact :D
------------------------------------------------------------------------------------------------------------------------
'''

Print "---------------------------------------------------------------------------------------- "
print '                             SERVER.PY                                                   '
Print "---------------------------------------------------------------------------------------- "
from socket import *
import sys

# make a server socket with address_family ipv4 and tcp_stream type
server_socket = socket(AF_INET, SOCK_STREAM)
# take an host (localhost)tuple and bind it with the server socket
server_address = ("", 8081)  # an address + a port (gateway, door whatever we call it)
server_socket.bind(server_address)
print "[+]localhost is up",  server_address
# now listen for incoming connection
server_socket.listen(5)  # can take 5 connections at a time
print "[+]Listening for remote device(s)...........\n"
# A server continuously listens for incoming connections
while True:
    client_socket, client_address = server_socket.accept()
# returns two tuple objects.................
    print "[+]connected with remote LAN device: ", client_address  # receive data string
                                                                  #  sent via client connection
    while True:
        received_data = client_socket.recv(4000)
        if not received_data:
            break
        print received_data
        send_data = raw_input(">>> ")
        client_socket.sendall("[Server:] %s " % send_data)

client_socket.close()
server_socket.close()
print "[-] connection closed !!\n"
sys.exit()
# Now run Client.py on a remote device on the same network 
Print "---------------------------------------------------------------------------------------- "
print '                             CLIENT.PY (ON YOUR ANDROID OR LAPTOP ETC)                                                   '
Print "---------------------------------------------------------------------------------------- "
from socket import *
import sys
# creat a client socket
client_socket = socket(AF_INET, SOCK_STREAM)
print "socket created\n\r"
#host = raw_input("input host name/ ip: ")
host = 'localhost' # use the ip of the machine where server is running
port = 8081
# try to get host/ remote ip
try:
    remote_ip = gethostbyname(host)
except gaierror:
    print "couldn't resolve the host/ip"
    sys.exit()
# try to connect the socket with the localhost/ server 
try:
    client_socket.connect((host, port))
except error as msg:
    print "[-]failed\n\rError Code: %s\n\rCause: %s" %(msg[0], msg[1])
    sys.exit()
print "connected with "+ host+" remote ip: "+remote_ip+"at port ", port
# now chat with the server 
while True:
    msg = raw_input(">>> ")
    if msg == '':
        break
    client_socket.sendall("[Client:] %s " % msg)
    # receive the reply from server
    response_data = client_socket.recv(100000)
    print response_data
client_socket.close()
sys.exit()





