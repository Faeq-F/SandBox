'''
from tkinter import *
import tkinter as tkinter
import tkinter as tk
import time
import webbrowser
def move_window(event):
    top.geometry('+{0}+{1}'.format(event.x_root, event.y_root))
root = tkinter.Tk()
top = tkinter.Toplevel(root)
top.overrideredirect(1) #removes border but undesirably from taskbar too (usually for non toplevel windows)
toolbar = Frame(top, bd=1, relief=RAISED,bg = 'black')
toolbar.bind('<B1-Motion>', move_window)
root.attributes("-alpha",0.0)
root.mainloop()
'''
try:
    from tkinter import *
except ImportError:
    from Tkinter import *


class NewRoot(Tk):    
    def __init__(self):
        Tk.__init__(self)
        self.attributes('-alpha', 0.0)

class MyMain(Toplevel):
    def __init__(self, master):
        Toplevel.__init__(self, master)
        self.overrideredirect(1)
        def move_window(event):
            self.geometry('+{0}+{1}'.format(event.x_root, event.y_root))
        self.bind('<B1-Motion>', move_window)
        self.attributes('-topmost', 1)
        self.geometry('+100+100')
        self.bind('<ButtonRelease-3>', self.on_close)  #right-click to get out

    def on_close(self, event):
        self.master.destroy()


if __name__ == '__main__':

    root = NewRoot()
    root.lower()
    root.iconify()
    root.title('Program')
    
    app = MyMain(root)
    app.mainloop()
