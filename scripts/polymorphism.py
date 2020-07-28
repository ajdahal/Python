# same funtion name --> used for different types (data, number of varibales)
 
# Built-in Polymorphism in python

print (len("geeks"))
print (len([1,5,4,2,3]))
print (len({"a": 5, "b":3, "c":7}))

# defined polymorphic functions -- variable overriding 

def add(x,y,z=0):
    return x+y+z;
print("sum of 2 numbers : ",add(4,5))
print("sum of 3 numbers : ",add(3,4,5))

class Nepal():
    print("Nepal1")
    def capital(self):
        print("The capital of Nepal is Kathmandu")
        
    def language(self):
        print("The language of Nepal is Nepali")
    print("Nepal2")
    
class America():
    print("America1")
    def capital(self):
        print("The capital of America is New York")
    
    def language(self):
        print("The language of America is English")
    print("America2")    
    

nep = Nepal();
ame = America();

# Object treated as tuple here

#for x in (nep,ame):
#    x.capital()
#    x.language()
    
# Object treated as Variable (that is passed to a function) here
def func(obj):
    print("func----")
    obj.capital()
    obj.language()
    
func(nep)
func(ame)
    
# re-implementing a method in child class -> overriding method in base class
# This is Method Overriding
print("--------------------------------------------")
class Bird:
    def intro(self):
        print("There are many types of birds")
    def flight(self):
        print("Some birds can fly whereas some cannot")
    
class pigeon(Bird):
    def flight(self):
        print("Pigeons can fly")
        
class ostrich(Bird):
    print(x)
    #def flight(self):
        #print("Ostrich cannot fly")
        
Obj_Bird = Bird()
Obj_Bird.intro()
Obj_Bird.flight()

Obj_pigeon = pigeon()
Obj_pigeon.intro()
Obj_pigeon.flight()


Obj_ostrich = ostrich()
Obj_ostrich.intro()
Obj_ostrich.flight()








