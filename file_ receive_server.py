import socket
import base64

def copy(cp_str,extens):
    cp_enc = cp_str
    write = open("copy."+extens,"wb")
    cp_f = base64.b64decode(cp_enc)
    write.write(cp_f)
    write.close()

host = "10.10.6.42"#"192.168.0.254"
port = 1270

serversock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
serversock.bind((host,port))
serversock.listen(10)

print ("whaiting for connections...")
clientsock, client_address = serversock.accept()

rcvmsg = clientsock.recv(1024)
if rcvmsg=="":
    clientsock.close()
extens = rcvmsg
clientsock.sendall("okay, file extension please".encode())
rcvmsg = clientsock.recv(1024)
print("Capture split length ->"+rcvmsg.decode())
rcvmsg = int(rcvmsg.decode())
clientsock.sendall("start".encode())

cp_str = "".encode()
for i in range(rcvmsg):
    cp_str += clientsock.recv(1024)

copy(cp_str,extens)
clientsock.close()