class handling_exception(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        
        
        
def void():
    for i in range (0,4):
        x = 5
        if x:
            print("the value of x is accepted");
            try:
                if (x == ''):
                   print ("good")
                   return 0
            except Exception:
                raise handling_exception("this is handling of exception")
            
            print("this is after return False statement")
        else:
            print("the value of x");
    print("this is after the for range");

print("this is after the function");

def main():
    void()
if __name__ == "__main__":main()