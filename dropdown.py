from tkinter import *
import tkinter as tk
import time
import webbrowser
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
curOpt = ''
txt = ''

class Counter(object):#                                                                                   |
    counts = {}##                                                                                         |
#                                                                                                             |
    @staticmethod##                                                                                       |
    def count(func):##                                                                                    |
        def wrapped(*args,**kwargs):##                                                                    |
            if func.__name__ in Counter.counts.keys():##                                                  |
                Counter.counts[func.__name__] += 1##                                                      |
            else:##                                                                                       |
                Counter.counts[func.__name__] = 1##                                                       |
            return func(*args,**kwargs)##                                                                 |
        return wrapped##                                                                                  |
#                                                                                                             |

def k():


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

            exitButton = Button(toolbar, image=eimg, relief=FLAT,
                command=self.quit)
            exitButton.image = eimg
            exitButton.pack(side=LEFT, padx=2, pady=2)

            toolbar.pack(side=TOP, fill=X)
            self.master.config(menu=menubar)
            self.pack()


        def onExit(self):
            self.quit()


    OZoneIzotopeSemiWhite = "#3d3e40" # when hovering
    buttonBackground = "#303336" #default
    buttonforeground = "#FFFFFF"
    BACKGROUND2 = "#FFFFFF"
    

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
            if self.om_variable.get() == self.options[1]:
                print ("Hello")
            elif self.om_variable.get() == self.options[2]:
                print ("Hello 2!")
            elif self.om_variable.get() == self.options[3]:
                print("Hell0 3!")
            elif self.om_variable.get() == self.options[4]:
                print("Hell0 4!")
                
            
                

        def on_leave(self, enter):
            time.sleep(0)
            
        @Counter.count## 
        def option_select(self, *args):
            print('Current option set to '+self.om_variable.get())
            txt = self.om_variable.get()
            curOpt = txt
            global option
            option = curOpt
            l["text"] = txt


    if __name__ == '__main__':

        root = tk.Tk()
        root = NewRoot()
        root.lower()
        root.iconify()
        root.title('Program')
        
        can = Canvas(root, bg = 'blue', height=500, width=500)
        can.place(relx=0.5, rely=0.5, anchor=CENTER)
        image1=PhotoImage(file="blankbg.gif")#                                          |
        #                                                                           |
        #keep a link to the image to stop the image being garbage collected         |
        #can.img=image1#                                           |
        #                                                                           |
        #resizes background image                                                   |
        #displayimage = image1.subsample(1, 1)#                                      |
        #                                                                           |
        #displays image in background                                               |
        #can.create_image(500, 500, image=displayimage)#        
        #--------------------------------------------
        def move_window(event):
            root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))
        backg = '#FFFFFF'
        toolbar = Frame(root, bd=1, relief=RAISED,bg = 'black')
        toolbar.bind('<B1-Motion>', move_window)
        exitButton = Button(toolbar, text = 'quit', relief=FLAT,command=root.quit,bg=backg)
        exitButton.pack(side=LEFT, padx=2, pady=2)
        quitButton = Button(toolbar, text = 'destroy', relief=FLAT,command=root.destroy,bg=backg)
        quitButton.pack(side=LEFT, padx=2, pady=2)
        def endcommand():
            print('end button pressed')
        end = Button(toolbar, text = 'end', relief=FLAT,command=endcommand,bg=backg)
        end.pack(side=LEFT, padx=2, pady=2)
        def lastcommand():
            print('last command')
        exitButton = Button(toolbar, text = 'last', relief=FLAT,command=lastcommand,bg=backg)
        exitButton.pack(side=LEFT, padx=2, pady=2)
        toolbar.pack(side=TOP, fill=X)
        #-----------------------------------------------
        frame = Frame(root)
        frame.pack()
        DropDownButton(can, 1, ['none','one', 'two', 'three', 'four'])
        l = Label(frame, text=txt)
        l.place(relx=0.5, rely=0.5, anchor=N)
        def enter():
            print(option)
            link = 'http://'+option
            webbrowser.open(link, new=2, autoraise=True)
        b = Button(can, text = 'submit', command = enter,cursor='target')
        b.place(relx=0.5, rely=0.5, anchor=N)
        
        l = Button(can, text = 'end', command = root.destroy,cursor='target')
        l.place(relx=0.5, rely=0.632,anchor=N)
        
        root.geometry('500x500')
        center(root)
        app = MyMain(root)
        app.mainloop()

        
k()


print(Counter.counts)
