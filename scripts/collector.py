
# server side program to listen to logs 
# collector

import socket


def main():
    sock = socket.socket();
    host = '192.168.8.83';
    port = 6135;
    sock.bind((host,port));
    sock.listen(5);
    
    while True:
        newobj,addr = sock.accept();
        print('new object:',newobj);
        print('\n address returned:\n',addr,type(addr));
        print("connection accepted from:" + repr(addr[1]))
        newobj.send("server approved the connection".encode());
        print(repr(addr) + ":" + str(newobj.recv(1026)))
        newobj.close()
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()
    sock.detach()
    
if __name__ == "__main__":main()
