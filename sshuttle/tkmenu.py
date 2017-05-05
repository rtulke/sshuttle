#!/usr/bin/python

# Simple Tkinter Menu based on pro-linux.de
# 

import Tkinter
import tkMessageBox
import os
import sys

top = Tkinter.Tk()
try:
   top.tk.call('console','hide')
except Tkinter.TclError:
   pass

HOSTS = {
        's1': ["root@server1", "0.0.0.0/0", "10.42.42.0/24"],
        's2': ["root@server2", "0.0.0.0/0", "10.42.42.0/24"],
        's3': ["user@freeshell.org", "0.0.0.0/0", "10.42.42.0/24"],
        's4': ["user@shell.xshellz.com", "0.0.0.0/0", "10.42.42.0/24"],
        's5': ["root@server5", "0.0.0.0/0", "10.42.42.0/24"],
}

def startsshuttle(id):
    helloCallBack()
    options = HOSTS[id]
    host=options[0]
    targetnet=options[1]
    exclude=options[2]
    command = "/usr/local/bin/sshuttle --dns --pidfile /Users/cm/sshuttle.pid -r %s %s -x %s -D #>/dev/null &" % ( host, targetnet, exclude)
    os.system(command)
    titlestring = "ONLINE %s" % id
    top.title(titlestring)

def s1():
    startsshuttle("s1")

def s2():
    startsshuttle("s2")

def s3():
    startsshuttle("s3")

def s4():
    startsshuttle("s4")

def s5():
    startsshuttle("s5")

def offline():
       os.system("kill `cat /Users/user/sshuttle.pid` >/dev/null 2>/dev/null")
       top.title("offline")

def ende():
    offline()
    sys.exit(0)

A1 = Tkinter.Button(top, text ="Online gehen Server1", command = s1)
A2 = Tkinter.Button(top, text ="Online gehen Server2", command = s2)
A3 = Tkinter.Button(top, text ="Online gehen Server3", command = s3)
A4 = Tkinter.Button(top, text ="Online gehen Server4", command = s4)
A5 = Tkinter.Button(top, text ="Online gehen Server5", command = s5)
B = Tkinter.Button(top, text ="Offline gehen", command = offline)
C = Tkinter.Button(top, text ="Ende", command = ende)

A1.pack()
A2.pack()
A3.pack()
A4.pack()
A5.pack()
B.pack()
C.pack()
top.title("offline")
top.mainloop()
