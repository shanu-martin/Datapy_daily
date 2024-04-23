#This program needs internet!
# Better to use Windows. 
# plays notification sound if not  needed 🔇before running
# Install all requirments in the first try!
# Don`t mess with my code 😈 



#                                           To Nirmal sir ,
# the code that contain the part where i make class 
# and the answers to your task is from lines 
# ------------------------------------------------  from    90-190
     

# to install requirments to run my code...
import socket
import sys
def install_req():
    try:
        # Attempt to connect to a well-known website
        socket.create_connection(("www.google.com", 80))  #just checking for internet
        req = ['pillow', 'requests', 'customtkinter']
        subprocess.run(['pip', 'install'] + req)
        print('\033[2J\033[H', end='') 
        print('\033[96m' + 'Loading GUI, please wait...' + '\033[0m')
    except OSError:
        print("\033[91mError: Not connected to the internet.\033[0m")
        sys.exit(1)
# Install required packages
install_req()
import threading
import webbrowser
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from customtkinter import *
from customtkinter import CTkButton, CTkImage,CTkCheckBox  
import datetime
# Function to display the logo
def display_logo(root, url):
    response = requests.get(url)
    image_data = response.content
    image = Image.open(BytesIO(image_data))
    image = image.resize((300, 169), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo, bg=root["bg"])
    label.image = photo
    label.pack(pady=0)
# Function to beep
def beep(duration_ms=1000, f=440):
    try:
        import winsound
        # (Windows only sound)
        winsound.Beep(f, duration_ms)  # f is frequency, duration
    except Exception as e:
        print("Error playing system alert sound:", e)
#very complicated function dont mess with it !
def reload_gui(content, answer_lbl):
    # Beep in background
    threading.Thread(target=beep, args=(800, 880)).start()
    print('\033[2J\033[H', end='')
    print("\033[96mYou Initiated a reload\033[0m")
    print("\033[91mNow I'm resetting the window\033[0m")
    if answer_lbl:
        answer_lbl.config(text="Answers to your question will be here !", font=("Verdana", 8), bg='white', fg='black')
    # Clear  entry boxs
    for widget in content.winfo_children():
        if isinstance(widget, ttk.Entry):
            widget.delete(0, "end")
# Function to shake the window
def shake(root):
    dx = 5  
    for _ in range(5):  
        root.geometry(f"450x750+{root.winfo_x() + dx}+{root.winfo_y()}") 
        root.update()
        root.geometry(f"450x750+{root.winfo_x() - dx}+{root.winfo_y()}")  
        root.update()
        dx *= -1  
def invalid(answer_lbl):
    answer_lbl.config(text='INVALID')
    beep(200)
    shake(root)
def scroll_top(canvas):
    canvas.yview_moveto(0)


#fuunctions of my taslk
def single(n1_value,n2_value, answer_lbl):
    class Arithmetic:
        def __init__(self, x, y):
            self.n1 = x
            self.n2 = y
            self.result = ''
        def display(self):
            answer_lbl.config(text=f'Result : {self.result}')
    class Addition(Arithmetic):
        def add(self):
            self.result = self.n1 + self.n2
            self.display()
    try:
        x=int(n1_value.get())
        y=int(n2_value.get())
        obj = Addition(x,y)
        obj.add()
    except ValueError:
        invalid(answer_lbl)
def multilevel(ename_value, eexp_value, checkbox_state, answer_lbl):
    class Company:
        def __init__(self, name, exp):
            self.name = name
            self.exp = exp
            self.info = f'Name : {str(self.name).upper()}\nExperience : {self.exp}'
        def display(self):
            answer_lbl.config(text=str(self.info))
    class Manager(Company):
        def grant_leave(self, state):
            if state == 1:
                self.info += '\n He wants leave'
            else:
                self.info += '\n He doesnt wanr a leave'
    class Employee(Manager):
        pass
    experience='Invalid Entry'
    try:
        name = ename_value.get()
        experience = int(eexp_value.get())
    except ValueError:
        invalid(answer_lbl)
    obj = Employee(name=name, exp=experience)
    if checkbox_state:
        obj.grant_leave(1)
    else:
        obj.grant_leave(0)
    obj.display()
