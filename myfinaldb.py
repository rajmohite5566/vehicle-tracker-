from tkinter import *
from tkinter import messagebox
from tkinter import font
import re

def validate_form(name_entry, contact, email):
    # Get the values entered in the fields
    name = name_entry.get().strip()
    phone = contact.get().strip()
    email_address = email.get().strip()

    # Check if any field is empty
    if not name or not phone or not email_address:
        messagebox.showerror("Error", "All fields must be filled out!")
        return

    # Name validation (Only letters and spaces)
    if not re.match("^[A-Za-z ]+$", name):
        messagebox.showerror("Error", "Invalid Name. Name should contain only letters and spaces.")
        return

    # Phone validation (Phone number starts with 789 and is 10 digits long)
    if not re.match("^789[0-9]{7}$", phone):
        messagebox.showerror("Error", "Invalid Phone Number. It should start with 789 and have 10 digits.")
        return

    # Email validation (basic email pattern)
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email_address):
        messagebox.showerror("Error", "Invalid Email Address.")
        return

    # If all validations pass
    messagebox.showinfo("Success", "Form Submitted Successfully!")

    name_entry.delete(0, END)
    contact.delete(0, END)
    email.delete(0, END)

def new():
    # Create a new top-level window instead of using Tk()
    window = Toplevel(main_window)
    window.geometry("1000x600")
    window.title("Vehicle Maintenance Tracker - Sign Up")
    window.resizable(False, False)
    window.config(background="white")

    try:
        loginimg = PhotoImage(file="login.png")
        # Store the image reference in window (this is essential to avoid it getting garbage collected)
        window.loginimg = loginimg
        Label(window, image=loginimg, bg='white').place(x=5, y=25)
    except Exception as e:
        print(f"Error loading image: {e}")
        
    custom_font = font.Font(family="Poppins", size=30)
    custom_font1 = font.Font(family="Poppins", size=20)
    custom_font2 = font.Font(family="Poppins", size=15)
    custom_font3 = font.Font(family="Poppins", size=10)

    name = Label(window, text="Welcome to 99 Customs", font=custom_font, fg="light blue", background="white", image=loginimg, compound="bottom")
    name.place(x=5, y=25)

    heading = Label(window, text="Sign Up", bg="white", font=custom_font1)
    heading.place(x=648, y=100)

    name_text = Label(window, text="Enter Your Name:", bg="white", font=custom_font2)
    name_text.place(x=650, y=180)

    name_entry = Entry(window, width=40, border=2, fg="black", font=custom_font3)
    name_entry.place(x=650, y=220)

    contact_text = Label(window, text="Enter Your Contact Number:", bg="white", font=custom_font2)
    contact_text.place(x=650, y=260)

    contact = Entry(window, width=40, border=2, fg="black", font=custom_font3)
    contact.place(x=650, y=300)

    email_text = Label(window, text="Enter your Email-id:", bg="white", font=custom_font2)
    email_text.place(x=650, y=340)

    email = Entry(window, width=40, border=2, fg="black", font=custom_font3)
    email.place(x=650, y=380)

    submit = Button(window, text="Submit", command=lambda: validate_form(name_entry, contact, email))  # Validation function is called here
    submit.place(x=650, y=430)


# Main window
main_window = Tk()
main_window.geometry("1050x600")
main_window.title("Vehicle Maintenance Tracker")
main_window.resizable(False, False)
icon = PhotoImage(file="icon.png")
main_window.iconphoto(True, icon)
main_window.config(background="white")

login = PhotoImage(file="rsz_5main.png")

custom_font = font.Font(family="Cabin", size=35)
custom_font2 = font.Font(family="Fira Sans", size=15)
custom_font3 = font.Font(family="Fira Sans", size=10)

head = Label(main_window, text="Welcome To 99 Customs!", font=custom_font, fg="Grey", background="white")
head.place(x=300, y=5)
name = Label(main_window, text=".", font=custom_font, fg="white", background="white", image=login, compound="bottom")
name.place(x=50, y=65)

text1 = Label(main_window, text="At CarCare, we understand how important your car is ", font=custom_font2, background="white")
text2 = Label(main_window, text="to your daily life, and keeping it in top condition ", font=custom_font2, background="white")
text3 = Label(main_window, text="ensures both safety and performance. Our Car ", font=custom_font2, background="white")
text4 = Label(main_window, text="Maintenance Tracker is designed to help you easily ", font=custom_font2, background="white")
text5 = Label(main_window, text="manage and stay on top of all your car’s maintenance ", font=custom_font2, background="white")
text6 = Label(main_window, text="needs—because we believe that preventive care is the", font=custom_font2, background="white")
text7 = Label(main_window, text="key to longevity on the road.", font=custom_font2, background="white")
text1.place(x=500, y=100)
text2.place(x=500, y=130)
text3.place(x=500, y=160)
text4.place(x=500, y=190)
text5.place(x=500, y=220)
text6.place(x=500, y=250)
text7.place(x=500, y=280)

f1 = PhotoImage(file="ic1.png")
f2 = PhotoImage(file="ic2.png")

feature1 = Label(main_window, image=f1, background="white")
feature1.place(x=500, y=360)
feature2 = Label(main_window, image=f2, background="white")
feature2.place(x=780, y=360)

f1_text = Label(main_window, text="Service Remainders", font=custom_font2, fg="grey", background="white")
f1_text.place(x=560, y=330)

f1_text = Label(main_window, text="Monitor Health", font=custom_font2, fg="grey", background="white")
f1_text.place(x=840, y=330)

f1_subtext = Label(main_window, text="Don’t lose sight of your ", font=custom_font3, fg="grey", background="white")
f1_subtext.place(x=560, y=360)
f2_subtext = Label(main_window, text="maintenance and services. ", font=custom_font3, fg="grey", background="white")
f2_subtext.place(x=560, y=380)
f3_subtext = Label(main_window, text="Log your services and we will", font=custom_font3, fg="grey", background="white")
f3_subtext.place(x=560, y=400)
f3_subtext = Label(main_window, text="remind you when it's due.", font=custom_font3, fg="grey", background="white")
f3_subtext.place(x=560, y=420)

f4_subtext = Label(main_window, text="Track the health of your", font=custom_font3, fg="grey", background="white")
f4_subtext.place(x=840, y=360)
f5_subtext = Label(main_window, text="vehicle to gain insights", font=custom_font3, fg="grey", background="white")
f5_subtext.place(x=840, y=380)
f6_subtext = Label(main_window, text="for services and potential", font=custom_font3, fg="grey", background="white")
f6_subtext.place(x=840, y=400)
f8_subtext = Label(main_window, text="faulty issues.", font=custom_font3, fg="grey", background="white")
f8_subtext.place(x=840, y=420)

button_head = Label(main_window, text="Let's Get Started -->", font=custom_font2, background="white")
button_head.place(x=500, y=460)

new_user = Button(main_window, text="New User", font=custom_font2, command=new)
new_user.place(x=500, y=500)

old_user = Button(main_window, text="Existing User", font=custom_font2, command=new)
old_user.place(x=620, y=500)

main_window.mainloop()
