from tkinter import *
from tkinter.ttk import *
import time

def open_new_window():
    new_window = Toplevel(top)
    new_window.title("New Blank Page")
    new_window.geometry("400x300")
    blank_label = Label(new_window, text="This is page.")
    blank_label.pack(pady=20)
   

def open_file():
    print("File Opened")

def Start():
    File = 100
    download = 0
    speed = 1
    while(download < File):
        time.sleep(0.05)
        bar['value'] += (speed/File)*100
        download += speed
        percent.set(str(int((download/File)*100))+"%")
        text.set(str(download)+"/"+str(File)+" File Downloaded ")
        top.update_idletasks()

    bar['value'] = 100
    percent.set('100%')
    text.set("Download Complete")

    open_button.pack()

    open_button.config(state = NORMAL)

top = Tk()

percent = StringVar()
text = StringVar()
                    
bar = Progressbar(top, orient=HORIZONTAL, length=200)
bar.pack(pady=20)

percent_lable = Label(top,textvariable = percent)
percent_lable.pack()

tasklabel = Label(top,textvariable = text)
tasklabel.pack()

open_button = Button(top, text="Open", command=open_new_window, state=DISABLED)
open_button.pack(pady=10)

pro_button = Button(top, text="Download", command=Start)
pro_button.pack()

top.mainloop()



