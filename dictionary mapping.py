import tkinter as tk
import os
import pyglet
import time
import pickle

#gets working directory
directory = os.getcwd()
#redirects to directory with portable apps
directory = directory + "Computer Resources\\PortableApps\\"

pyglet.font.add_file(directory+"Launcher\\Phenomena-Regular.ttf")
#function to update executable list


with open(directory+"Launcher\\executableList.txt", 'rb') as fp:
    executables = pickle.load(fp)
    
class Example(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.label = tk.Label(self)
        self.selection = tk.Listbox(self, width=40)

        self.label.pack(side="top", fill="x", expand=False)
        self.selection.pack(side="top", fill="both", expand=True)
        self.data = {}
        
        for i in executables:
            itemname = i[0]
            path = i[1]
            self.data.update({itemname: path})
            self.selection.insert("end", itemname)
        
        

        self.selection.bind("<<ListboxSelect>>", self.on_listbox_select)

    def on_listbox_select(self, event):
        i = self.selection.curselection()[0]
        text = self.selection.get(i)
        self.label.configure(text="%s" % (self.data[text]))

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
