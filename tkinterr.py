
#-----------------------------------------------------------------------------------------------#
#Importing                                                                                      |
#                                                                                               |
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
#allows me to check the screen resolution being used by the user and                                          |
#modify the look of the proram according to what the screen can support                                       |
import ctype#                                                                                                 |
#                                                                                                             |
#                                                                                                             |
#allows me to manipulate os (mostly used for checking if things exist)                                        |
import os #                                                                                                   |
#                                                                                                             |
#                                                                                                             |
#used for the program to pass errors that would fail the program when on different operating systems          |
import time   #                                                                                               |
#-------------------------------------------------------------------------------------------------------------#
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
    @Counter.count##                                                                                          |
    def right():##                                                                                            |
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
#------------------------------#------------------------------------------------------------------------------#
#                              |
#creates window                |
window_for_menu = tk.Tk()#     |
#------------------------------#------------------------------------------------------------------------------#
#                                                                                                             |
#takes entryfield as argument                                                                                 |
class integersOnly(tk.Entry):#                                                                                |
#                                                                                                             |
    #creates entry field#                                                                                     |
def __init__(self, master=None, **kwargs):#                                                                   |
#                                                                                                             |
        #takes the entry as a string#                                                                         |
        self.var = tk.StringVar()#                                                                            |
#                                                                                                             |
        #creates the field                                                                                    |
        tk.Entry.__init__(self, master, textvariable=self.var, **kwargs)#                                     |
#                                                                                                             |
        #empty string for characters other than integers to be replaced with                                  |
        self.old_value = ''                                     #                                             |
#                                                                                                             |
        #checks integers                                                                                      |
        self.var.trace('w', self.check)#                                                                      |
#                                                                                                             |
        #replaces characters other than integers                                                              |
        self.get, self.set = self.var.get, self.var.set#                                                      |
#                                                                                                             |
    #function to check that only integers are left                                                            |
    def check(self, *args):#                                                                                  |
#                                                                                                             |
        #check if it is a integer                                                                             |
        if self.get().isdigit():#                                                                             |
#                                                                                                             |
            #the current value is only digits; allow this                                                     |
            self.old_value = self.get()#                                                                      |
#                                                                                                             |
        #no integer?                                                                                          |
        else:#                                                                                                |
#                                                                                                             |
            # there's non-digit characters in the input; reject this                                          |
            self.set(self.old_value) #                                                                        |
#-------------------------------------------------------------------------------------------------------------#
#                                                                                                             |
#canvas to show bg image    #                                                                                 |    
C = Canvas(mainWindow)#                                                                                       |
backg = PhotoImage(file = "ERd.gif")#                                                                         |
#                                                                                                             |
#placing the bg image on window#                                                                              |
background_label = Label(mainWindow, image=backg)#                                                            |
background_label.place(x=0, y=0, relwidth=1, relheight=1)#                                                    |
#                                                                                                             |
#reference back to bg image#                                                                                  |
C.grid()#                                                                                                     |
C.img = backg#                                                                                                |
#-----------------------------------------#-------------------------------------------------------------------#
#getting the value from the entry field   |
number = e.get()#                         |
#-----------------------------------------#
#closes window                            |
mainWindow.destroy()#                     |
#-----------------------------------------#--------------#
#window's title                                          |
error_window.title("ASCII art program by Faeq Faisal")#  |
#--------------------------------------------------------#---------#
#window's icon                                                     |
try:  #                                                            |
    error_window.iconbitmap('Icon_for_windows.ico') #              |
#                                                                  |
# if using linux (eg. ubuntu or mac os), the process is            |
#skipped as the os does not support icons in the title bar         |
#                                                                  |
except:          #                                                 |
    time.sleep(0)#                                                 |
