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

def AudioOutput():
    subprocess.Popen(['Powershell.exe',"\""+Drive + ":\\Portable Applications\\Audio output\\mute audio when output device unplugged.ps1\""])


def word():
    FNULL = open(os.devnull, 'w')    #use this if you want to suppress output to stdout from the subprocess
    args = Drive+":\\Portable Applications\\freeoffice\\TextMaker.exe"
    subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=False)

def yvd():
    os.system("\""+Drive+":\\Portable Applications\\Youtube Video Downloader\\yt.py\"")


def menu():

    #creates window
    window_for_menu = tk.Tk()

    ########################################Put any functions to be ran here######################################

    def on_closing():

        #close window
        try:
            window_for_menu.destroy()
        except:
            time.sleep(0)

        #new window created
        mainWindow = tk.Tk()
        mainWindow.title('background image')

        # pick a .gif image file you have in the working directory
        fname = DriveP+":\\Use non-encrypted volumes\\Launcher\\NoClosing.gif.gif"
        bg_image = tk.PhotoImage(file=fname)

        # get the width and height of the image
        w = bg_image.width()
        h = bg_image.height()

        # size the window so the image will fill it
        mainWindow.geometry('724x592')
        cv = tk.Canvas(width=w, height=h)

        #new canvas for bg
        cv.pack(side='top', fill='both', expand='yes')
        cv.create_image(0, 0, image=bg_image, anchor='nw')

        # anchor='nw' implies upper left corner coordinates
        cv.create_text(15, 20, text="", fill="red", anchor='nw')

        #window's icon
        try:
            mainWindow.iconbitmap(DriveP+":\\Use non-encrypted volumes\\Launcher\\Icon_for_windows.ico")
        except:
            time.sleep(0)

            #can't resize window
        mainWindow.resizable(width=False, height=False)
        #creates enter rle button
        backimage = tk.PhotoImage(
            file=DriveP+":\\Use non-encrypted volumes\\Launcher\\Back.gif")

        #puts the window in front of the menu
        mainWindow.attributes('-topmost', True)

        #creates background
        mainWindow["bg"] = "#FFFFFF"


        #does not allow window to be moved
        mainWindow.overrideredirect(True)


        #does not allow it to be resized
        mainWindow.resizable(width=False, height=False)


        #back to prev. window
        def noclose():

            #close window
            mainWindow.destroy()

            #back to prev. window
            menu()


        #resizes background image
        backimagee = backimage.subsample(2, 2)
        Button = tk.Button(cv, relief='flat', image=backimagee, command =noclose ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

        #places button on bg
        Button.pack(side='left', padx = 3, pady=0, anchor='s')
        Button.image= backimagee

        #runs window
        center(mainWindow)
        mainWindow.mainloop()

#       -----------------------------------------------------

    #overides the close button
    window_for_menu.protocol("WM_DELETE_WINDOW", on_closing)

    #puts the window in front of the others
    window_for_menu.attributes('-topmost', False)

    #creates a canvas to put the image on
    PutImageForBackground=Canvas(window_for_menu)

    #displays canvas
    PutImageForBackground.grid()

    #puts image for background onto canvas
    image1 = PhotoImage(
        file=DriveP+":\\Use non-encrypted volumes\\Launcher\\new.gif")

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
                self.master.iconbitmap(DriveP+":\\Use non-encrypted volumes\\Launcher\\Icon_for_windows.ico")

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

                # pick a .gif image file you have in the working directory
                fname = DriveP+":\\Use non-encrypted volumes\\Launcher\\Bye.gif"
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
                    mainWindow.iconbitmap(DriveP+":\\Use non-encrypted volumes\\Launcher\\Icon_for_windows.ico")
                except:
                    time.sleep(0)

                    #can't resize window
                mainWindow.resizable(width=False, height=False)

                #creates enter rle button
                backimage = tk.PhotoImage(
                    file=DriveP+":\\Use non-encrypted volumes\\Launcher\\goodBYE.gif")

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
            labelspace = tk.Label(PutImageForBackground, text="",background='white',font=("calibri", 12), justify=LEFT)
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
            def frameText(frame, **kw):
                style = ttk.Style()
                style.theme_use('alt')

                # configure the style
                style.configure("Vertical.TScrollbar", gripcount=3,
                                background="#6EA3DE", darkcolor="Black", lightcolor="SteelBlue1",
                                troughcolor="white", bordercolor="black", arrowcolor="#81D3E0",relief="flat")



                ysb = ttk.Scrollbar(frame,orient="vertical")
                text = Canvas(frame, **kw)
                frame_container=Frame(frame)
                import functools
                canvas_container=Canvas(frame_container, height=400, width=240, bg='#FFFFFF')
                frame2=Frame(canvas_container, bg='#FFFFFF')
                canvas_container.create_window((0,0),window=frame2,anchor='nw')
                



                def func(name):
                    if name == 'Visual Studio':
                        p1 = threading.Thread(name='child procs', target=Visual)
                        p1.start()
                mylist = AllApps
       

                for item in mylist:
                    button = Button(frame2, text=item, command=functools.partial(
                        func, item), relief=FLAT, bg='#FFFFFF', font=('Phenomena', 14), fg='#6EA3DE')
                    button.grid()


                frame2.update() # update frame2 height so it's no longer 0 ( height is 0 when it has just been created )
                canvas_container.configure(yscrollcommand=ysb.set, scrollregion="0 0 0 %s" % frame2.winfo_height()) # the scrollregion mustbe the size of the frame inside it,
                                                                                                                            #in this case "x=0 y=0 width=0 height=frame2height"
                                                                                                                            #width 0 because we only scroll verticaly so don't mind about the width.

                canvas_container.grid(sticky=W)
                frame_container.grid(sticky=tk.W)

                ysb.configure(command = canvas_container.yview)




                canvas_container.configure(yscrollcommand = ysb.set)
                ysb.bind_all("<MouseWheel>")
                def _on_mousewheel(self, event):
                    canvas_container.yview_scroll(int(-1 *
                                                  (event.delta/120)), "units")
                canvas_container.grid(row = 0, column = 0, sticky = N+E+S+W)
                ysb.grid(row = 0, column = 1, sticky = "ns")

                return text
            frame1.text = frameText(frame1)
            #creates enter rle button
            def startup():                
                p18 = threading.Thread(name='child procs', target=eyedropper)
                p18.start()
                
            st = tk.Button(frame1, text='Startup', bg="#FFFFFF",fg='#6EA3DE',relief=FLAT,cursor = "target",command=startup, font=('Phenomena',16))

            st.grid()
            Quitimage = tk.PhotoImage(file=DriveP+":\\Use non-encrypted volumes\\Launcher\\5.gif")
            #resizes background image
            Quitimagee = Quitimage.subsample(3, 3)

            #creates quit button
            QuitButton = tk.Button(frame1, image=Quitimagee, bg="#FFFFFF",fg='#FFFFFF',relief=FLAT,cursor = "target",command=exit_program)

            QuitButton.grid(sticky="w")
            QuitButton.image = Quitimagee

#       -----------------------------------------------------

            #creates enter rle button
            AQAimage = tk.PhotoImage(file=DriveP+":\\Use non-encrypted volumes\\Launcher\\AQA.gif")

            #resizes background image
            AQAimagee = AQAimage.subsample(2, 2)


#       -----------------------------------------------------


            #puts my name on the program
            Name = tk.Button(PutImageForBackground,image = AQAimagee, text="Program By Faeq Faisal ",bg='#81D3E0',fg="#FFFFFF",font=("Segoe UI Emoji",10),relief=FLAT,cursor = "trek")
            Name.grid(sticky="e")
            Name.image = AQAimagee


#       -----------------------------------------------------



            #image for text
            image = tk.PhotoImage(file=DriveP+":\\Use non-encrypted volumes\\Launcher\\r.gif")
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
