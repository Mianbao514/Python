from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


# Define Class
class MyGame:
    def __init__(self, master):
        self.master = master

# Initialize window
root = tk.Tk()
root.title("Game")
root.geometry('1536x864')

# style
style = ttk.Style()

# set bg image
Bg_image = Image.open("bg2.png").resize((1536, 864))  # Resize
Bg_photo = ImageTk.PhotoImage(Bg_image)

bg_label = tk.Label(root, image=Bg_photo)  
bg_label.place(x=0, y=0, relwidth=1, relheight=1)  

# set logo
logo_image = Image.open("Logo_2.0.png").resize((309, 119))
logo_photo = ImageTk.PhotoImage(logo_image)

logo_label = tk.Label(root, image = logo_photo)
logo_label.place(x=618, y=50)

# Load btn image
button_image = Image.open("ButtonFrame.png").resize((300, 100))  
button_photo = ImageTk.PhotoImage(button_image)

# load btn hover image
button_hover_image = Image.open("ButtonFrame1.png").resize((300, 100))
button_hover_photo = ImageTk.PhotoImage(button_hover_image)

# Button 1
btn1 = ttk.Button(root, image=button_photo, compound="center", command=lambda: print("Start Game"))
btn1.configure( text="Start", compound="center")
btn1.place(x=618, y=300)  
btn1.bind('<Enter>', lambda e: btn1.configure(image=button_hover_photo))
btn1.bind('<Leave>', lambda e : btn1.configure(image= button_photo))

# Button 2
btn2 = ttk.Button(root, image=button_photo, compound="center", command=lambda: print("Language"))
btn2.configure(text="Language")
btn2.place(x=618, y=420) 
btn2.bind('<Enter>', lambda e: btn2.configure(image=button_hover_photo))
btn2.bind('<Leave>', lambda e: btn2.configure(image= button_photo))

# Run game
game = MyGame(root)

root.mainloop()
