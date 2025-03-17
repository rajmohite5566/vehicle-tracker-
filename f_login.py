from tkinter import *
from tkinter import messagebox
from tkinter import font


new_window = None

def click():
    global new_window
    
    
    if new_window is None or not new_window.winfo_exists():  
       
        new_window = Toplevel(window)
        new_window.title("Next Window")



window = Tk()
#new_window = Tk()

window.geometry("1000x600")
window.title("Vehicle Maintainance Tracker")
window.resizable(False, False)
icon = PhotoImage(file = "icon.png")
window.iconphoto(True, icon)
window.config(background = "white")

login = PhotoImage(file = "login.png")
Label(window, image = login,background="white").place(x = 5, y = 25)

custom_font = font.Font(family="Poppins", size=30)
custom_font1 = font.Font(family="Poppins", size=20)
custom_font2 = font.Font(family="Poppins", size=15)
custom_font3 = font.Font(family="Poppins", size=10)

name = Label(text="Welcome to 99 Customs", font = custom_font ,fg = "light blue", background="white" ,compound="bottom")
name.place(x = 5, y = 25)
#name.pack()

heading = Label(text = "Sign Up", bg = "white", font = custom_font1)
heading.place(x=648,y=100)

name_text = Label(text = "Enter Your Name:", bg = "white", font = custom_font2)
name_text.place(x = 650, y = 180)

name = Entry(width=40, border=2, fg="black", font = custom_font3)
name.place(x=650, y = 220)

contact_text = Label(text = "Enter Your Contact Number:", bg = "white", font = custom_font2)
contact_text.place(x = 650, y = 260)

contact = Entry(width=40, border=2, fg="black", font = custom_font3)
contact.place(x=650, y = 300)

email_text = Label(text = "Enter your Email-id:", bg = "white", font = custom_font2)
email_text.place(x = 650, y = 340)

email = Entry(width=40, border=2, fg="black", font = custom_font3)
email.place(x=650, y = 380)

submit = Button(window, text = "Submit",command= click)
submit.place(x = 650, y = 430)

#Page2

vehicle_name = Label(new_window,text = "Enyer vheivles data")
vehicle_name.pack()

#new_window.loop()

window.mainloop()