def multiple(sname_value,sroll_value,smark_value,checkbox_state2,answer_lbl): 
    class Teacher:
        def __init__(self,name,roll,mark):
            self.name=name
            self.roll=roll
            self.mark=mark
            self.info=f'Name : {str(self.name).upper()}\nRoll no  : {self.roll}\nMark : {self.mark}'
        def display(self):
            answer_lbl.config(text=str(self.info))
    class Hod:
        def sign(self, state):
            if state == 1:
                self.info += '\n He got sign'
            else:
                self.info += '\n He did`t got sign'
    class Student(Teacher,Hod):
        pass
    roll='Invalid Entry'
    mark='Invalid Entry'

    try:
        name = sname_value.get()
        roll = int(sroll_value.get())
        mark = int(smark_value.get())
    except ValueError:
        invalid(answer_lbl)

    obj = Student(name=name, roll=roll,mark=mark)
    if checkbox_state2:
        obj.sign(1)
    else:
        obj.sign(0)
    obj.display()
def heirarchial(lister, answer_lbl):
    class Polygon:
        def __init__(self,name):
            self.name=name
            self.info=f'I am child of class Polygon\nMy name is {self.name}'
        def display(self):
            answer_lbl.config(text=self.info)
    class Square(Polygon):
        def namex(self):
            self.name='Square'
    class Rectangle(Polygon):
        def namex(self):
            self.name='Rectangle'
    class Triangle(Polygon):
        def namex(self):
            self.name='Triangle'
    tname=lister.get()
    selection = getattr(sys.modules[__name__], tname, Polygon)
    obj = selection(tname) 
    obj.display()


