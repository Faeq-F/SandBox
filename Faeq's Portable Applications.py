from os import listdir
import functools
import os


def mouse_wheel(event):
    global count
    # respond to Linux or Windows wheel event
    if event.num == 5 or event.delta == -120:
        count -= 1
    if event.num == 4 or event.delta == 120:
        count += 1
    


count = 0
import time
dir = os.getcwd()
dir = dir + "Computer Resources\\PortableApps\\"
AllAppsFolders = listdir(dir)
executables = []
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(dir):
    for file in f:
        if '.exe' in file or '.ps1' in file:
            file = os.path.join(r, file)
            splitstring = file.split('\\')
            length = len(splitstring)
            if int(length) > 5:
                time.sleep(0)
            else:
                filename = splitstring[len(splitstring) - 1]
                newlist = (file,filename[:-4])
                executables.append(newlist)
        else:
            time.sleep(0)
names=[]
for app in executables:
    name = app[1]
    names.append(name)
import ctypes
import os
from string import ascii_uppercase
import threading
import sys
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
    import Tkinter as tk#                                                                       |
#                                                                                               |
#-----------------------------------------------------------------------------------------------#-------------#
#                                                                                                             |
#allows me to use math to decompress and compress data                                                        |
from math import *    #                                                                                       |
#                                                                                                             |
#                                                                                                             |
#                                                                                                             |
#                                                                                                             |
#allows me to manipulate os (mostly used for checking if things exist)                                        |
import os #                                                                                                   |
#                                                                                                             |
#                                                                                                             |
#used for the program to pass errors that would fail the program when on different operating systems          |
import time   #                                                                                               |
#-------------------------------------------------------------------------------------------------------------#
#                                                                                                             |
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


import subprocess
from multiprocessing import Process

def executeApps(appDirectory):
    from subprocess import Popen, PIPE
    FNULL = open(os.devnull, 'w')    #use this if you want to suppress output to stdout from the subprocess
    args = appDirectory
    proc = Popen(appDirectory, stdout=PIPE, stderr=PIPE,
                 encoding='utf8', errors='ignore')
    


def menu():

    #creates window
    window_for_menu = tk.Tk()

    ########################################Put any functions to be ran here######################################


    #puts the window in front of the others
    window_for_menu.attributes('-topmost', False)

    #creates a canvas to put the image on
    PutImageForBackground=Canvas(window_for_menu)

    #displays canvas
    PutImageForBackground.grid()

    #puts image for background onto canvas
    image1 = PhotoImage(
        file=dir+"Launcher\\blankbg.gif")

    #keep a link to the image to stop the image being garbage collected
    PutImageForBackground.img=image1

    #resizes background image
    displayimage = image1.subsample(1, 1)

    #displays image in background
    PutImageForBackground.create_image(400, 300, image=displayimage)


#       -----------------------------------------------------


    # creating the class, Window, and the Frame
    class Window(Frame):

        # Define settings
        def __init__(self, master=None):

            # parameters that are sent through the Frame class.
            Frame.__init__(self, master)

            #reference to the window
            self.master = master
            

            

            masterwindowsthatshouldonlybeusedasavariablethroughthis = self.master
            #runs the settings
            self.init_window()

        #Creation of init_window
        def init_window(self):

#       -----------------------------------------------------

            #icon for the window
            try:
                self.master.iconbitmap(dir+"Launcher\\Icon_for_windows.ico")

            except:
                time.sleep(0)

            #changing the title of the window
            self.master.title("Launcher by Faeq Faisal")
            

            # window size created
#       -----------------------------------------------------

            self.master.geometry("724x592")
            self.master.grid_columnconfigure(0, weight=1)
            self.master.grid_rowconfigure(1, weight=1)
            self.master.resizable(width=False, height=False)
            
            #Remove root window border and title bar with:
            self.master.overrideredirect(True)

            lastClickX = 0
            lastClickY = 0


            def SaveLastClickPos(event):
                global lastClickX, lastClickY
                lastClickX = event.x
                lastClickY = event.y


            def Dragging(event):
                x, y = event.x - lastClickX + self.master.winfo_x(), event.y - lastClickY + \
                    self.master.winfo_y()
                self.master.geometry("+%s+%s" % (x, y))

            self.master.bind('<Button-1>', SaveLastClickPos)
            self.master.bind('<B1-Motion>', Dragging)

