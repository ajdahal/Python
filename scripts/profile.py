# this program is all about profiling
#python3 -m memory_profiler profile.py --> this is for referencing the module, if used no need to use "from memory_profiler import profile"
'''
 on command line: 
 mprof run script_name/executable 
 mprof plot
 mprof plot --flame
 mprof list    // produces a dat file that lists memory usage 
 mprof clean   // remove all memory recorded files 
# can be used to track child processes as well
'''
#from memory_profiler import profile
from guppy import hpy
h = hpy()
print("heap before program executes",h.heap())


#@profile(precision=4)      //digit are shown upto 4 decimal points 
def hello_func(n):
    lst = [o for o in range(2,n)]
    a = [1] * (10 ** 6)
    for i in range(2,n):
        lst.append(i)
    for i in range(2,n):
        for j in range(2,i-1):
            if (i%j == 0):
                #print("%d is composite" %i)
                lst.remove(i)
                break

#@profile
def main():
    print("Enter a number:")
    n = int(input())
    x = hello_func(n)
    #print("the prime numbers are:" % (*y for y in x))

if __name__ == "__main__": main() 

print("heap after program executes",h.heap())