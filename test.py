import tkinter as tk
from tkinter import ttk
try:#                                                                                           |
    from tkinter import *#                                                                      |
#                                                                                               |
    #makes sure that no matter what update you are on, the program will still try to work       |
    import tkinter as tk#                                                                       |
#                                                                                               |
#                                                                                               |
except ImportError: #                                                                           |
#                                                                                               |
    from Tkinter import *#                                                                      |
#                                                                                               |
    #used if on a lower update eventhough being on the latest version of python is advised      |
    import Tkinter as tk#
#getting the scrollable frame with buttons to work with .grid
"""
root = Tk()
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

def frameText(frame, **kw):
    ysb = Scrollbar(frame)
    text = Canvas(frame, **kw)
    frame_container=Frame(frame)
    import functools
    canvas_container=Canvas(frame_container, height=100)
    frame2=Frame(canvas_container)
    canvas_container.create_window((0,0),window=frame2,anchor='nw')
    canvas_container.bind_all("<MouseWheel>")
    def _on_mousewheel(self, event):
        canvas_container.yview_scroll(-1*(event.delta/120), "units")
    def func(name):
        print (name)
    mylist = ['item1','item2','item3','item4','item5','item6','item7','item8','item9']
    for item in mylist:
        button = Button(frame2,text=item,command=functools.partial(func,item))
        button.grid()


    frame2.update() # update frame2 height so it's no longer 0 ( height is 0 when it has just been created )
    canvas_container.configure(yscrollcommand=ysb.set, scrollregion="0 0 0 %s" % frame2.winfo_height()) # the scrollregion mustbe the size of the frame inside it,
                                                                                                                #in this case "x=0 y=0 width=0 height=frame2height"
                                                                                                                #width 0 because we only scroll verticaly so don't mind about the width.

    canvas_container.grid(sticky=W)
    frame_container.grid()

    ysb.configure(command = canvas_container.yview)
    canvas_container.configure(yscrollcommand = ysb.set)
    canvas_container.grid(row = 0, column = 0, sticky = N+E+S+W)
    ysb.grid(row = 0, column = 1, sticky = "ns")
    return text
root.text = frameText(root)
root.geometry('{}x{}'.format(800, 500))

root.mainloop()
"""
"""
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style()
style.theme_use('clam')

# configure the style
style.configure("Vertical.TScrollbar", gripcount=2,
                background="#6EA3DE", darkcolor="Black", lightcolor="LightGreen",
                troughcolor="white", bordercolor="black", arrowcolor="#81D3E0")

hs = ttk.Scrollbar(root, orient="vertical")
hs.place(x=5, y=5, height=200)


root.mainloop()

"""
"""
elif name == '':
    FNULL = open(os.devnull, 'w')    #use this if you want to suppress output to stdout from the subprocess
    args = Drive+":\\.exe"
    subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=False)
    
"""