#       -----------------------------------------------------

            #allowing the text to take the full space of the window
            self.grid()


#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


            #creating a menu
            menu = Menu(self.master)
            self.master.config(menu=menu)

            #create the file object
            file = Menu(menu)
            #adds a command to the menu option
            def exit_program():

                #closes window
                self.master.destroy()

                #creates new window
                mainWindow = tk.Tk()
                mainWindow.title('Bye!')
                mainWindow.overrideredirect(True)
                # pick a .gif image file you have in the working directory
                fname = dir+"Launcher\\Bye.gif"
                bg_image = tk.PhotoImage(file=fname)

                # get the width and height of the image
                w = bg_image.width()
                h = bg_image.height()

                # size the window so the image will fill it
                mainWindow.geometry('200x100')
                cv = tk.Canvas(width=w, height=h)

                #canvas for bg
                cv.pack(side='top', fill='both', expand='yes')
                cv.create_image(0, 0, image=bg_image, anchor='nw')

                # anchor='nw' implies upper left corner coordinates
                cv.create_text(15, 20, text="", fill="red", anchor='nw')

                #window's icon
                try:
                    mainWindow.iconbitmap(dir+"Launcher\\Icon_for_windows.ico")
                except:
                    time.sleep(0)

                    #can't resize window
                mainWindow.resizable(width=False, height=False)

                #creates enter rle button
                backimage = tk.PhotoImage(
                    file=dir+"Launcher\\goodBYE.gif")

                #resizes background image
                backimagee = backimage.subsample(8, 8)
                Button = tk.Button(cv, relief='flat', image=backimagee, command =mainWindow.destroy,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

                #places button on bg
                Button.pack(side='left', padx=30, pady=5, anchor='sw')
                Button.image= backimagee

                #centers window on the screen
                center(mainWindow)

                #runs window
                mainWindow.mainloop()




#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',font=("calibri", 12), justify=LEFT)
            labelspace.grid(sticky="w")

            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="Portable Apps Launcher",background='white',font=("calibri", 12), justify=LEFT, fg = 'SteelBlue1')
            labelspace.grid(sticky="w")

            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',font=("calibri", 12),cursor = "trek")
            labelspace.grid(sticky="w")



#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

            #checks if buttons are pressed
            button_flag = True

            # create frame
            frame1 = tk.Frame(PutImageForBackground,bg='#FFFFFF',padx=10)
            frame1.grid(sticky=tk.W)

