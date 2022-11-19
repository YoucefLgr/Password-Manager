import tkinter
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def choose():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for i in range(nr_letters)]
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    password_list = password_symbols + password_numbers + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    input_3.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def pw():
    global data, t
    web = input_1.get()
    email = input_2.get()
    pas = input_3.get()
    dict = {
        web: {
            "email": email,
            "password": pas,
        }
    }
    if pas == "" or email == "" or web == "":
        messagebox.showwarning(title="Password Manager", message="please type the full infos")
    else:
        try:
            t = open("data.json", "r")
            data = json.load(t)

        except FileNotFoundError:
            t = open("data.json", "w")
            json.dump(dict, t, indent=4)
        else:
            data.update(dict)
            t = open("data.json", "w")
            json.dump(data, t, indent=4)
        finally:
            input_1.delete(0, tkinter.END)
            input_3.delete(0, tkinter.END)


def find():
    web = input_1.get()
    try:
        with open("data.json", "r") as dt:
            d = json.load(dt)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Data File Not Found")
    else:
        if web in d:
            e = d[web]["email"]
            p = d[web]["password"]
            messagebox.showinfo(title=web, message=f"email : {e}\n password : {p}")
        else:
            messagebox.showinfo(title="Error", message=f"No Information For {web} exists")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.config(padx=50, pady=50, height=400, width=400)
window.title("PassWord_ManaGer")
canvas = tkinter.Canvas(width=200, height=200)
img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)
label_1 = tkinter.Label(text="Website : ")
label_1.grid(row=1, column=0)
input_1 = tkinter.Entry(width=33)
input_1.grid(row=1, column=1, columnspan=1)
input_1.focus()
butt0 = tkinter.Button(text="Search", command=find, width=14)
butt0.grid(row=1, column=2)
label_2 = tkinter.Label(text="Email/UserName : ")
label_2.grid(row=2, column=0)
input_2 = tkinter.Entry(width=51)
input_2.insert(0, "youcef@email.com")
input_2.grid(row=2, column=1, columnspan=2)
label_3 = tkinter.Label(text="PassWord : ")
label_3.grid(row=3, column=0)
input_3 = tkinter.Entry(width=33)
input_3.grid(row=3, column=1)
butt = tkinter.Button(text="Generate Password", command=choose)
butt.grid(row=3, column=2)
butt_2 = tkinter.Button(text="Add", width=43, command=pw)
butt_2.grid(row=4, column=1, columnspan=2)

window.mainloop()
