 

import sys
import traceback
import inspect
import cgitb;cgitb.enable()
from pygments import highlight
from pygments.lexers import PythonTracebackLexer
from pygments.formatters import TerminalFormatter
#import hunter
#hunter.trace(module='posixpath', action=hunter.VarsPrinter('et'))

# exception_type, exception_value,traceback -> et,ev,tb
# pip3 install pygments --use
# print(dir(lexers))
# print(dir(formatters))

def custom_traceback(et,ev,tb):
   trace = ''.join(traceback.format_exception(et,ev,tb))
   print("this is custom traceback")
  # print(et)  //zero division error //exception_type
  # print(ev)    //division by zero  //event_value
  # print(tb)    //traceback object at 0x1015cc410 //traceback 
  # lexer-> splits source into tokens with token type that... 
  # ...determines what text represents semantically ...
  # formatter-> takes in token stream and writes it to an output...
  # ..file in format specified here terminalformatter
   print(highlight(code=trace, lexer=PythonTracebackLexer(), formatter=TerminalFormatter()))

sys.excepthook = custom_traceback


def div(a,b):
    return (a/b)

def foo(a,b):
    return div(a,b)

# print(foo(1,1))
try:
    print(foo(1,0))
except:
    et, ev, tb = sys.exc_info()
    #print(" ".join(traceback.format_exception(et,ev,tb)))
    frame_records = inspect.getinnerframes(tb)
    #print("\n","frame_records:",frame_records)
    frame, fname,lnum, func, lines, index = frame_records[1]
    args, varargs,varkw,local_vars = inspect.getargvalues(frame)
    #print("\n","args,varargs, varkw, local_vars:",args,varargs, varkw, local_vars)
    #print("\n","lines:",lines)
    def reader():
        return lines[index]
    
    objects = cgitb.scanvars(reader, frame, local_vars)
    #print("\n","Objects:",objects)

# Use case of traceback:
# hyperlink (link that takes us to place in code where error occured)
# UI apps (app must run event if exception occurs) -- use traceback to silently log exception somewhere
# Interactive debugging -> inspect every state of program
# PEP 3134, Chain exceptions
# https://pypi.org/project/ptb/

'''
try:
    do_stuff()
except Exception:
    print(traceback.format_exc())
   '''
