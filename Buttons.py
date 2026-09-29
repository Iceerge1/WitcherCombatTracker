import tkinter as tk
from tkinter import ttk

# Adds element 'a' & 'b' to given Listbox
def Add_To_Listbox(listbox, a, b):
    listbox.insert("end", f"{a}     |     {b}")

def Remove_From_Listbox(listbox, index):
    listbox.delete(index)

def on_item_click(event):
    listbox = event.widget
    selection = listbox.curselection()
    
    if selection:
        index = selection[0]
        Remove_From_Listbox(listbox, index)