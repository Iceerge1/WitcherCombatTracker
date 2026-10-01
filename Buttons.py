import tkinter as tk
from tkinter import ttk

list_box_elements = []

# Adds element 'a' & 'b' to given Listbox
def Add_To_Listbox(listbox, a, b):
    if ((a != "") and (b != "")):
        list_box_elements.append((a, b))
        list_box_elements.sort(key=lambda tup: int(tup[1]), reverse=True)
        listbox.delete(0, "end")
        for item in list_box_elements:
            listbox.insert("end", f"{item[0]}     |     {item[1]}")


def sortlist(listbox):
    data = []
    i = 0
    for item in listbox.get(0, "end"):
        data[i] = item
        item.delete(i)
        i += 1
    data.sort(key=lambda tup: tup[1])

# Remove element at index 'index' from listbox
def Remove_From_Listbox(listbox, index):
    listbox.delete(index)
    del(list_box_elements[index])

# Finds clicked listbox element
def on_item_click(event):
    listbox = event.widget
    index = listbox.nearest(event.y)
    
    if listbox.size() == 0:
        return

    bbox = listbox.bbox(index)
    
    if bbox:
        y_top = bbox[1]
        y_bottom = y_top + bbox[3]
        
        if y_top <= event.y <= y_bottom:
            Remove_From_Listbox(listbox, index)


def create_popup(root, popup_width, popup_height):
    parent_x = root.winfo_x()
    parent_y = root.winfo_y()
    parent_width = root.winfo_width()
    parent_height = root.winfo_height()
    center_x = parent_x + (parent_width // 2) - (popup_width // 2)
    center_y = parent_y + (parent_height // 2) - (popup_height // 2)

    popup = tk.Toplevel(root)
    popup.geometry(f"{popup_width}x{popup_height}+{center_x}+{center_y}")
    return popup

# Adds users input to given listbox
def Add_Initiative(root, listbox):
    # Set Popup in the middle of main window
    popup = create_popup(root, 300, 200)
    popup.title("Add Initiative")

    # Popup Content (Label, Input fields, Cancel & Add Buttons)
    pop_frame = tk.Frame(popup)
    pop_frame.pack(padx=50, pady=15, anchor="center")
    pop_label1 = tk.Label(pop_frame, text="Enemy:")
    pop_entry1 = tk.Entry(pop_frame)
    pop_label1.pack(anchor="w")
    pop_entry1.pack(anchor="w")
    pop_label2 = tk.Label(pop_frame, text="Initiative:")
    pop_entry2 = tk.Entry(pop_frame)
    pop_label2.pack(anchor="w")
    pop_entry2.pack(anchor="w")
    pop_canc_btn = tk.Button(popup, text="Cancel", command=popup.destroy)
    pop_ok_btn = tk.Button(popup, text="Add", command=lambda: (Add_To_Listbox(listbox, pop_entry1.get(), pop_entry2.get()), popup.destroy()))
    pop_canc_btn.pack(side="left", anchor="w", padx=(50, 0), pady=(0, 10))
    pop_ok_btn.pack(side="right", anchor="e", padx=(0, 50), pady=(0, 10))

def Add_Enemy(root, left_frame):
   # popup = create_popup(root, 600, 400)
    #popup.title("Add Enemy")

    create_card(left_frame)

def create_card(left_frame):
    frame = tk.Frame(left_frame, bg="white", height=60, width=60)
    frame.pack()