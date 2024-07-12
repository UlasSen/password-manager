from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json 
global website
global password
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    #Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters= [random.choice(letters) for i in range(nr_letters)]
    password_symbols= [random.choice(symbols) for i in range(nr_symbols)]
    password_numbers= [random.choice(numbers) for i in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)

    entry_password.insert(0,password)
    pyperclip.copy(password)
    '''password = ""
    for char in password_list:
    password += char'''


# ---------------------------- SAVE PASSWORD ------------------------------- #

def Save():
    website = entry_web.get()
    email = entry_email.get()
    password = entry_password.get()
    new_Data = {website: {
         
    
                "email":email,
                "password":password
                
                }
    }

    if website=="" or password=="":
        messagebox.showwarning(title="Oops...",message="Please dont leave any fields empty!")
        
    try:
        with open("data.json", "r") as data_File:
                
                data=json.load(data_File)

                data.update(new_Data)

        

        with open("data.json", "w") as data_File:
                json.dump(data,data_File,indent=4)
                
                entry_web.delete(0,END)
                entry_password.delete(0, END)
    
    except FileNotFoundError:
        with open("data.json", "w") as data_File:
             json.dump(new_Data,data_File,indent=4)


def find_password():
    website = entry_web.get()
    
    with open("data.json", "r") as data_File:
    

     website_control= json.load(data_File)
     for key in website_control :
          email = website_control[website]["email"]
          password = website_control[website]["password"]
          if website in website_control:
               messagebox.showinfo(title=f"Your details for {website}.",message=f"Email: {email}\nPassword: {password}")
               break
     
     
     
   


     
        

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas=Canvas(width=200,height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0,column=1)

label_website=Label(text="Website:")
label_website.grid(row=1,column=0)

label_email= Label(text="Email/Username:")
label_email.grid(row=2,column=0)

label_password= Label(text="Password:")
label_password.grid(row=3,column=0)



entry_web=Entry(width=35)
entry_web.grid(row=1, column=1)
a=entry_web.focus()

entry_email=Entry(width=35)
entry_email.grid(row=2, column=1, )
entry_email.insert(0,"ulasennn@gmail.com")

entry_password=Entry(width=35)
entry_password.grid(row=3, column=1)


button_generate=Button(text="Generate Password", command=generator)
button_generate.grid(row=3,column=2)

button_add=Button(text="Add",width=36,command=Save)
button_add.grid(row=4,column=1   )

button_search = Button(text="Search", command=find_password, width=13)
button_search.grid(row=1,column=2)










window.mainloop()