import subprocess
# i am doing this as a experiment so that all  my users will have the requirements for this program
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO
# code  
req=['pillow','requests']#add requirements here because user may not have it

def instl():
    for e  in req:
        subprocess.run(['pip','install',e])
    print('\033[2J\033[H', end='')
    print('\033[96m'+'loading please wait...'+'\033[0m')
instl()
def logo(url):
    response = requests.get(url)
    image_data = response.content
    image = Image.open(BytesIO(image_data))
    image = image.resize((300, 300), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(root, image=photo,bg=root["bg"])
    label.image = photo  # Keep a reference to the image to prevent garbage collection
    label.pack()
def submit():
    age=age_value.get()  # da eth string ayi alley edukull so int()
    email=email_value.get()
    print(f'age : {age} , email : {email}')
# ........................My GUI Section............................
root = tk.Tk()
root.title("Nyctophile")
root.minsize(width=600, height=800) #minimum size of my window
root.config(background='black') #my background color for window
root.option_add("*Font", "Times 18 bold") #giving default font styles
root.option_add("*Foreground", "white") #giving default fg to all my fonts
root.option_add("*Label.Background", root["bg"]) #default color to all my labels
# style object for the Entry widget "alt" to enable curved edges
ttk.Style().theme_use("alt")
style = ttk.Style()
style.configure("TEntry", borderwidth=2, relief="solid", padding=5, bordercolor="black")

# Hawks logo
hawk = "https://i.ibb.co/RYg12BN/full-LOGO.jpg"
logo(hawk)
name = tk.Label(root, text="Shanu Martin",bg=root["bg"])
name.pack(side=tk.TOP)
# frame for content side by side 
content = tk.Frame(root, bg=root["bg"])
content.pack(anchor="nw", pady=10,padx=3)

age_lbl = tk.Label(content, text="Age")
age_lbl.grid(row=0, column=0, padx=20)
age_value = ttk.Entry(content, style="TEntry")
age_value.grid(row=0, column=1)
age_btn=tk.Button(content,text='ok',command=submit,bg='brown',font=('Arial', 10)).grid(row=0, column=2,padx=20)

email_lbl = tk.Label(content, text="Email")
email_lbl.grid(row=1, column=0, padx=20,pady=10)
email_value = ttk.Entry(content, style="TEntry")
email_value.grid(row=1, column=1,pady=10)

btn1 = tk.Button(root, text='submit', command=submit, bg='dark gray', font=('Arial', 14)).pack()
root.mainloop()#eth ettaley window close avull
# ........................My GUI Section END............................

print("you are done")

