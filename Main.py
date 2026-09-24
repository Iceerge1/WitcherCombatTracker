from tkinter import *
import tkinter as tk
from tkinter import ttk

root = Tk()
root.title("The Witcher Combatsupport")

# Determine window size & position
swidth, sheight = root.winfo_screenwidth(), root.winfo_screenheight()
wwidth,wheigth = 600, 400
wposwidth, wposheight = (swidth // 2) - (wwidth // 2), (sheight // 2) - (wheigth // 2)
root.geometry(f"600x400+{wposwidth}+{wposheight}")


mainframe = tk.Frame(root, bg="grey")
root.mainloop()