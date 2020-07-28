# Inheritance 

# class Person(object): == class Person: (In python 3 - same)

# In python 2____
# class Person(object) - creates class with object as parent
# class Person: - creates class without object parent
# Built in basic class is -- Object, class Person(object) inherits from object 

class person():
    
    def __init__(self,name,citizenship_number):
        self.name = name;
        self.citizenship_number = citizenship_number;
        self.string_t = "Hello from base"
        
    
    def display(self):
        print(self.name)
        print(self.citizenship_number)

class employee():
    
    def __init__(self,employee_id,name,citizenship_number):
        self.employee_id = employee_id;
        print("this is printed when __init__ is called")
        
        # Initializing the variables name and citizenship_number
        person.__init__(self,name ,citizenship_number)
    
    def display(self):
        print(self.name)
        print(self.citizenship_number)
        print("Employee_id is: ",self.employee_id)
        print(self.string_t)
        
#pobj = person("arjun",456)
eobj = employee(67,"ramananda",45)
eobj.display();
print (eobj.name)

print("---------------------------------------------")
class Base1:
    def __init__(self):
        self.str1 = "Base_1"
        print("Base_1")
    
class Base2:
    def __init__(self):
        self.str2 = "Base_2"
        print("Base_2")

class Derived(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")
    
    def PrintStrs(self):
        print(self.str1, self.str2)
    
        
der = Derived()
der.PrintStrs()

print("-------------------------------------------")

class grandfather:
    def __init__(self,name):
        self.name = name # this is public variable 
        self.__pri = "private variable from base class"
        self._protected = "protected variable from base class"
    
    def getName(self):
        return self.name;
    
    def __prifun(self):
        return self.__pri;

class father(grandfather):
    def __init__(self,name,age):
        self.age = age
        grandfather.__init__(self,name)
    
    def getAge(self):
        return self.age;
    
class child(father):
    def __init__(self,name,age,address):
        self.address = address
        father.__init__(self,name,age)
    
    def getAddress(self):
        return self.address;

chi = child("Arjun", 23, "Chandranighapur")
print(chi.name, chi.age, chi.address)
#print(chi.__pri)   // Gives us Error -- accessing private variable
#print(chi.__prifun) // Accessing private function
print(chi._protected)
    
print("-------------------------------------------")

class A:
    def __init__(self,v):
        self.v = 2 * v;
        print (self.v);
        return v;
     
class B:
    def __init__(self,c):
        print("in B_init :", c)
        print(super(B,self).__init__())
        print("in B_init_2:", c)
    
    def get_value(self):
        print("this is in get_value")
        print(A.__init__(self,c))

b = B(3)




