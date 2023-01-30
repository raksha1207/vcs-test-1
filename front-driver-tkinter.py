from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Item")
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=editMenu)

    def exitProgram(self):
        exit()
        
root = Tk()
app = Window(root)
root.wm_title("Tkinter window")
root.mainloop()



root = Tk()
app = Window(root)
The window class is not standard, we create a Window. This class in itself is pretty basic.

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
Then set the window title and show the window:

# set window title
root.wm_title("Tkinter window")

# show window
root.mainloop()
