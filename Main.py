from tkinter import *
import tkinter as tk
from tkinter import ttk
from Buttons import Add_To_Listbox, Remove_From_Listbox, on_item_click

root = Tk()
root.title("The Witcher Combatsupport")

# Determine window size & position
swidth, sheight = root.winfo_screenwidth(), root.winfo_screenheight()
wwidth,wheigth = 1280, 800
wposwidth, wposheight = (swidth // 2) - (wwidth // 2), (sheight // 2) - (wheigth // 2)
root.geometry(f"1280x800+{wposwidth}+{wposheight}")
root.minsize(1024, 720)

# 2. Unterer Bereich (Bottom Log / Details)
bottom_frame = tk.Frame(root, bg="#1e1e1e", height=180)
bottom_frame.pack(side="bottom", fill="x", padx=10, pady=(5, 10))
bottom_frame.pack_propagate(False) # Hält die Höhe konstant

# 3. Oberer Container (für Links + Rechts)
top_container = tk.Frame(root)
top_container.pack(side="top", fill="both", expand=True, padx=10, pady=(10, 5))

# Right side (for buttons)
right_frame = tk.Frame(top_container, bg="#252526", width=260)
right_frame.pack(side="right", fill="y", padx=(5, 0))
right_frame.pack_propagate(False)

# Load & Save:
load_btn = tk.Button(right_frame, text="Load Setup", width=25)
load_btn.pack(pady=(15, 7))
save_btn = tk.Button(right_frame, text="Save Setup", width=25)
save_btn.pack(pady=(7, 15))

# New Enemy & Add Enemy:
add_enemy_btn = tk.Button(right_frame, text="Add Enemy", width=25)
new_enemy_btn = tk.Button(right_frame, text="New Enemy", width=25)
add_enemy_btn.pack(pady=(15,7))
new_enemy_btn.pack(pady=(7,30))

# Initiative Box:
ini_frame = tk.Frame(right_frame, bg="black")
ini_frame.pack(fill=tk.X, padx= 15)

ini_inner_frame = tk.Frame(ini_frame)
ini_label = tk.Label(ini_inner_frame, text="Initiative:", font=("Arial", 12, "bold"), anchor="center")
ini_label.pack(side="left", padx=(5, 0))
ini_add_btn = tk.Button(ini_inner_frame, text="Add", command=lambda: Add_To_Listbox(ini_listbox, "Nekker", 14))
ini_add_btn.pack(side="right")
ini_inner_frame.pack(fill=X)

ini_listbox = tk.Listbox(ini_frame, height=15, selectmode="single")
ini_listbox.pack(side="bottom", pady=(0, 15), fill=tk.X)
ini_listbox.bind("<<ListboxSelect>>", on_item_click)

# 5. Linker Bereich für das Gegner-Raster
left_frame = tk.Frame(top_container, bg="#2d2d2d")
left_frame.pack(side="left", fill="both", expand=True, padx=(0, 5))
root.mainloop()