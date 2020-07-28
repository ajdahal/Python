# Client side program to send logs to server

import socket            #python module that calls os socket API

def main():
    sock = socket.socket();  #socket object is returned whose methods implement various socket system calls
    host = '192.168.1.65';
    port = 6133;
    sock.connect((host,port)); #connects to tcp service running on this ip and port
    print (sock.recv(1024)); #max amount of data received at once
    inut = input('type your message to server::');
    sock.send(inut.encode());  #send data to socket_which is connected to remote socket
    print("the message has been sent succesfully!");
    sock.close();
if __name__ == "__main__":main()