#------------------------------------------------------------------
'''

pdb

// python 3.7 or later has another debugger on top of pdb (debugger), which makes debugging easy
python3 -m pdb /opt/immune/installed/webserver/applications/DashboardTabs/controller.py
python -m pdb /opt/immune/installed/webserver/applications/DashboardTabs/controller.py arg1 arg2
pdb /opt/immune/installed/webserver/applications/DashboardTabs/controller.py


p -- print
pp -- pretty print ( dictionaries )
n -- execute the statement and go to next line in same function/Module
s -- execute the statement and go to next line even if next line is call the another function

ll -- list the whole source code for the current function or frame
l  -- show shorter snippet of code 

breakpoints:

b -- set breakpoint 
b(reak) [ ([filename:]lineno | function) [, condition] ]
(pdb) b /opt/immune/installed/webserver/applications/DashboardTabs/controller.py:1475
(Pdb) b /opt/immune/installed/webserver/applications/DashboardTabs/controller.py:1518
(Pdb) c  -- continue execution till breakpoint is found
(Pdb) b  -- show breakpoints
(Pdb) disable 1  -- disables breakpoint 1
(Pdb) enable 1   -- enables breakpoint 1
(Pdb) cl /opt/immune/installed/webserver/applications/DashboardTabs/controller.py:1475 
// -- clears the breakpoint set
(Pdp) b util.get_path, not filename.startswith('/') -- Example of breakpoint set when certain condition isn't met
after setting break point, type in "c" to continue execution, the program stops when expression evaluates to true
(Pdb) a -- use "a" to print argument list of the current function
unt(until): continue execution until a line with a number greater or equal to that is reached
Stop when the current frame returns
unt(until) is superset of n (next) | breakpoint: line number given
--> Execute and step over 
unt(il)[lineno]  -- specify line number to execute code till that point
(Pdb) unt[20] -- hit enter (a loop is being run that follows the next step when you hit enter)
(Pdb) display li_version -- display value of variables (useful in loops after setting breakpoint at the end of loop)
(Pdb) display text 
(Pdb) w -- to print stack trace in a large program to find out where the function under evaluation is called from
// Current Frame indicated by >, other frames by ->
// Where is Current Frame set? -> the function/place where "pdb.set_trace()" is set
u  u(p)[count], d d(own)[count] -- move a frame up or down
--> Why move? -- so that you can move and print local varibles in different functions in different files 

Frame: DataStructure that python creates when a function is called and deletes when it returns 
Stack: Ordered list of frames or function calls at any point in time

h pdb -- pdb docs
h     -- list all available commands 


logging:
use log.debug instead of print

Trace:
python -m ModuleName --trace PythonFileName
-t/--trace: Display lines as they are executed 

python -mtrace --trace TraceBack.py -- this shows all the lines that are executed when the file is run with python
python -mtrace --trace TraceBack.py| egrep 'div' -- "div" is function here

pip install hunter

try:
    code that fails
except:
    import pdb
    pdb.pm()       //post_mortem() of code that fails

python -m pdb script.py

pip install remote_pdb
from remote_pdb import set_trace
set_trace()

from remote_pdb import RemotePdb
RemotePdb(host="10.45.9.141", port=44444).set_trace()

strace -p 12345 or strace -p 12355 &> file_1 
ltrace -- like strace but with library calls

lsof -p 12345

htop:
hightlight a process and type:
s -- for sytem call trace (strace)
L -- for library call trace (ltrace)
l -- lsof


iotop,iftop,htop,iostat,vmstat --- use dstat

dstat: very very useful 

dstat --cpu --io --mem --net --load --fs --vm --disk-util --disk-tps --freespace --swap --top-io --top-bio-adv

gdb:
gdb -p 12345
bt -- backtrace

segfaults -- program tries to read or write to memory location that doesn't exist
import faulthandler
faulthandler.enable()
faulthandler.register(signal.SIGUSR2, all_threads=True)

kill -USR 12345  -- gives stacktrace for all threads on the process stderr

Memory Leaks:

import objgraph
objgraph.show_most_common_types()
objs = objgraph.by_type("Request")[:15]
objgraph.show_backrefs(objs, max_depth=15, highlight=lambda v: v in objs, filename="/tmp/graph.png")

Memory Usage:

pytracemalloc:
useful for finding memory allocation per file and line ....

gdb:

gdb python process_id
bt      -- show backtrace
thread apply all backtrace      -- show backtrace of all threads
info threads            -- get information on threads 

python -c "import ctypes; ctypes.string_at(0xffffffff)"  -- trying to access memeory location that can't be accessed (freed block of memory, reading and writing operation in read only location)
Segmentation fault (core dumped) -- indicates memory corruption 

gdb --args python
run
execute the python code under gdb to inspect the bug in it

if the program detects segmentation fault it will stop with the error such as:
    Program received signal SIGSEGV, Segmentation fault.
strlen () at ../sysdeps/x86_64/strlen.S:106
106     ../sysdeps/x86_64/strlen.S: No such file or directory.

bt -- Now use backtrace to see where the execution ended

we can enrich the information obtained importing libparsing libray in python and reloading it
python objects can be pretty printed i.e. from a number we can obtain the function name, object_type,...
https://fedoraproject.org/wiki/Features/EasierPythonDebugging
https://blog.ionelmc.ro/2013/06/05/python-debugging-tools/

frame 9 -- print frame 9

'''


''' 
find if a process is running or hung 
cat /proc/4965/task/*/status  
'''