# server side program to listen to logs 
# collector

import socket


#def start_tcp_service():
sock = socket.socket();
host = '192.168.1.65';
port = 6133;
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
    
    
    
    
    
#if __name__ == "__main__":main()


#{
#    "client_map": {
#        "192.168.8.141": {
#            "_enrich_policy": "None", 
#            "charset": "utf_8", 
#            "device_name": "windows", 
#            "normalizer": "None", 
#            "parser": "LineParser", 
#            "routing_policy": "default", 
#            "timezone": "Asia/Kathmandu"
#        }
#}
#        }