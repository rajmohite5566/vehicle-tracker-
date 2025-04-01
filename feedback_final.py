from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re
import pymysql
from tkinter import font
import time


myconn = pymysql.connect(host='localhost', database='v_tracker', user='root', password='root', charset='utf8', port=3306)
print('connected')
cursor = myconn.cursor()

#email
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

#phone number 
def is_valid_phone(phone):
    return bool(re.match(r'^[789]\d{9}$', phone))

#name
def is_valid_name(name):
    return bool(re.match(r'^[A-Z][a-z]+ [A-Z][a-zA-Z]+$', name))

#feedback function 
def submit_feedback():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    feedback = feedback_text.get("1.0", END).strip()

    if not name or not phone or not email or not feedback:
        messagebox.showerror("Incomplete Details", "Please fill in all the fields before submitting.")
        return
    
    if not is_valid_name(name):
        messagebox.showerror("Invalid Name", "Invalid Name! Please Enter a valid Name.")
        return

    if not is_valid_email(email):
        messagebox.showerror("Invalid Email", "Please enter a valid email address.")
        return

    if not is_valid_phone(phone):
        messagebox.showerror("Invalid Phone", "Invalid Phone Number.")
        return

    try:
        cursor.execute("INSERT INTO feedback(name, phone, email, feedback) VALUES (%s, %s, %s, %s)",
                      (name, phone, email, feedback))
        myconn.commit()
        messagebox.showinfo("Feedback Sent!", "Your feedback has been submitted successfully. Thank you!")
        
        # Clear input 
        name_entry.delete(0, END)
        phone_entry.delete(0, END)
        email_entry.delete(0, END)
        feedback_text.delete("1.0", END)

        open_new_window()
        
    except pymysql.MySQLError as e:
        messagebox.showerror("Database Error!", "Failed to save feedback: " + str(e))

def open_new_window():
    new_window = Toplevel(top)
    new_window.title("Thank You!")
    new_window.geometry("400x300")
    new_window.resizable(False, False)

    thank_you_label = Label(new_window, text="Thank you for your feedback!", font=myfont_1, fg="green")
    thank_you_label.pack(pady=50)
    
    close_button = Button(new_window, text="Close", command=new_window.destroy, font=myfont_3, bg="teal", fg="white")
    close_button.pack()

#gui
top = Tk()
top.geometry("1000x600")  
top.title("Customer Feedback")
top.resizable(False, False)
top.configure(bg="white")

#image 
try:
    feed_image = PhotoImage(file="rsz_1feedback.png")
    Label(top, image=feed_image, background="white").place(x=50, y=100)
except Exception as e:
    print(f"Error loading image: {e}")

myfont = font.Font(family="Poppins", size=30)
myfont_1 = font.Font(family="Poppins", size=20)
myfont_2 = font.Font(family="Poppins", size=15)
myfont_3 = font.Font(family="Poppins", size=10)

label_font = ("Arial", 12, "bold")
input_font = ("Arial", 12)
button_font = ("Arial", 14, "bold")
heading_font = ("Arial", 18, "bold")

heading = Label(top, text="Feedback Form", fg="Blue", font=myfont_1, bg="White")
heading.pack(pady=10)

#Labels 
name_label = Label(top, text="Your Name:", bg="white", font=myfont_2)
name_label.place(x=650, y=100)

phone_label = Label(top, text="Phone Number:", bg="white", font=myfont_2)
phone_label.place(x=650, y=190)

email_label = Label(top, text="Email Address:", bg="white", font=myfont_2)
email_label.place(x=650, y=270)

feedback_label = Label(top, text="Your Feedback:", bg="white", font=myfont_2)
feedback_label.place(x=650, y=350)

#input/entries
name_entry = Entry(top, width=40, border=2, font=myfont_3)
name_entry.place(x=650, y=140)

phone_entry = Entry(top, width=40, border=2, font=myfont_3)
phone_entry.place(x=650, y=230)

email_entry = Entry(top, width=40, border=2, font=myfont_3)
email_entry.place(x=650, y=310)

feedback_text = Text(top, width=40, border=2, height=5, font=myfont_3)
feedback_text.place(x=650, y=390)

#Submit Button
submit_button = Button(top, text="Submit", command=submit_feedback, bg="teal", fg="white", font=myfont_3, relief="raised")
submit_button.place(x=650, y=530)


top.mainloop()

cursor.close()
myconn.close()