#-------------------------------------------------------------#----#
#                                              #              |
#image file for bg                             #              |
fname = "NoClosing.gif.gif"#                                  |
bg_image = tk.PhotoImage(file=fname)#                         |
#                                                             |
# get the width and height of the image#                      |
w = bg_image.width()#                                         |
h = bg_image.height()#                                        |
#                                                             |
# size the window so the image will fill it#                  | 
mainWindow.geometry('724x592')#                               |
#                                                             |
#canvas to use bg image#                                      |
cv = tk.Canvas(width=w, height=h)#                            |
cv.pack(side='top', fill='both', expand='yes')#               |
#                                                             |
#putting the image in the north west corner#                  |
cv.create_image(0, 0, image=bg_image, anchor='nw')#           |
cv.create_text(15, 20, text="", fill="red", anchor='nw')#     |
#------------------------------------------------#------------#
#user can't resize window                        |
mainWindow.resizable(width=False, height=False)# |
#------------------------------------------#-----#
#puts the window in front of the menu      |
mainWindow.attributes('-topmost', True)#   |
#-----------------------------------#------#
#does not allow window to be moved  |
mainWindow.overrideredirect(True)#  |
#-----------------------------------#--------------------------------------------------------------------------------------#
#resizes background image                                                                                                  |
backimagee = backimage.subsample(2, 2)               #                                                                     |
Button = tk.Button(cv, relief='flat', image=backimagee, command =noclose ,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")#    |
#                                                                                                                          |
#placing button on window                                                                                                  |
Button.pack(side='left', padx = 3, pady=0, anchor='s')#                                                                    |
Button.image= backimagee#                                                                                                  |
#------------------------#-------------------------------------------------------------------------------------------------#
#running the window      |
center(mainWindow)#      |
mainWindow.mainloop()#   |
#------------------------#-------------------------------------------#
#overides the close button ( 'X' button) to run the function above   |
error_window.protocol("WM_DELETE_WINDOW", on_closing)#               |
#---------------------------------------------------------#----------#
#frame for the bg image                                   |
F1=Frame(error_window)#                                   |
F1=Frame(error_window,width=400,height=450)#              |
                                        #                 |
#placing the frame on the window                          |
F1.place(height=7000, width=4000, x=100, y=100)#          |
F1.grid(columnspan=10,rowspan=10)#                        |
#                                                         |
#configuring the placement of the frame on the window     |
F1.grid_rowconfigure(0,weight=1)#                         |
F1.grid_columnconfigure(0,weight=1)#                      |
#---------------------------------------------------------#--------------------------------------------------#
#image for bg                                                                                                |
photo=PhotoImage(file="errorLines.gif")#                                                                     |
label = Label(error_window,image = photo)#                                                                   |
#                                                                                                            |
label.image = photo # keep a reference                                                                       |
label.grid(row=0,column=0,columnspan=20,rowspan=20)#                                                         |
#                                                                                                            |
#text entry field                                                                                            |
imag = tk.PhotoImage(file="entry.gif")#                                                                      |
#                                                                                                            |
# create a frame and pack it                                                                                 |
frame2 = tk.Frame(window,bg='#FFFFFF',padx=15)#                                                              |
frame2.grid()#                                                                                               |
#                                                                                                            |
#makes the image smaller (by subsampling)                                                                    |
imagee = imag.subsample(3, 3)#                                                                               |
s = tk.Label(frame2, borderwidth=1, image=imagee, bg = '#FFFFFF')#                                           |
#                                                                                                            |
#places the image behind the entry field                                                                     |
s.grid(column = 2, row = 20)#                                                                                |
s.image = imagee#                                                                                            |
#                                                                                                            |
#creartes a entry field that only allows integers to be entered                                              |
#(uses a class that I defined above)                                                                         |
#                                                                                                            |
entry = Entry(frame2,width = 20,bg = '#FFFFFF',relief = 'flat',font=('Consolas',18), fg = 'SteelBlue1')#     |
entry.grid(column = 2, row = 20)#                                                                            |
#---------------------------------------------------------------------------------------------#--------------#
#                                                                                             |
#during the window being shown, itr checks if it is still                                     |
#active to stop more windows from going over them                                             |
while True:#                                                                                  |
#                                                                                             |
#try and except is used as the user can close the window at any time,                         |
#and when they do, I want to not get a defining error                                         |
try:#                                                                                         |
#                                                                                             |
    #'checks if the window is running                                                         |
    if 'normal' == window.state():#                                                           |
#                                                                                             |
        #if it is, the program does nothing                                                   |
        time.sleep(0)#                                                                        |
#                                                                                             |
#if the window is no longer running, the check variable is updated and the loop is broken     |
except:#                                                                                      |
#                                                                                             |
    #check is updated                                                                         |
    check = check + 1#                                                                        |
    break#                                                                                    |
#---------------------------------------------------------------------------------------------#--------------------------------------------------#
#checks if file exists                                                                                                                           |
if os.path.exists(enterredfilename) == True:#                                                                                                    |
#                                                                                                                                                |
#opens the file, if it does not exist, it will create the file, and write to it with nothing meaning that it is erased of previous content       |
open(textfile,"w+").close()#                                                                                                                     |
#                                                                                                                                                |
#opens file                                                                                                                                      |
openfile=open(file)#                                                                                                                             |
#-------------------------------------------------------------------------------------------------#----------------------------------------------#
 #importing filedialog in local scope to make function work                                       |
try:#                                                                                             |
    from tkinter import filedialog#                                                               |
    #python 2 is below                                                                            |
except:#                                                                                          |
    from Tkinter import tkFileDialog#                                                             |
#                                                                                                 |
    #function to browse for file                                                                  |
def browse():#                                                                                    |
    #                                                                                             |
    #opens file dialog and lets user to browse for file                                           |
    Convert_rle.filename =  filedialog.askopenfilename(filetypes=(('text files', 'txt'),))#       |
#                                                                                                 |
    # asigns the file location to the variable                                                    |
    file = Convert_rle.filename#                                                                  |
#                                                                                                 |
    #runs the function to load the art through the browse function                                |
    CcompressData()#                                                                              |
#---------------------------------------------------------------#---------------------------------#
#                                                               |
    #overides the close button                                  |
    window_for_menu.protocol("WM_DELETE_WINDOW", on_closing)#   |
    #                                                           |
    #puts the window in front of the others                     |
    window_for_menu.attributes('-topmost', False)#              |
#---------------------------------------------------------------#---------------#
    #creates a canvas to put the image on                                       |
    PutImageForBackground=Canvas(window_for_menu)#                              |
    #                                                                           |
    #displays canvas                                                            |
    PutImageForBackground.grid()#                                               |
    #                                                                           |
    #puts image for background onto canvas                                      |
    image1=PhotoImage(file="new.gif")#                                          |
    #                                                                           |
    #keep a link to the image to stop the image being garbage collected         |
    PutImageForBackground.img=image1#                                           |
    #                                                                           |
    #resizes background image                                                   |
    displayimage = image1.subsample(1, 1)#                                      |
    #                                                                           |
    #displays image in background                                               |
    PutImageForBackground.create_image(400, 300, image=displayimage)#           |
#                                                                               |
    #                                                                           |
#-------------------------------------------------------------------------------#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


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
            self.master.title("ASCII art program by Faeq Faisal")
            
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

                
           

            #function to load the next functions
            def Convert_rle_window():
                
                #destroys the window for the menu
                window_for_menu.destroy()
                
                #loads the option that was selected by the user
                Convert_Rle()

#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
                

            #creates empty space with varied heights
            labelspace = tk.Label(PutImageForBackground, text="",background='white',cursor = "trek")
            labelspace.grid(sticky="w")

            
#________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

            #checks if buttons are pressed
            button_flag = True

            # create frame
            frame1 = tk.Frame(PutImageForBackground,bg='#FFFFFF',padx=109)
            frame1.grid(sticky=tk.W)

#       -----------------------------------------------------

            #creates enter rle button
            imagetobeused = tk.PhotoImage(file="1.gif")

            #resizes background image
            imagetobeusede = imagetobeused.subsample(3, 3)
            Button = tk.Button(frame1, relief=FLAT, image=imagetobeusede, command =Load_RLE_window,bg="#FFFFFF",fg='#FFFFFF',cursor = "target")

            #places button on bg
            Button.grid()
            Button.image = imagetobeusede

   

#       -----------------------------------------------------

            #creates enter rle button
            AQAimage = tk.PhotoImage(file="AQA.gif")
            
            #resizes background image
            AQAimagee = AQAimage.subsample(2, 2)
            
            
#       -----------------------------------------------------


            #puts my name on the program
            Name = tk.Button(PutImageForBackground,image = AQAimagee, command=Load_About_window, text="Program By Faeq Faisal ",bg='#81D3E0',fg="#FFFFFF",font=("Segoe UI Emoji",10),relief=FLAT,cursor = "trek")
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
#running function
menu()
