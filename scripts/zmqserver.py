# ZMQ
## ZMQ.REQ can connect to many servers
import zmq
import json
import time
#
def start_service():
    context = zmq.Context()    #initialize zmq context (used to create zmq sockets)
    socket = context.socket(zmq.PAIR); #socket subclass,PAIR is socket type of ZMQ
    port = 5573;
    socket.bind("tcp://127.0.0.1:%s " % port);
    
    while True:
        socket.send_string("server message to client");
        message = socket.recv()
        col_ts = time.time();
        print("Received data now")
        print("Message is:", message.decode("utf-8"),col_ts)
        if message.decode("utf-8") == "close":
            print("closing it now")
#            socket.unbind("tcp://127.0.0.1:%s " % port);
            socket.close()
            context.term()
            break;
        else:
            print("Next Iteration")  
              

def write_json():
 jon =   {
    'client_map': {
        '192.168.8.141': {
            '_enrich_policy': 'None', 
            'charset': 'utf_8', 
            'device_name': 'linux', 
            'normalizer': 'None', 
            'parser': 'LineParser', 
            'routing_policy': 'default', 
            'timezone': 'Asia/Kathmandu'
      }
    }
   }
        
 with open('config.json','w') as fp:
     json.dump(jon,fp)
     
def main():
    start_service();
    write_json();
    
    
if __name__ == "__main__":main()