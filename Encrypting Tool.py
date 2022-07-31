import base64
from tkinter import *
from tkinter import messagebox
from base64 import *
import os




def encrypt():
    password=code.get()
    if password=="1o1rowc":
        screen1=Toplevel()
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message=text1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode(("ascii"))

        Label(screen1,text="Encrypt",font="arial",fg="white",bg="#ed3833").place(x=10,y=0)
        text2=Text(screen1,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)
        text2.insert(END,encrypt)
    elif password=="":
        messagebox.showerror("encryption","Input Password")
    elif password!="1o1rowc":
        messagebox.showerror("encryption","Invalid Password")

def decrypt():
    password = code.get()
    if password == "1o1rowc":
        screen2 = Toplevel()
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode(("ascii"))

        Label(screen2, text="Decrypt", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
        text2 = Text(screen2, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, decrypt)
    elif password == "":
        messagebox.showerror("encryption", "Input Password")
    elif password != "1o1rowc":
        messagebox.showerror("encryption", "Invalid Password")


def main_screen():
    global main_screen
    global code
    global text1
    def reset():
        code.set("")
        text1.delete(1.0,END)
    screen=Tk()
    screen.geometry("500x450")
    screen.title("Encrypter")
    Label(text="Enter text for Encryption and Decryption",fg="Black",font=("calbri",13)).place(x=10,y=10)
    text1=Text(font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=480,height=100)
    Label(text="Enter the key for Encryption and Decryption",fg="black",font=("calibri",13)).place(x=10,y=170)
    code=StringVar()
    Entry(textvariable=code,width=22,bd=0,font=("calbri",26),show="*").place(x=10,y=200)
    Button(text="Encrypt",height="2",width=23,bg="#ed3833",fg="white",bd=0,command=encrypt).place(x=10,y=250)
    Button(text="Decrypt", height="2", width=23, bg="#00bd56", fg="white", bd=0,command=decrypt).place(x=250, y=250)
    Button(text="Reset", height="2", width=50, bg="#1089ff", fg="white", bd=0,command=reset).place(x=10, y=350)
    screen.mainloop()
main_screen()

 
