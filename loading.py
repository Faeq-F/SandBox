import tkinter as tk
from time import sleep

def task():
    # The window will stay open until this function call ends.
    for i in range(100):
        print(i)# Replace this with the code you want to run
    root.destroy()

root = tk.Tk()
root.title("Example")

label = tk.Label(root, text="Waiting for task to finish.")
label.pack()

root.after(200, task)
root.mainloop()

print("Main loop is now over and we can do other stuff.")
