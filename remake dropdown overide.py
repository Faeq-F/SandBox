from tkinter import *
import tkinter as tk
import time
import webbrowser
try:
    from tkinter import *
except ImportError:
    from Tkinter import *
OZoneIzotopeSemiWhite = "#3d3e40" # when hovering
buttonBackground = "#303336" #default
buttonforeground = "#FFFFFF"
BACKGROUND2 = "#FFFFFF"
curOpt = ''
txt = ''
lastClickX = 0
lastClickY = 0

class CustomButton(tk.Canvas):
    def __init__(self, parent, width, height, color, command=None):
        tk.Canvas.__init__(self, parent, borderwidth=1,
            relief="raised", highlightthickness=0)
        self.command = command

        padding = 4
        id = self.create_oval((padding,padding,
            width+padding, height+padding), outline=color, fill=color)
        (x0,y0,x1,y1)  = self.bbox("all")
        width = (x1-x0) + padding
        height = (y1-y0) + padding
        self.configure(width=width, height=height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()
class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.master.title("Toolbar")

        menubar = Menu(self.master)
        self.fileMenu = Menu(self.master, tearoff=0)
        self.fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=self.fileMenu)

        toolbar = Frame(self.master, bd=1, relief=RAISED)

        self.img = Image.open("exit.png")
        eimg = ImageTk.PhotoImage(self.img)

        exitButton = Button(toolbar, image=eimg, relief=FLAT,command=self.quit)
        exitButton.image = eimg
        exitButton.pack(side=LEFT, padx=2, pady=2)

        toolbar.pack(side=TOP, fill=X)
        self.master.config(menu=menubar)
        self.pack()

    def onExit(self):
        self.quit()

class DropDownButton():
    def __init__(self, parent, placement, opTions, **kw):
        self.parent = parent
        self.options = opTions

        self.om_variable = tk.StringVar(self.parent)
        self.om_variable.set(self.options[0])
        self.om_variable.trace('w', self.option_select)

        self.om = tk.OptionMenu(self.parent, self.om_variable, *self.options)
        self.om["menu"].config(fg=buttonforeground, bg=buttonBackground, activebackground=OZoneIzotopeSemiWhite, activeforeground=BACKGROUND2, borderwidth = 0)
        self.om.config(fg=buttonforeground, bg=buttonBackground, activebackground=OZoneIzotopeSemiWhite, activeforeground=BACKGROUND2, bd =0)
        self.om.place(x = placement,y = placement, relx=0.5, rely=0.5, anchor=S)
        self.om.bind("<Enter>", self.on_enter)
        self.om.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        if self.om_variable.get() == self.options[0]:
            print ("none selected")
        elif self.om_variable.get() == self.options[1]:
            print ("Hello")
        elif self.om_variable.get() == self.options[2]:
            print ("Hello 2!")
        elif self.om_variable.get() == self.options[3]:
            print("Hell0 3!")
        elif self.om_variable.get() == self.options[4]:
            print("Hell0 4!")




    def on_leave(self, enter):
        time.sleep(0)

    def option_select(self, *args):
        print('Current option set to '+self.om_variable.get())
        txt = self.om_variable.get()
        curOpt = txt
        global option
        option = curOpt
        l["text"] = txt


class NewRoot(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.attributes('-alpha', 0.0)

class MyMain(Toplevel):
    def __init__(self, master):
        Toplevel.__init__(self, master)
        self.overrideredirect(1)
        self.attributes('-topmost', 1)
        self.geometry('+100+100')
        self.bind('<ButtonRelease-3>', self.on_close)  #right-click to get out
        can = Canvas(self, bg = 'blue', height=500, width=500)
        can.place(relx=0.5, rely=0.5, anchor=CENTER)
        backg = '#FFFFFF'
        toolbar = Frame(self, bd=1, relief=RAISED,bg = 'black')

        def SaveLastClickPos(event):
            global lastClickX, lastClickY
            lastClickX = event.x
            lastClickY = event.y
        def Dragging(event):
            x, y = event.x - lastClickX + self.winfo_x(), event.y - lastClickY + self.winfo_y()
            self.geometry("+%s+%s" % (x , y))
        #creates enter rle button
        imagetobeused = tk.PhotoImage(file="1.gif")
        #resizes background image
        imagetobeusede = imagetobeused.subsample(3, 3)

        exitButton = Button(toolbar, relief=FLAT, image=imagetobeusede,command=self.destroy,bg=backg)
        exitButton.pack(side=LEFT, padx=2, pady=2)
        exitButton.image = imagetobeusede
        quitButton = Button(toolbar, text = 'destroy', relief=FLAT,command=self.destroy,bg=backg)
        quitButton.pack(side=LEFT, padx=2, pady=2)
        button = CustomButton(toolbar, 50, 25, 'red')
        button.pack()
        def endcommand():
            print('end button pressed')
            self.destroy()
        end = Button(toolbar, text = 'end', relief=FLAT,command=endcommand,bg=backg)
        end.pack(side=LEFT, padx=2, pady=2)
        def lastcommand():
            print('last command')
            self.destroy()
        exitButton = Button(toolbar, text = 'last', relief=FLAT,command=lastcommand,bg=backg)
        exitButton.pack(side=LEFT, padx=2, pady=2)
        toolbar.pack(side=TOP, fill=X)
        #-----------------------------------------------
        frame = Frame(self)
        frame.pack()
        DropDownButton(can, 1, ['none','one', 'two', 'three', 'four'])
        global l
        l = Label(frame, text=txt, font=('Arial',18))
        l.place(relx=0.5, rely=0.5, anchor=N)
        def enter():
            print(option)
            link = 'http://'+option
            webbrowser.open(link, new=2, autoraise=True)
        b = Button(can, text = 'submit', command = enter,cursor='target')
        b.place(relx=0.5, rely=0.5, anchor=N)

        lb = Button(can, text = 'end', command = self.destroy,cursor='target')
        lb.place(relx=0.5, rely=0.632,anchor=N)
        toolbar.bind('<Button-1>', SaveLastClickPos)
        toolbar.bind('<B1-Motion>', Dragging)
        self.geometry('500x500')
        center(self)


    def on_close(self, event):
        self.master.destroy()

def center(win):#                                                                                             |
    #                                                                                                         |
    #updates window to make it active#                                                                        |
    win.update_idletasks()#                                                                                   |
    #                                                                                                         |
    #finds width of screen#                                                                                   |
    width = win.winfo_width()#                                                                                |
    #                                                                                                         |
    #finds height of screen#                                                                                  |
    height = win.winfo_height()#                                                                              |
    #                                                                                                         |
    #creates the x coordinate for the window by finding the center by dividing it by 2#                       |
    x = (win.winfo_screenwidth() // 2) - (width // 2)#                                                        |
    #                                                                                                         |
    #creates the y coordinate for the window by finding the center by dividing it by 2#                       |
    y = (win.winfo_screenheight() // 2) - (height // 2)#                                                      |
    #                                                                                                         |
    #creates the final coordinates#                                                                           |
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))#                                                  |
#------------------------------#------------------------------------------------------------------------------#



def k():
    if __name__ == '__main__':
        root = NewRoot()
        root.lower()
        root.iconify()
        root.title('Program')
        app = MyMain(root)
        app.mainloop()
k()
