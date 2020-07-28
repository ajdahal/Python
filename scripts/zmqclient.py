# ZMQ
import zmq
#import time

def main():
    context = zmq.Context()    #initialize zmq context (used to create zmq sockets)
    socket = context.socket(zmq.PAIR);
    port = 5573;
    socket.connect("tcp://127.0.0.1:%s" % port);
    
    while True:
        message = socket.recv()
        print (message.decode("utf-8"))
        inp = input("type your message to server:");
        socket.send_string(inp);
        print("message has been send succesfully")

if __name__ == "__main__":main()