#       -----------------------------------------------------

            from tkinter import ttk
            class ScrollbarFrame(tk.Frame):
                """
                Extends class tk.Frame to support a scrollable Frame 
                This class is independent from the widgets to be scrolled and 
                can be used to replace a standard tk.Frame
                """

                def __init__(self, parent, **kwargs):
                    tk.Frame.__init__(self, parent, **kwargs)

                    # The Scrollbar, layout to the right
                    vsb = tk.Scrollbar(self, orient="vertical")
                    vsb.pack(side="right", fill="y")

                    # The Canvas which supports the Scrollbar Interface, layout to the left
                    self.canvas = tk.Canvas(
                        self, borderwidth=0, background="#ffffff", height=400, width=280)
                    self.canvas.pack(side="left", fill="both", expand=True)

                    # Bind the Scrollbar to the self.canvas Scrollbar Interface
                    self.canvas.configure(yscrollcommand=vsb.set)
                    vsb.configure(command=self.canvas.yview)

                    # The Frame to be scrolled, layout into the canvas
                    # All widgets to be scrolled have to use this Frame as parent
                    self.scrolled_frame = tk.Frame(
                        self.canvas, background=self.canvas.cget('bg'))
                    self.canvas.create_window(
                        (4, 4), window=self.scrolled_frame, anchor="nw")

                    # Configures the scrollregion of the Canvas dynamically
                    self.scrolled_frame.bind("<Configure>", self.on_configure)

                def on_configure(self, event):
                    """Set the scroll region to encompass the scrolled frame"""
                    self.canvas.configure(scrollregion=self.canvas.bbox("all"))
            
            
            
            
            
            sbf = ScrollbarFrame(frame1)
            frame1.grid_rowconfigure(0, weight=1)
            frame1.grid_columnconfigure(0, weight=1)
            sbf.grid(row=0, column=0, sticky='nsew')
            frame = sbf.scrolled_frame
            # sbf.pack(side="top", fill="both", expand=True)

            mylist = []
            for name in names:
                mylist.append(name)
            mylist.sort(key=str.lower)

            def func(name):
                extract = [item[0] for item in executables]
                # Driver code
                for i in extract:
                    if name in i:
                        appposition = i
                        p1 = threading.Thread(
                            name='child procs', target=executeApps(appposition))
                        p1.start()
                    else:
                        continue

            

            # Some data, layout into the sbf.scrolled_frame
            
            for row in range(len(executables)):
                text = "%s" % row
                tk.Label(frame, text=text,
                         width=3, borderwidth="1", relief=FLAT, fg='Steelblue1', bg='#FFFFFF') \
                    .grid(row=row, column=0)
            frame.bind("<MouseWheel>", mouse_wheel)
                    
            for item in mylist:
                button = Button(frame, text=item, command=functools.partial(
                    func, item), relief=FLAT, bg='#FFFFFF', fg='#6EA3DE')
                button.grid(column = 1,row=mylist.index(item), sticky=W)
                    
                    
                    
                    
                    

            Quitimage = tk.PhotoImage(file=dir+"Launcher\\5.gif")
            #resizes background image
            Quitimagee = Quitimage.subsample(3, 3)

            #creates quit button
            QuitButton = tk.Button(frame1, image=Quitimagee, bg="#FFFFFF",fg='#FFFFFF',relief=FLAT,cursor = "target",command=exit_program)

            QuitButton.grid(sticky="w")
            QuitButton.image = Quitimagee

#       -----------------------------------------------------

            #creates enter rle button
            AQAimage = tk.PhotoImage(file=dir+"Launcher\\AQA.gif")

            #resizes background image
            AQAimagee = AQAimage.subsample(2, 2)


#       -----------------------------------------------------


            #puts my name on the program
            Name = tk.Button(PutImageForBackground,image = AQAimagee, text="Program By Faeq Faisal ",bg='#81D3E0',fg="#FFFFFF",font=("Segoe UI Emoji",10),relief=FLAT,cursor = "trek")
            Name.grid(sticky="e")
            Name.image = AQAimagee


#       -----------------------------------------------------



            #image for text
            image = tk.PhotoImage(file=dir+"Launcher\\r.gif")
            read = tk.Label(PutImageForBackground, image=image,background='white')


            #showing image
            read.grid(sticky="w")
            read.image = image

#       -----------------------------------------------------

            #asks the user to read my read-me note
            labelspace = tk.Label(PutImageForBackground, text="   ",background='#FFFFFF',fg='SteelBlue1', font=("Calibri", 9),cursor = "arrow")
            labelspace.grid(sticky='w')


            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")


            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text=".                                                                                                                                                                                                                                              .", background='white',cursor = "trek")
            labelspace.grid(sticky="w")

#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

#                                                             creates canvas with size and positioning


            PutImageForBackground.create_window(900,900)


#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


#                                      makes sure that the python interpreter does not close as soon as the program is read
#                                            also makes sure that the interpreter only closes when the program is done
            edit = Menu(menu)

        def client_exit(self):
            exit()


#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

    #creation
    app = Window(window_for_menu)

    #centers window
    center(window_for_menu)


    #runs window
    window_for_menu.mainloop()


#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


#                                                                    #---------------------------#
#                                                                    |       End of the code     |
#                                                                    #---------------------------#
#
#                                                                    running all of the code above
menu()

