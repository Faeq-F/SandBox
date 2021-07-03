from tkinter import *
from tkinter.filedialog import askopenfilename


def loadTable():
    filename = askopenfilename(filetypes=[("allfiles","*")])
def addCourse():
    print("Insert functionality here")
def addTime():
    print("Insert functionality here")
def resetTable():
    print("Insert functionality here")
def addComment():
    print("Insert functionality here")
def viewTable():
    print("Insert functionality here")


class menu():
    app = Tk()
    app.geometry("800x600+200+200")
    app.title("Time Tracker")
    #load the buttons for UI
    bLoad = Button(app, text = "Load Table", command = loadTable())
    bCourse = Button(app, text = "Add Course", command = addCourse())
    bTime = Button(app, text = "Add Time", command = addTime())
    bReset = Button(app, text = "Reset Time", command = resetTable())
    bComment = Button(app, text = "Add Comment", command = addComment())
    bView = Button(app, text = "View Table", command = viewTable())
    bLoad.pack(side="top", anchor = "w", padx=15, pady=35)
    bCourse.pack(side="top", anchor = "w", padx=15, pady=35)
    bTime.pack(side="top", anchor = "w", padx=15, pady=35)
    bReset.pack(side="top", anchor = "w", padx=15, pady=35)
    bComment.pack(side="top", anchor = "w",  padx=15, pady=35)
    bView.pack(side="top", anchor = "w", padx=15, pady=35)

if __name__ == '__main__':
    mainloop()
