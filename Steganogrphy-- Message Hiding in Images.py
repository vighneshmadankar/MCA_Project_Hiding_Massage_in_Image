from tkinter import *
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk
import os
from stegano import lsb

win = Tk()
win.geometry('900x600')
win.config(bg='#2C3E50')  # Set background color
win.title("Message Hiding in Image")

# Function to open an image
def open_img():
    global open_file
    open_file = filedialog.askopenfilename(initialdir=os.getcwd(),
                                            title='Select File Type',
                                            filetypes=(('PNG file', '*.png'), ('JPG file', '*.jpg'),
                                                       ('All files', '*.*')))
    if open_file:
        img = Image.open(open_file)
        img = ImageTk.PhotoImage(img)
        lf1.configure(image=img)
        lf1.image = img

# Function to hide a message in the image
def hide():
    global open_file
    global hide_msg
    password = code.get()
    if password == '1234':
        msg = text1.get(1.0, END)
        hide_msg = lsb.hide(str(open_file), msg)
        hide_msg.save(open_file)  # Save the hidden message in the same file
        messagebox.showinfo('Success', 'Your message is successfully hidden in the image')
    elif password == '':
        messagebox.showerror('Error', 'Please enter Secret key')
    else:
        messagebox.showerror('Error', 'Wrong Secret Key')
        code.set('')

# Function to save the image with the hidden message
def save_img():
    global hide_msg
    hide_msg.save('Secret_file.png')
    messagebox.showinfo('Saved', 'Image has been successfully saved')

# Function to reveal the hidden message in the image
def show():
    password = code.get()
    if password == '1234':
        show_msg = lsb.reveal(open_file)
        text1.delete(1.0, END)
        text1.insert(END, show_msg)
    elif password == '':
        messagebox.showerror('Error', 'Please enter Secret key')
    else:
        messagebox.showerror('Error', 'Wrong Secret Key')
        code.set('')

# Function to change the password
def change_password():
    new_password = simpledialog.askstring("Change Password", "Enter new password:")
    if new_password:
        code.set(new_password)

# Heading
Label(win, text='Message Hiding in Image', font='Helvetica 24 bold', bg='#2C3E50', fg='#E74C3C').place(x=230, y=20)

# Frame 1
f1 = Frame(win, width=400, height=300, bd=5, bg='#3498DB')
f1.place(x=50, y=100)
lf1 = Label(f1, bg='#3498DB')
lf1.place(x=0, y=0)

# Frame 2
f2 = Frame(win, width=400, height=300, bd=5, bg='#E74C3C')
f2.place(x=450, y=100)
text1 = Text(f2, font='Helvetica 14 bold', wrap=WORD)
text1.place(x=0, y=0, width=390, height=290)

# Label for Secret Key
Label(win, text='Enter Secret Key', font='Helvetica 12 bold', bg='#2C3E50', fg='#F39C12').place(x=350, y=480)

# Entry Widget for secret key
code = StringVar()
e = Entry(win, textvariable=code, bd=2, font='Helvetica 12 bold ', show='*')
e.place(x=350, y=520)

# Button to change password
change_password_button = Button(win, text='Change Password', bg='#3498DB', fg='#ECF0F1', font='Helvetica 12 bold ',
                                cursor='hand2', command=change_password)
change_password_button.place(x=500, y=520)

# Buttons
open_button = Button(win, text='Open Image', bg='#3498DB', fg='#ECF0F1', font='Helvetica 12 bold ', cursor='hand2',
                     command=open_img)
open_button.place(x=50, y=480)

save_button = Button(win, text='Save Image', bg='#E74C3C', fg='#ECF0F1', font='Helvetica 12 bold ', cursor='hand2',
                     command=save_img)
save_button.place(x=200, y=480)

hide_button = Button(win, text='Hide Data', bg='#2ECC71', fg='#ECF0F1', font='Helvetica 12 bold ', cursor='hand2',
                     command=hide)
hide_button.place(x=350, y=560)

show_button = Button(win, text='Show Data', bg='#F39C12', fg='#ECF0F1', font='Helvetica 12 bold ', cursor='hand2',
                     command=show)
show_button.place(x=500, y=560)

win.mainloop()