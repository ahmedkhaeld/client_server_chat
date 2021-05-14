from socket import * 
try:
    s=socket(AF_INET,SOCK_STREAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    host='192.168.1.4'
    port=7000
    s.bind((host,port))
    s.listen(5)
    c,ad=s.accept()
    print("Connection from",ad[0])
    while True:
        x=c.recv(2048)
        print("Client:",x.decode('utf-8'))
        c.send((input("Server:")).encode('utf-8'))
    s.close()
except error as e:
    print(e)
except KeyboardInterrupt :
    print("OK") 