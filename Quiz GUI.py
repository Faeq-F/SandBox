name = ''
level =''
sc = 0

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
import random
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
import sys
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

def menu():
    
    #creates window
    window_for_menu = tk.Tk()
    
    ########################################Put any functions to be ran here######################################
    def notalpha():
        
        wr = tk.Tk()
        wr.geometry("724x592")
            
        wr.resizable(width=False, height=False)
        #icon for the window
        try:
            wr.iconbitmap('Icon_for_windows.ico')
            
        except:
            time.sleep(0)
        wr.title("Cyber Security Quiz")#  |
        PutImageForBackground=Canvas(wr)#                              |
        
        #displays canvas                                                            |
        PutImageForBackground.grid()#                                               |
        #                                                                           |
        #puts image for background onto canvas                                      |
        image1=PhotoImage(file="blankbg.gif")#                                          |
        #                                                                           |
        #keep a link to the image to stop the image being garbage collected         |
        PutImageForBackground.img=image1#                                           |
        #                                                                           |
        #resizes background image                                                   |
        displayimage = image1.subsample(1, 1)#                                      |
        #                                                                           |
        #displays image in background                                               |
        PutImageForBackground.create_image(400, 300, image=displayimage)#
        label = tk.Label(PutImageForBackground, relief='flat', text="Invalid name",bg="#FFFFFF",fg='#000000',cursor = "target")
        label.pack(side='left', padx = 3, pady=0, anchor='n')
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        backimaget = PhotoImage(file = "C.gif")#                                                                         |
        #resizes background image                                                                                                  |
        backimagee = backimaget.subsample(2, 2)               #
        def k():
            wr.destroy()
            menu()
        Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =k ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
        #                                                                                                                          |
        #placing button on window                                                                                                  |
        Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
        Button.image= backimagee#
        center(wr)
        wr.mainloop()

    class Counter(object):
        counts = {}

        @staticmethod
        def count(func):
            def wrapped(*args,**kwargs):
                if func.__name__ in Counter.counts.keys():
                    Counter.counts[func.__name__] += 1
                else:
                    Counter.counts[func.__name__] = 1
                return func(*args,**kwargs)
            return wrapped
    #
    @Counter.count
    def right():
        
        wr = tk.Tk()
        wr.geometry("724x592")
            
        wr.resizable(width=False, height=False)
        #icon for the window
        try:
            wr.iconbitmap('Icon_for_windows.ico')
            
        except:
            time.sleep(0)
        wr.title("Cyber Security Quiz")#  |
        PutImageForBackground=Canvas(wr)#                              |
        
        #displays canvas                                                            |
        PutImageForBackground.grid()#                                               |
        #                                                                           |
        #puts image for background onto canvas                                      |
        image1=PhotoImage(file="blankbg.gif")#                                          |
        #                                                                           |
        #keep a link to the image to stop the image being garbage collected         |
        PutImageForBackground.img=image1#                                           |
        #                                                                           |
        #resizes background image                                                   |
        displayimage = image1.subsample(1, 1)#                                      |
        #                                                                           |
        #displays image in background                                               |
        PutImageForBackground.create_image(400, 300, image=displayimage)#
        label = tk.Label(PutImageForBackground, relief='flat', text="You got it right",bg="#FFFFFF",fg='#000000',cursor = "target")
        label.pack(side='left', padx = 3, pady=0, anchor='n')
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        backimaget = PhotoImage(file = "C.gif")#                                                                         |
        #resizes background image                                                                                                  |
        backimagee = backimaget.subsample(2, 2)               #                                                                     |
        Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =wr.destroy ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
        #                                                                                                                          |
        #placing button on window                                                                                                  |
        Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
        Button.image= backimagee#
        center(wr)
        wr.mainloop()


    def wrong():
        wr = tk.Tk()
        wr.geometry("724x592")
            
        wr.resizable(width=False, height=False)
        #icon for the window
        try:
            wr.iconbitmap('Icon_for_windows.ico')
            
        except:
            time.sleep(0)
        wr.title("Cyber Security Quiz")#  |
        PutImageForBackground=Canvas(wr)#                              |
        #                                                                           |
        #displays canvas                                                            |
        PutImageForBackground.grid()#                                               |
        #                                                                           |
        #puts image for background onto canvas                                      |
        image1=PhotoImage(file="blankbg.gif")#                                          |
        #                                                                           |
        #keep a link to the image to stop the image being garbage collected         |
        PutImageForBackground.img=image1#                                           |
        #                                                                           |
        #resizes background image                                                   |
        displayimage = image1.subsample(1, 1)#                                      |
        #                                                                           |
        #displays image in background                                               |
        PutImageForBackground.create_image(400, 300, image=displayimage)#
        label = tk.Label(PutImageForBackground, relief='flat', text="You got it wrong",bg="#FFFFFF",fg='#000000',cursor = "target")
        label.pack(side='left', padx = 3, pady=0, anchor='n')
    
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        backimaget = PhotoImage(file = "C.gif")#                                                                         |
        #resizes background image                                                                                                  |
        backimagee = backimaget.subsample(2, 2)               #                                                                     |
        Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =wr.destroy ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
        #                                                                                                                          |
        #placing button on window                                                                                                  |
        Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
        Button.image= backimagee#
        center(wr)
        wr.mainloop()

    def Qss():
        def Cont():
            questions = ["Question 1", "Question 2", "Question 3", "Question 4", "Question 5", "Question 6", "Question 7", "Question 8", "Question 9", "Question 10"]
            
            random.shuffle(questions)
            
            #points counter
            points = 0
            
            #checks the amount of questions completed
            question = 0
            
            #checks if 10 questions have been completed
            while question < 10:
            
                #checks if it is question 1
                if questions[0] == "Question 1":
                    
                    question += 1
                    
                    del questions[0]
                    
                    def r():
                        windowFor1.destroy()
                        right()
                        
                    
                    def w():
                        windowFor1.destroy()
                        wrong()
                    
                    windowFor1 = tk.Tk()
                    windowFor1.geometry("724x592")
            
                    windowFor1.resizable(width=False, height=False)
                                #icon for the window
                    try:
                        windowFor1.iconbitmap('Icon_for_windows.ico')
                        
                    except:
                        time.sleep(0)
                    windowFor1.title("Cyber Security Quiz")#  |
                    PutImageForBackground=Canvas(windowFor1)#                              |
                    #                                                                           |
                    #displays canvas                                                            |
                    PutImageForBackground.grid()#                                               |
                    #                                                                           |
                    #puts image for background onto canvas                                      |
                    image1=PhotoImage(file="blankbg.gif")#                                          |
                    #                                                                           |
                    #keep a link to the image to stop the image being garbage collected         |
                    PutImageForBackground.img=image1#                                           |
                    #                                                                           |
                    #resizes background image                                                   |
                    displayimage = image1.subsample(1, 1)#                                      |
                    #                                                                           |
                    
                    #displays image in background                                               |
                    PutImageForBackground.create_image(400, 300, image=displayimage)#
                                
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                                
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                                
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                                
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    label = tk.Label(PutImageForBackground, relief='flat', text="\nQ. Which one of these is a safe password?\n",bg="#FFFFFF",fg='#000000',cursor = "target")
                    label.pack(side='left', padx = 3, pady=0, anchor='s')
                    
                    backimaget = PhotoImage(file = "C.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimaget.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =w ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #                                                                                                                          |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    
                    backimagey = PhotoImage(file = "3.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimagey.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =w ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #                                                                                                                          |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    
                    backimagew = PhotoImage(file = "2.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimagew.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =r ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    center(windowFor1)
                    windowFor1.mainloop()
                #checks if it is question 1
                elif questions[0] == "Question 2":
                    
                    question += 1
                    
                    del questions[0]
                    
                    def r():
                        windowFor1.destroy()
                        right()
                        
                    
                    def w():
                        windowFor1.destroy()
                        wrong()
                        
                    
                    windowFor1 = tk.Tk()
                    windowFor1.geometry("724x592")
            
                    windowFor1.resizable(width=False, height=False)
                    #icon for the window
                    try:
                        windowFor1.iconbitmap('Icon_for_windows.ico')
                        
                    except:
                        time.sleep(0)
                    windowFor1.title("Cyber Security Quiz")#  |
                    PutImageForBackground=Canvas(windowFor1)#                              |
                    #                                                                           |
                    #displays canvas                                                            |
                    PutImageForBackground.grid()#                                               |
                    #                                                                           |
                    #puts image for background onto canvas                                      |
                    image1=PhotoImage(file="blankbg.gif")#                                          |
                    #                                                                           |
                    #keep a link to the image to stop the image being garbage collected         |
                    PutImageForBackground.img=image1#                                           |
                    #                                                                           |
                    #resizes background image                                                   |
                    displayimage = image1.subsample(1, 1)#                                      |
                    #                                                                           |
                    #displays image in background                                               |
                    PutImageForBackground.create_image(400, 300, image=displayimage)#
                                                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                                                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                                 
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                 
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()

                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()

                    label = tk.Label(PutImageForBackground, relief='flat', text="\nQ. What can you do to get less spam?\n",bg="#FFFFFF",fg='#000000',cursor = "target")
                    label.pack(side='left', padx = 3, pady=0, anchor='s')
                    backimaget = PhotoImage(file = "C.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimaget.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =r ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #                                                                                                                          |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    
                    backimagey = PhotoImage(file = "3.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimagey.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =w ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #                                                                                                                          |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    
                    backimagew = PhotoImage(file = "2.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimagew.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =w ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    center(windowFor1)
                    windowFor1.mainloop()
                elif questions[0] == "Question 3":
                    
                    question += 1
                    
                    del questions[0]
                    
                    def r():
                        windowFor1.destroy()
                        right()
                        
                    
                    def w():
                        windowFor1.destroy()
                        wrong()
                        
                    
                    windowFor1 = tk.Tk()
                    windowFor1.geometry("724x592")
            
                    windowFor1.resizable(width=False, height=False)
                    #icon for the window
                    try:
                        windowFor1.iconbitmap('Icon_for_windows.ico')
                        
                    except:
                        time.sleep(0)
                    windowFor1.title("Cyber Security Quiz")#  |
                    PutImageForBackground=Canvas(windowFor1)#                              |
                    #                                                                           |
                    #displays canvas                                                            |
                    PutImageForBackground.grid()#                                               |
                    #                                                                           |
                    #puts image for background onto canvas                                      |
                    image1=PhotoImage(file="blankbg.gif")#                                          |
                    #                                                                           |
                    #keep a link to the image to stop the image being garbage collected         |
                    PutImageForBackground.img=image1#                                           |
                    #                                                                           |
                    #resizes background image                                                   |
                    displayimage = image1.subsample(1, 1)#                                      |
                    #                                                                           |
                    #displays image in background                                               |
                    PutImageForBackground.create_image(400, 300, image=displayimage)#
                                                        
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                                                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    

                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                            
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                                                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()

                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()

                    label = tk.Label(PutImageForBackground, relief='flat', text="\nQ. What term describes the act of annoying someone online?\n",bg="#FFFFFF",fg='#000000',cursor = "target")
                    label.pack(side='left', padx = 3, pady=0, anchor='s')
                    backimaget = PhotoImage(file = "C.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimaget.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =r ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #                                                                                                                          |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    
                    backimagey = PhotoImage(file = "3.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimagey.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =w ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #                                                                                                                          |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    
                    backimagew = PhotoImage(file = "2.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimagew.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =w ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    center(windowFor1)
                    windowFor1.mainloop()
                elif questions[0] == "Question 4":
                    
                    question += 1
                    
                    del questions[0]
                    
                    def r():
                        windowFor1.destroy()
                        right()
                        
                    
                    def w():
                        windowFor1.destroy()
                        wrong()
                        
                    
                    windowFor1 = tk.Tk()
                    windowFor1.geometry("724x592")
            
                    windowFor1.resizable(width=False, height=False)
                    #icon for the window
                    try:
                        windowFor1.iconbitmap('Icon_for_windows.ico')
                        
                    except:
                        time.sleep(0)
                    windowFor1.title("Cyber Security Quiz")#  |
                    PutImageForBackground=Canvas(windowFor1)#                              |
                    #                                                                           |
                    #displays canvas                                                            |
                    PutImageForBackground.grid()#                                               |
                    #                                                                           |
                    #puts image for background onto canvas                                      |
                    image1=PhotoImage(file="blankbg.gif")#                                          |
                    #                                                                           |
                    #keep a link to the image to stop the image being garbage collected         |
                    PutImageForBackground.img=image1#                                           |
                    #                                                                           |
                    #resizes background image                                                   |
                    displayimage = image1.subsample(1, 1)#                                      |
                    #                                                                           |
                    #displays image in background                                               |
                    PutImageForBackground.create_image(400, 300, image=displayimage)#
                                                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                                                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                                                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    

                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()

                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                                                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()

                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()

                    label = tk.Label(PutImageForBackground, relief='flat', text="\nQ. What software can you use to avoid getting viruses?\n",bg="#FFFFFF",fg='#000000',cursor = "target")
                    label.pack(side='left', padx = 3, pady=0, anchor='s')
                    backimaget = PhotoImage(file = "C.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimaget.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =w ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #                                                                                                                          |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    
                    backimagey = PhotoImage(file = "3.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimagey.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =r ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #                                                                                                                          |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    
                    backimagew = PhotoImage(file = "2.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimagew.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =w ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    center(windowFor1)
                    windowFor1.mainloop()
                elif questions[0] == "Question 5":
                    
                    question += 1
                    
                    del questions[0]
                    
                    def r():
                        windowFor1.destroy()
                        right()
                        
                    
                    def w():
                        windowFor1.destroy()
                        wrong()
                        
                    
                    windowFor1 = tk.Tk()
                    windowFor1.geometry("724x592")
            
                    windowFor1.resizable(width=False, height=False)
                    #icon for the window
                    try:
                        windowFor1.iconbitmap('Icon_for_windows.ico')
                        
                    except:
                        time.sleep(0)
                    windowFor1.title("Cyber Security Quiz")#  |
                    PutImageForBackground=Canvas(windowFor1)#                              |
                    #                                                                           |
                    #displays canvas                                                            |
                    PutImageForBackground.grid()#                                               |
                    #                                                                           |
                    #puts image for background onto canvas                                      |
                    image1=PhotoImage(file="blankbg.gif")#                                          |
                    #                                                                           |
                    #keep a link to the image to stop the image being garbage collected         |
                    PutImageForBackground.img=image1#                                           |
                    #                                                                           |
                    #resizes background image                                                   |
                    displayimage = image1.subsample(1, 1)#                                      |
                    #                                                                           |
                    #displays image in background                                               |
                    PutImageForBackground.create_image(400, 300, image=displayimage)#
                                                            
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                                                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    

                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                        
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                                                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()

                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()

                    label = tk.Label(PutImageForBackground, relief='flat', text="\nQ. What name would you give to an email attachment that may harm your computer?\n",bg="#FFFFFF",fg='#000000',cursor = "target")
                    label.pack(side='left', padx = 3, pady=0, anchor='s')
                    backimaget = PhotoImage(file = "C.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimaget.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =w ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #                                                                                                                          |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    
                    backimagey = PhotoImage(file = "3.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimagey.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =w ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #                                                                                                                          |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    
                    backimagew = PhotoImage(file = "2.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimagew.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =r ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    center(windowFor1)
                    windowFor1.mainloop()
                elif questions[0] == "Question 6":
                    
                    question += 1
                    
                    del questions[0]
                    
                    def r():
                        windowFor1.destroy()
                        right()
                        
                    
                    def w():
                        windowFor1.destroy()
                        wrong()
                        
                    
                    windowFor1 = tk.Tk()
                    windowFor1.geometry("724x592")
            
                    windowFor1.resizable(width=False, height=False)
                    #icon for the window
                    try:
                        windowFor1.iconbitmap('Icon_for_windows.ico')
                        
                    except:
                        time.sleep(0)
                    windowFor1.title("Cyber Security Quiz")#  |
                    PutImageForBackground=Canvas(windowFor1)#                              |
                    #                                                                           |
                    #displays canvas                                                            |
                    PutImageForBackground.grid()#                                               |
                    #                                                                           |
                    #puts image for background onto canvas                                      |
                    image1=PhotoImage(file="blankbg.gif")#                                          |
                    #                                                                           |
                    #keep a link to the image to stop the image being garbage collected         |
                    PutImageForBackground.img=image1#                                           |
                    #                                                                           |
                    #resizes background image                                                   |
                    displayimage = image1.subsample(1, 1)#                                      |
                    #                                                                           |
                    #displays image in background                                               |
                    PutImageForBackground.create_image(400, 300, image=displayimage)#
                                                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                                                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                                                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    

                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()

                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                                                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()

                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()

                    label = tk.Label(PutImageForBackground, relief='flat', text="\nQ. Which of these statements is true?\n",bg="#FFFFFF",fg='#000000',cursor = "target")
                    label.pack(side='left', padx = 3, pady=0, anchor='s')
                    backimaget = PhotoImage(file = "C.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimaget.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =r ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #                                                                                                                          |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    
                    backimagey = PhotoImage(file = "3.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimagey.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =w ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #                                                                                                                          |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    
                    backimagew = PhotoImage(file = "2.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimagew.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =w ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    center(windowFor1)
                    windowFor1.mainloop()
                elif questions[0] == "Question 7":
                    
                    question += 1
                    
                    del questions[0]
                    
                    def r():
                        windowFor1.destroy()
                        right()
                        
                    
                    def w():
                        windowFor1.destroy()
                        wrong()
                        
                    
                    windowFor1 = tk.Tk()
                    windowFor1.geometry("724x592")
            
                    windowFor1.resizable(width=False, height=False)
                    #icon for the window
                    try:
                        windowFor1.iconbitmap('Icon_for_windows.ico')
                        
                    except:
                        time.sleep(0)
                    windowFor1.title("Cyber Security Quiz")#  |
                    PutImageForBackground=Canvas(windowFor1)#                              |
                    #                                                                           |
                    #displays canvas                                                            |
                    PutImageForBackground.grid()#                                               |
                    #                                                                           |
                    #puts image for background onto canvas                                      |
                    image1=PhotoImage(file="blankbg.gif")#                                          |
                    #                                                                           |
                    #keep a link to the image to stop the image being garbage collected         |
                    PutImageForBackground.img=image1#                                           |
                    #                                                                           |
                    #resizes background image                                                   |
                    displayimage = image1.subsample(1, 1)#                                      |
                    #                                                                           |
                    #displays image in background                                               |
                    PutImageForBackground.create_image(400, 300, image=displayimage)#
                                                               
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                                                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    

                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                     
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                                                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()

                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()

                    label = tk.Label(PutImageForBackground, relief='flat', text="\nQ. What should you do if you want to meet someone you only know online?\n",bg="#FFFFFF",fg='#000000',cursor = "target")
                    label.pack(side='left', padx = 3, pady=0, anchor='s')
                    backimaget = PhotoImage(file = "C.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimaget.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =w ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #                                                                                                                          |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    
                    backimagey = PhotoImage(file = "3.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimagey.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =r ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #                                                                                                                          |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    
                    backimagew = PhotoImage(file = "2.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimagew.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =w ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    center(windowFor1)
                    windowFor1.mainloop()
                elif questions[0] == "Question 8":
                    
                    question += 1
                    
                    del questions[0]
                    
                    def r():
                        windowFor1.destroy()
                        right()
                        
                    
                    def w():
                        windowFor1.destroy()
                        wrong()
                        
                    
                    windowFor1 = tk.Tk()
                    windowFor1.geometry("724x592")
            
                    windowFor1.resizable(width=False, height=False)
                    #icon for the window
                    try:
                        windowFor1.iconbitmap('Icon_for_windows.ico')
                        
                    except:
                        time.sleep(0)
                    windowFor1.title("Cyber Security Quiz")#  |
                    PutImageForBackground=Canvas(windowFor1)#                              |
                    #                                                                           |
                    #displays canvas                                                            |
                    PutImageForBackground.grid()#                                               |
                    #                                                                           |
                    #puts image for background onto canvas                                      |
                    image1=PhotoImage(file="blankbg.gif")#                                          |
                    #                                                                           |
                    #keep a link to the image to stop the image being garbage collected         |
                    PutImageForBackground.img=image1#                                           |
                    #                                                                           |
                    #resizes background image                                                   |
                    displayimage = image1.subsample(1, 1)#                                      |
                    #                                                                           |
                    #displays image in background                                               |
                    PutImageForBackground.create_image(400, 300, image=displayimage)#
                                                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                                                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                                                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                                                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    

                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()

                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()

                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()

                    label = tk.Label(PutImageForBackground, relief='flat', text="\nQ. Which of these is classed as personal infandmation?\n",bg="#FFFFFF",fg='#000000',cursor = "target")
                    label.pack(side='left', padx = 3, pady=0, anchor='s')
                    backimaget = PhotoImage(file = "C.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimaget.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =r ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #                                                                                                                          |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    
                    backimagey = PhotoImage(file = "3.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimagey.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =w ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #                                                                                                                          |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    
                    backimagew = PhotoImage(file = "2.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimagew.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =w ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    center(windowFor1)
                    windowFor1.mainloop()
                elif questions[0] == "Question 9":
                    
                    question += 1
                    
                    del questions[0]
                    
                    def r():
                        windowFor1.destroy()
                        right()
                        
                    
                    def w():
                        windowFor1.destroy()
                        wrong()
                        
                    
                    windowFor1 = tk.Tk()
                    windowFor1.geometry("724x592")
            
                    windowFor1.resizable(width=False, height=False)
                    #icon for the window
                    try:
                        windowFor1.iconbitmap('Icon_for_windows.ico')
                        
                    except:
                        time.sleep(0)
                    windowFor1.title("Cyber Security Quiz")#  |
                    PutImageForBackground=Canvas(windowFor1)#                              |
                    #                                                                           |
                    #displays canvas                                                            |
                    PutImageForBackground.grid()#                                               |
                    #                                                                           |
                    #puts image for background onto canvas                                      |
                    image1=PhotoImage(file="blankbg.gif")#                                          |
                    #                                                                           |
                    #keep a link to the image to stop the image being garbage collected         |
                    PutImageForBackground.img=image1#                                           |
                    #                                                                           |
                    #resizes background image                                                   |
                    displayimage = image1.subsample(1, 1)#                                      |
                    #                                                                           |
                    #displays image in background                                               |
                    PutImageForBackground.create_image(400, 300, image=displayimage)#
                                                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                                                            
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                                                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    

                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                        
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()

                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()

                    label = tk.Label(PutImageForBackground, relief='flat', text="\nQ. What is the definition of phishing?\n",bg="#FFFFFF",fg='#000000',cursor = "target")
                    label.pack(side='left', padx = 3, pady=0, anchor='s')
                    backimaget = PhotoImage(file = "C.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimaget.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =r ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #                                                                                                                          |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    
                    backimagey = PhotoImage(file = "3.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimagey.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =w ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #                                                                                                                          |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    
                    backimagew = PhotoImage(file = "2.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimagew.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =w ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    center(windowFor1)
                    windowFor1.mainloop()
                elif questions[0] == "Question 10":
                    
                    question += 1
                    
                    del questions[0]
                    
                    def r():
                        windowFor1.destroy()
                        right()
                        
                    
                    def w():
                        windowFor1.destroy()
                        wrong()
                        
                    
                    windowFor1 = tk.Tk()
                    windowFor1.geometry("724x592")
            
                    windowFor1.resizable(width=False, height=False)
                    #icon for the window
                    try:
                        windowFor1.iconbitmap('Icon_for_windows.ico')
                        
                    except:
                        time.sleep(0)
                    windowFor1.title("Cyber Security Quiz")#  |
                    PutImageForBackground=Canvas(windowFor1)#                              |
                    #                                                                           |
                    #displays canvas                                                            |
                    PutImageForBackground.grid()#                                               |
                    #                                                                           |
                    #puts image for background onto canvas                                      |
                    image1=PhotoImage(file="blankbg.gif")#                                          |
                    #                                                                           |
                    #keep a link to the image to stop the image being garbage collected         |
                    PutImageForBackground.img=image1#                                           |
                    #                                                                           |
                    #resizes background image                                                   |
                    displayimage = image1.subsample(1, 1)#                                      |
                    #                                                                           |
                    #displays image in background                                               |
                    PutImageForBackground.create_image(400, 300, image=displayimage)#
                                                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                                                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                                                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                                                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    

                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()

                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()

                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()
                    
                    #creates empty space with varied heights
                    labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                    labelspace.pack()

                    label = tk.Label(PutImageForBackground, relief='flat', text="\nQ. What is the definiton of spyware?\n",bg="#FFFFFF",fg='#000000',cursor = "target")
                    label.pack(side='left', padx = 3, pady=0, anchor='s')
                    backimaget = PhotoImage(file = "C.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimaget.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =r ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #                                                                                                                          |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    
                    backimagey = PhotoImage(file = "3.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimagey.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =w ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #                                                                                                                          |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    
                    backimagew = PhotoImage(file = "2.gif")#                                                                         |
                    #resizes background image                                                                                                  |
                    backimagee = backimagew.subsample(2, 2)               #                                                                     |
                    Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =w ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                    #placing button on window                                                                                                  |
                    Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                    Button.image= backimagee#
                    center(windowFor1)
                    windowFor1.mainloop()
                
                
            def end():
                
                windowFor2 = tk.Tk()
                windowFor2.geometry("724x592")
            
                windowFor2.resizable(width=False, height=False)
                #icon for the window
                try:
                    windowFor2.iconbitmap('Icon_for_windows.ico')
                    
                except:
                    time.sleep(0)
                windowFor2.title("Cyber Security Quiz")#  |
                PutImageForBackground=Canvas(windowFor2)#                              |
                #                                                                           |
                #displays canvas                                                            |
                PutImageForBackground.grid()#                                               |
                #                                                                           |
                #puts image for background onto canvas                                      |
                image1=PhotoImage(file="blankbg.gif")#                                          |
                #                                                                           |
                #keep a link to the image to stop the image being garbage collected         |
                PutImageForBackground.img=image1#                                           |
                #                                                                           |
                #resizes background image                                                   |
                displayimage = image1.subsample(1, 1)#                                      |
                #                                                                           |
                #displays image in background                                               |
                PutImageForBackground.create_image(400, 300, image=displayimage)#
                                            
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                                            
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                                            
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                                            
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                

                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()

                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()

                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
                labelspace.pack()

                #creates empty space with varied heights
                k = str(Counter.counts)
                k = k[:-1]
                k = k[10:]
                score = int(k)
                if score <5:
                    level = 'You got a level 1'
                elif score <7:
                    level = 'You got a level 2'
                elif score < 9:
                    level = 'You got a level 3'
                elif score == 10:
                    level = 'You got a level 4'
                else:
                    print('Error creating score')
                    sys.exit(0)
                def r():
                    windowFor2.destroy()
                    exit_program()
                score = name+', you got '+str(score)+' out of 10'
                
                labelspace = tk.Label(PutImageForBackground, text=score,background='white',font=("calibri", 12), justify=LEFT, fg = '#000000')
                labelspace.pack()
                
                #creates empty space with varied heights
                labelspace = tk.Label(PutImageForBackground, text=level,background='white',font=("calibri", 12), justify=LEFT, fg = '#000000')
                labelspace.pack()
                
                  
                backimaget = PhotoImage(file = "C.gif")#                                                                         |
                #resizes background image                                                                                                  |
                backimagee = backimaget.subsample(2, 2)               #                                                                     |
                Button = tk.Button(PutImageForBackground, relief='flat', image=backimagee, command =r ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
                #                                                                                                                          |
                #placing button on window                                                                                                  |
                Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
                Button.image= backimagee#
                center(windowFor2)
                windowFor2.mainloop()
            end()
        
   

                
        Cont()            
            
        InstrWin = tk.Tk()
        InstrWin.title("Cyber Security Quiz")#  |
              #creates a canvas to put the image on                                       |
        PutImageForBackground=Canvas(InstrWin)#                              |
        #                                                                           |
        #displays canvas                                                            |
        PutImageForBackground.grid()#                                               |
        #                                                                           |
        #puts image for background onto canvas                                      |
        image1=PhotoImage(file="blankbg.gif")#                                          |
        #                                                                           |
        #keep a link to the image to stop the image being garbage collected         |
        PutImageForBackground.img=image1#                                           |
        #                                                                           |
        #resizes background image                                                   |
        displayimage = image1.subsample(1, 1)#                                      |
        #                                                                           |
        #displays image in background                                               |
        PutImageForBackground.create_image(400, 300, image=displayimage)#           |
        ##
    
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',font=("calibri", 12), justify=LEFT)
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',font=("calibri", 12), justify=LEFT)
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',font=("calibri", 12),cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()
        
        #creates empty space with varied heights
        labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
        labelspace.pack()

        backimagre = PhotoImage(file = "C.gif")#                                                                         |
        #resizes background image                                                                                                  |
        backimagere = backimagre.subsample(2, 2)               #                                                                     |
        Button = tk.Button(PutImageForBackground, relief='flat', image=backimagere, command=Cont, bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
        #                                                                                                                          |
        #placing button on window                                                                                                  |
        Button.pack(side='left', padx = 3, pady=0)#                                                                    |
        Button.image= backimagere#
        InstrWin.mainloop()
        
    #puts the window in front of the others
    window_for_menu.attributes('-topmost', False)
    
    #creates a canvas to put the image on
    PutImageForBackground=Canvas(window_for_menu)
    
    #displays canvas
    PutImageForBackground.grid()
    
    #puts image for background onto canvas
    image1=PhotoImage(file="new.gif")
    
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

            #runs the settings
            self.init_window()
    
        #Creation of init_window
        def init_window(self):
            
#       -----------------------------------------------------

            #icon for the window
            try:
                self.master.iconbitmap('Icon_for_windows.ico')
                
            except:
                time.sleep(0)
                
            #changing the title of the window      
            self.master.title("Cyber Security Quiz")
            
            # window size created
#       -----------------------------------------------------

            self.master.geometry("724x592")
            
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
                fname = "Bye.gif"
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
                    mainWindow.iconbitmap('Icon_for_windows.ico')
                except:
                    time.sleep(0)

                    #can't resize window
                mainWindow.resizable(width=False, height=False)
                
                #creates enter rle button
                backimage = tk.PhotoImage(file="goodBYE.gif")

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

          #functions to load other functions
            def Qs():
                global name
                name = entry.get()
                if name.isalpha() != True:
                    window_for_menu.destroy()
                    notalpha()
                else:
                    window_for_menu.destroy()
                    Qss()
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
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")
            
            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")

            
#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

            #checks if buttons are pressed
            button_flag = True
            #text entry field                                                                                            |
            imag = tk.PhotoImage(file="entry.gif")#                                                                      |
            #                                                                                                            |
            # create a frame and pack it                                                                                 |
            frame2 = tk.Frame(PutImageForBackground,bg='#FFFFFF',padx=50)#                                                              |
            frame2.grid(sticky=tk.W)#                                                                                                                                                                |
            #                                                                                                            |
            #makes the image smaller (by subsampling)                                                                    |
            imagee = imag.subsample(3, 3)#                                                                               |
            s = tk.Label(frame2, borderwidth=1, image=imagee, bg = '#FFFFFF')#                                           |
            #                                                                                                            |
            #places the image behind the entry field                                                                     |
            s.grid(column = 1, row = 20)#                                                                                |
            s.image = imagee#                                                                                            |
            #                                                                                                            |
            #creartes a entry field that only allows integers to be entered                                              |
            #(uses a class that I defined above)                                                                         |
            #                                                                                                            |
            entry = Entry(frame2,width = 20,bg = '#FFFFFF',relief = 'flat',font=('Consolas',18), fg = 'SteelBlue1')#     |
            entry.grid(column = 1, row = 20)#     
            # create frame
            frame1 = tk.Frame(PutImageForBackground,bg='#FFFFFF',padx=50)
            frame1.grid(sticky=tk.W)
            
#       -----------------------------------------------------

            #creates enter rle button
            Quitimager = tk.PhotoImage(file="C.gif")
            
            #resizes background image
            Quitimageeb = Quitimager.subsample(3, 3)
            
            #creates quit button
            b = tk.Button(frame1, image=Quitimageeb, bg="#FFFFFF",fg='#FFFFFF',relief=FLAT,cursor = "target",command=Qs)
            
            b.grid(sticky="w")
            b.image = Quitimageeb
            ##############################

            #creates enter rle button
            Quitimage = tk.PhotoImage(file="5.gif")
            
            #resizes background image
            Quitimagee = Quitimage.subsample(3, 3)
            
            #creates quit button
            QuitButton = tk.Button(frame1, image=Quitimagee, bg="#FFFFFF",fg='#FFFFFF',relief=FLAT,cursor = "target",command=exit_program)
            
            QuitButton.grid(sticky="w")
            QuitButton.image = Quitimagee

#       -----------------------------------------------------

            #creates enter rle button
            AQAimage = tk.PhotoImage(file="AQA.gif")
            
            #resizes background image
            AQAimagee = AQAimage.subsample(2, 2)
            
            
#       -----------------------------------------------------


            #puts my name on the program
            Name = tk.Button(PutImageForBackground,image = AQAimagee, text="Program By Faeq Faisal ",bg='#81D3E0',fg="#FFFFFF",font=("Segoe UI Emoji",10),relief=FLAT,cursor = "trek")
            Name.grid(sticky="e")
            Name.image = AQAimagee

            
#       -----------------------------------------------------


            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")


            #image for text
            image = tk.PhotoImage(file="r.gif")
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
#
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
