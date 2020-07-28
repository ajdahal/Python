## This is section where thing are learned in python in great details.

p = (4,5);
print(type(p));
print("\n")
x,y=p;            ##unpacking
print(x,y);
data = ["x",10,(2009,6,3)];
name,age_now,data_of_birth=data;
print(name,age_now,data_of_birth);

## Anything iterable in python list, tuple, string, files, iterators, generators can be unpacked 
## If you don't want some values to be unpacked, use the following syntax 
print("\n")
ign,age_now,_=data;
print(age_now); ##here i have printed "_" but it is not used in programming world
print("the ign is used here and _ as well :", ign, _); # _ or ign can be used 
print(type(_));

## unpacking Elemetns from Iterables of Arbitary length -- using star expressions 
#The unpacked list of elements captured using star expression can be anywhere -- at the beginning, middle or end of the iterable
def avg(grades):
    return (sum(grades)/len(grades));

grades = (90, 91, 89, 56, 98,67, 43);

def sum(grades):
    head,*tail = grades;
#    print("the tail in sum(grades) function is:", tail)
    return head + sum(tail) if tail else head; #here, if ..else handles exception --
 
print("the sum of all the grades is:", sum(grades));
    
first, *middle, last = grades
print(*middle, avg(middle))
print("Type of middle elements are:", type(middle))
print("the first and last of the elements along with their types are:", first, last, type(first), type(last))

#another use case of star operator 

records = [('foo',1,2),('foo',3,4),('bar','hello')]

def foo(x,y): #or def foo(*args): print('foo',*args)
    print('foo',x,y);

def bar(x):
    print('bar',x);

for tag, *args in records:
    if tag == 'foo':
        foo(*args);
    elif tag == 'bar':
        bar(*args);    


from collections import deque
#deque -- list-like container with fast appends and pops on either end
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history) # //deque has 
    for line in lines:
        if pattern in line:
            yield line, previous_lines   #
        previous_lines.append(line)

def keep_last_n_itmes():
    with open("test.txt") as f:
        for line, prevlines in search(f,'python',3):
            for pline in prevlines:
                print(pline, end='')
            print(line,end='')
            print('-'*20)

keep_last_n_itmes();
        
    
