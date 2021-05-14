from socket import * 
s=socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
host='192.168.1.4'
port=7000
s.connect((host,port))
while True:
    s.send((input("Client:")).encode('utf-8'))
    x=s.recv(2048)
    print("Server:",x.decode('utf-8'))
s.close()