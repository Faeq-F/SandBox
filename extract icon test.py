
import os
import sys
import subprocess
dir = "H:\\Computer Resources\\PortableApps\\"
#extracting icons
'''
#allows program to run with administrative privelages
from elevate import elevate
elevate(show_console=False)



i = "H:\\Computer Resources\\PortableApps\\BootSafe\\BootSafe.exe"

#gets the icons from every program executable needed
command = dir+"Launcher\\BatchIconExtractor.exe  \""+i+"\""
p12 = subprocess.Popen(command, shell=False)

'''
#displaying icons
from tkinter import *
import PIL
import time




icons = []
item = 'blender'
root = Tk()
root.geometry('1000x1000')
for r, d, f in os.walk(dir + "Launcher\\icons\\"):
    for file in f:
        #checks if the file is executable
        if '.ico' in file:
            #adds executable to list
            icons.append(file)
        else:
            #skips if not an executable
            time.sleep(0)
possibleimage = [s for s in icons if item.lower() in s.lower()]
try:
    from PIL import Image, ImageTk
    imagetouse = possibleimage[0]
    pilImage = Image.open(dir + "Launcher\\icons\\"+imagetouse)
    image = ImageTk.PhotoImage(pilImage)
    #image = Image.open(dir +"Launcher\\icons\\"+imagetouse)
    #imagetobeusedonbutton = ImageTk.PhotoImage(image)
    button = Button(root, image=image, relief=FLAT,
                    bg='#FFFFFF', fg='#6EA3DE')
    button.grid(column = 1, sticky=W)    
    button.image = image
except:
    time.sleep(0)

root.mainloop()
