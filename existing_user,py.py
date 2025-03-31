from tkinter import *
from tkinter import font
from tkinter import messagebox
import re

window = Tk()
window.title("Sign in")
window.geometry("1000x600")
window.config(background="white")

#name
def is_valid_name(name):
    return bool(re.match(r'^[A-Za-z\s]+$', name))

def is_valid_ID(ID):
    return ID.isdigit()

def onclick():
    name = name_entry.get().strip()
    ID = id_entry.get().strip()

    if not name or not ID:
        messagebox.showerror("Incomplete details","Please fill all the Fields!")
        return

    if not is_valid_name(name):
        messagebox.showerror("Invalid Name", "Invalid Name! Please Enter a valid Name.")
        return

    if not is_valid_ID(ID):
        messagebox.showerror("Invalid ID","Please Enter a Valid ID!")
        return
    
try:
    login_img = PhotoImage(file = "rsz_signin.png")
    Label(window, image = login_img,bg = "white").place(x = 80, y =65)
except Exception as e:
    print(f"Error loading image: {e}")

custom_font = font.Font(family="Poppins", size=30)
custom_font1 = font.Font(family="Poppins", size=20)
custom_font2 = font.Font(family="Poppins", size=15)
custom_font3 = font.Font(family="Poppins", size=10)
    
#labels and entries
heading = Label(text = "Sign In", bg = "white", font = custom_font1,fg = "blue")
heading.place(x=648,y=100)

name_text = Label(window,text = "Enter Your Name:", bg = "white", font = custom_font1)
name_text.place(x = 650, y = 180)

name_entry = Entry(window,width=22, border=2, fg="black", font = custom_font2)
name_entry.place(x=650, y = 220)

ID_label = Label(window,text = "Enter Customer Id:", bg = "white", font = custom_font1)
ID_label.place(x = 650, y = 295)

id_entry = Entry(window, width=22, border=2, fg="black", font = custom_font2)
id_entry.place(x=650, y = 340)

submit_button = Button(window,text = "Submit",font = (25) ,width = 6,height = 2,relief = RAISED,command = onclick,fg = "teal")
submit_button.place(x=650,y=410)

window.mainloop()