# GUI
def gui(root):
    root.title("task 5")
    root.minsize(width=450, height=750)
    root.maxsize(width=450, height=root.winfo_screenheight()) 
    root.config(background='black')
    root.option_add("*Font", "Times 14 bold")
    root.option_add("*Foreground", "white")
    root.option_add("*Label.Background", root["bg"])

    ttk.Style().theme_use("alt")

    # Create a canvas widget
    canvas = tk.Canvas(root, bg='black', highlightthickness=0)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Add a scrollbar
    scrollbar = tk.Scrollbar(root, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.config(yscrollcommand=scrollbar.set)

    # Frame to contain the widgets
    frame = tk.Frame(canvas, bg='black')
    canvas.create_window((0,0), window=frame, anchor='nw')

    # Making canvas
    frame.bind("<Configure>", lambda event, canvas=canvas: on_frame_configure(canvas))
    frame.bind_all("<MouseWheel>", lambda event, canvas=canvas: on_mousewheel(event, canvas))
    frame.bind_all("<KeyPress-Up>", lambda event, canvas=canvas: on_arrow_key(event, canvas))
    frame.bind_all("<KeyPress-Down>", lambda event, canvas=canvas: on_arrow_key(event, canvas))

    rld_btn = tk.Button(frame, text='refresh', bg='brown', font=('Arial', 8), command=lambda: reload_gui(content, answer_lbl))
    rld_btn.pack(side=tk.TOP, anchor=tk.NE, padx=30, pady=5)

    # Display hawk logo
    hawk_logo_url = "https://i.ibb.co/rdx1n7K/full-LOGO.jpg"
    display_logo(frame, hawk_logo_url)
    # my github?
    def open_git(event):
        webbrowser.open("https://github.com/shanu-martin")
    # Header
    name = tk.Label(frame, text="Shanu Martin", bg='black', fg='white')
    name.pack(side=tk.TOP, pady=0)
    name.bind("<Button-1>", open_git)

    # Answer Section
    answer_container = tk.Frame(frame, bg='white', width=400, height=100, relief="solid", bd=5)
    answer_container.pack(anchor="nw", pady=10, padx=50)

    # Answer Frame
    answer_frame = tk.Frame(answer_container, bg='white', width=350, height=100, borderwidth=5, relief="ridge", highlightbackground="black")
    answer_frame.pack_propagate(False)
    answer_frame.pack()

    answer_lbl = tk.Label(answer_frame, text="Answers to your question will be here !", font=("Verdana", 8), bg='white', fg='black')
    answer_lbl.pack(pady=5, padx=5, fill='both', expand=True) 



    # Content
    content = tk.Frame(frame, bg='black')
    content.pack(anchor="nw", pady=10, padx=3)

    # Question Section
    q1_hdng=tk.Label(content, text="Single Inheritance  ", bg='black', fg='green')
    q1_hdng.grid(row=0, column=1, padx=20,sticky='w')

    q1_class1=tk.Label(content, text="Parent Name : Arithmetic ", bg='black', fg='brown')
    q1_class1.grid(row=1, column=0,columnspan=2, padx=20,sticky='w')

    q1_class1_mthd=tk.Label(content, text="class Methods  : display() ", bg='black', fg='white')
    q1_class1_mthd.grid(row=2, column=0,columnspan=2, padx=20,sticky='w')

    q1_class2=tk.Label(content, text="Child Name : Addition ", bg='black', fg='brown')
    q1_class2.grid(row=3, column=0,columnspan=2, padx=20,sticky='w')

    q1_class2_mthd=tk.Label(content, text="class Methods  : add() ", bg='black', fg='white')
    q1_class2_mthd.grid(row=4, column=0,columnspan=2, padx=20,sticky='w')


    q1_lbl2=tk.Label(content, text="Arithmetic is parent class of Addition showing single inheritance.", bg='black', fg='white' ,font=('Arial', 10))
    q1_lbl2.grid(row=5, column=0,columnspan=3, padx=20,sticky='w')

    n1_lbl = tk.Label(content, text="N1:", bg='black', fg='white')
    n1_lbl.grid(row=6, column=0, padx=20, pady=10,sticky='w')
    n1_value = ttk.Entry(content, style="TEntry")
    n1_value.grid(row=6, column=1, pady=10)
    n2_lbl = tk.Label(content, text="N2:", bg='black', fg='white')
    n2_lbl.grid(row=7, column=0, padx=20, pady=10,sticky='w')
    n2_value = ttk.Entry(content, style="TEntry")
    n2_value.grid(row=7, column=1, pady=10)

    add_btn = tk.Button(content, text='Display', command=lambda: single(n1_value,n2_value, answer_lbl), bg='brown', font=('Arial', 10))
    add_btn.grid(row=7, column=2, padx=20)
    # --------------------------------------------------------------------------------
    q2_hdng=tk.Label(content, text="Multilevel Inheritance  ", bg='black', fg='green')
    q2_hdng.grid(row=8, column=1, padx=20,sticky='w')

    q2_class1=tk.Label(content, text="Base Class : Company ", bg='black', fg='brown')
    q2_class1.grid(row=9, column=0,columnspan=2, padx=20,sticky='w')

    q2_class1_mthd=tk.Label(content, text="class Methods  : display() ", bg='black', fg='white')
    q2_class1_mthd.grid(row=10, column=0,columnspan=2, padx=20,sticky='w')

    q2_class2=tk.Label(content, text="Parent Class : Manager ", bg='black', fg='brown')
    q2_class2.grid(row=11, column=0,columnspan=2, padx=20,sticky='w')

    q2_class2_mthd=tk.Label(content, text="class Methods  : grant_leave() ", bg='black', fg='white')
    q2_class2_mthd.grid(row=12, column=0,columnspan=2, padx=20,sticky='w')

    q2_class2=tk.Label(content, text="Child Class : Employee ", bg='black', fg='brown')
    q2_class2.grid(row=13, column=0,columnspan=2, padx=20,sticky='w')

    q2_lbl=tk.Label(content, text="*Company class is parent class of Manager class and\t\t \n Manager is parent of Employee showing Multilevel inheritance.", bg='black', fg='white' ,font=('Arial', 10))
    q2_lbl.grid(row=14, column=0,columnspan=3, padx=20,sticky='w')

    ename_lbl = tk.Label(content, text="Name :", bg='black', fg='white')
    ename_lbl.grid(row=15, column=0, padx=20, pady=10,sticky='w')
    ename_value = ttk.Entry(content, style="TEntry")
    ename_value.grid(row=15, column=1, pady=10)

    eexp_lbl = tk.Label(content, text="Exp :", bg='black', fg='white')
    eexp_lbl.grid(row=16, column=0, padx=20, pady=10,sticky='w')
    eexp_value = ttk.Entry(content, style="TEntry")
    eexp_value.grid(row=16, column=1, pady=10)

    checkbox_var = tk.IntVar()  # Create a variable for checkbox state
    checkbox = CTkCheckBox(master=content, text="Apply for leave", fg_color="brown", checkbox_height=30, checkbox_width=30, corner_radius=36, variable=checkbox_var)
    checkbox.grid(row=17, column=0, columnspan=2, padx=20, pady=10)

    # checkbox
    def get_checkbox_state():
        return checkbox_var.get()

    multilevel_btn = tk.Button(content, text='Display', command=lambda: (multilevel(ename_value, eexp_value, get_checkbox_state(), answer_lbl), scroll_top(canvas)), bg='brown', font=('Arial', 10))
    multilevel_btn.grid(row=17, column=2, padx=20)
    # --------------------------------------------------------------------------------
    q3_hdng=tk.Label(content, text="Multiple Inheritance  ", bg='black', fg='green')
    q3_hdng.grid(row=18, column=1, padx=20,sticky='w')

    q3_class1=tk.Label(content, text="Parent 1 : Teacher ", bg='black', fg='brown')
    q3_class1.grid(row=19, column=0,columnspan=2, padx=20,sticky='w')

    q3_class1_mthd=tk.Label(content, text="class Methods  : display() ", bg='black', fg='white')
    q3_class1_mthd.grid(row=20, column=0,columnspan=2, padx=20,sticky='w')

    q3_class2=tk.Label(content, text="Parent 2 : HOD ", bg='black', fg='brown')
    q3_class2.grid(row=21, column=0,columnspan=2, padx=20,sticky='w')

    q3_class2_mthd=tk.Label(content, text="class Methods  : sign() ", bg='black', fg='white')
    q3_class2_mthd.grid(row=22, column=0,columnspan=2, padx=20,sticky='w')

    q3_class2=tk.Label(content, text="Child Class : Student ", bg='black', fg='brown')
    q3_class2.grid(row=23, column=0,columnspan=2, padx=20,sticky='w')

    q3_lbl=tk.Label(content, text="*Teacher class & Hod class parents of Student class", bg='black', fg='white' ,font=('Arial', 10))
    q3_lbl.grid(row=24, column=0,columnspan=3, padx=20,sticky='w')

    sname_lbl = tk.Label(content, text="Name :", bg='black', fg='white')
    sname_lbl.grid(row=25, column=0, padx=20, pady=10,sticky='w')
    sname_value = ttk.Entry(content, style="TEntry")
    sname_value.grid(row=25, column=1, pady=10)

    sroll_lbl = tk.Label(content, text="Roll no :", bg='black', fg='white')
    sroll_lbl.grid(row=26, column=0, padx=20, pady=10,sticky='w')
    sroll_value = ttk.Entry(content, style="TEntry")
    sroll_value.grid(row=26, column=1, pady=10)

    smark_lbl = tk.Label(content, text="Mark :", bg='black', fg='white')
    smark_lbl.grid(row=27, column=0, padx=20, pady=10,sticky='w')
    smark_value = ttk.Entry(content, style="TEntry")
    smark_value.grid(row=27, column=1, pady=10)

    checkbox_var2 = tk.IntVar()  
    checkbox2 = CTkCheckBox(master=content, text="Signed by HOD", fg_color="brown", checkbox_height=30, checkbox_width=30, corner_radius=36, variable=checkbox_var2)
    checkbox2.grid(row=28, column=0, columnspan=2, padx=20, pady=10)

    # checkbox
    def get_checkbox_state2():
        return checkbox_var2.get()
    multiple_btn = tk.Button(content, text='Display', command=lambda: (multiple(sname_value,sroll_value,smark_value, get_checkbox_state2(), answer_lbl), scroll_top(canvas)), bg='brown', font=('Arial', 10))
    multiple_btn.grid(row=28, column=2, padx=20)

    # --------------------------------------------------------------------------------

    q4_hdng=tk.Label(content, text="Heirarchial Inheritance  ", bg='black', fg='green')
    q4_hdng.grid(row=30, column=1,columnspan=2, padx=20,sticky='w')

    q4_class1=tk.Label(content, text="Parent  : Polygon ", bg='black', fg='brown')
    q4_class1.grid(row=31, column=0,columnspan=2, padx=20,sticky='w')

    lister=CTkComboBox(master=content, values=["Square", "Rectangle", "Triangle"],fg_color='brown')
    lister.grid(row=32, column=0,columnspan=2, padx=0)

    q4_class1_mthd=tk.Label(content, text="class Methods :display() ", bg='black', fg='white')
    q4_class1_mthd.grid(row=33, column=0,columnspan=2, padx=20,sticky='w')

    q4_class2=tk.Label(content, text="Child 1 : Square ", bg='black', fg='brown')
    q4_class2.grid(row=34, column=0,columnspan=2, padx=20,sticky='w')
    q4_class3=tk.Label(content, text="Child 2 : Rectangle ", bg='black', fg='brown')
    q4_class3.grid(row=35, column=0,columnspan=2, padx=20,sticky='w')
    q4_class4=tk.Label(content, text="Child 3 : Triangle ", bg='black', fg='brown')
    q4_class4.grid(row=36, column=0,columnspan=2, padx=20,sticky='w')

    hier = tk.Button(content, text='Display', command=lambda: (heirarchial(lister, answer_lbl), scroll_top(canvas)), bg='brown', font=('Arial', 10))
    hier.grid(row=32, column=2, padx=0)

    q3_lbl=tk.Label(content, text="*Square,Rectangle,Triangle are children of Polygon class", bg='black', fg='white' ,font=('Arial', 10))
    q3_lbl.grid(row=37, column=0,columnspan=3, padx=20,sticky='w')
    # Exit Button
    img_url = "https://i.ibb.co/zN32f7p/dd.png"
    response = requests.get(img_url)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    btn = CTkButton(master=frame, text="Exit", corner_radius=32, fg_color="brown", hover_color="#D2B48C", border_color="white", border_width=2, image=CTkImage(dark_image=img, light_image=img), command=root.destroy)  # Command to destroy the root window
    btn.pack()

    # Footer 
    foot = tk.Label(frame, text='Made by shanu as template for Datapy daily tasks', bg='white', fg='black', font=("Verdana", 8, "bold"))
    foot.pack(side=tk.BOTTOM, fill='x', pady=5)

    root.mainloop()  # Run the event loop

# Scrolling feature to entry window 
def on_frame_configure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

def on_mousewheel(event, canvas):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

def on_arrow_key(event, canvas):
    if event.keysym == "Up":
        canvas.yview_scroll(-1, "units")
    elif event.keysym == "Down":
        canvas.yview_scroll(1, "units")

# Create a new Screen
root = tk.Tk()
gui(root)


print("You are done!")

