#This program needs internet!
# Better to use Windows. 
# plays notification sound if not  needed 🔇before running
# Install all requirments in the first try!
# Don`t mess with my code 😈 
import subprocess
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
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from customtkinter import CTkButton, CTkImage
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
def q1(get_String_value, answer_lbl):
    class Word:
        def get_String(self):
            self.x = get_String_value.get()

        def print_String(self):
            res=self.x.upper()
            answer_lbl.config(text=res)
    obj = Word()                            #object for Question !
    obj.get_String()
    obj.print_String()
def q2(radious_entry, answer_lbl):
    class Circle:
        def __init__(self, r):
            self.r = r

        def area(self):
            res = 3.14 * self.r * self.r
            return res

        def pm(self):
            res = 2 * 3.14 * self.r
            return res

    try:
        r = int(radious_entry.get()) 
        obj2 = Circle(r)
        Area = obj2.area()
        pm = obj2.pm()
        res = f'Area of the Circle = {Area}\nPerimeter of Circle = {pm}'
        answer_lbl.config(text=res)
    except ValueError:
        invalid(answer_lbl)
def q3(sname_value, roll_value, age_value, mark_value, answer_lbl):
    class Student:
        def __init__(self, name, roll='Invalid', age=None, mark=None):
            self.name = name
            try:
                x=int(roll)
                self.roll = roll
            except:
                self.roll ='Invalid'
                invalid(answer_lbl)
            self.age = age if age is not None else 'Not set'
            self.mark = mark if mark is not None else 'Not set'

        def display(self):
            res = f'Student Name: {self.name}\nRoll no: {self.roll}\nAge: {self.age}\nMarks: {self.mark}'
            answer_lbl.config(text=res)

        def setAge(self, age):
            try:
                x=int(age)
                self.age = x
            except:
                invalid(answer_lbl)

        def setMark(self, mark):
            try:
                x=int(mark)
                self.mark = mark
            except:
                invalid(answer_lbl)

    name = sname_value.get()
    roll = roll_value.get()
    age = age_value.get()
    mark = mark_value.get()

    obj3 = Student(name, roll)
    if age:
        obj3.setAge(age)

    # mark undenkil
    if mark:
        obj3.setMark(mark)

    obj3.display()
def q4(hour_value, min_value, x, answer_lbl):
    timeNow = datetime.datetime.now()
    Hour = timeNow.strftime("%I") 
    M = timeNow.strftime("%M") 
    hour_str = hour_value.get()
    min_str = min_value.get()
    if hour_str == '' or min_str == '':
        
        Hour = timeNow.strftime("%I")
        M = timeNow.strftime("%M")
    else:
        try:
            Hour = int(hour_str)
            M = int(min_str)
        except ValueError:
            invalid(answer_lbl)
            return

    class Time:
        def __init__(self, Hour, M):
            self.Hour = Hour
            self.M = M

        def addtime(self):
            res = f'Time values Together: {int(self.Hour) + int(self.M)}'
            answer_lbl.config(text=res, font=("Verdana", 12,"bold"), bg='white', fg='black')

        def display(self):
            res = f'{self.Hour} hr {self.M} min'
            answer_lbl.config(text=res, font=("Verdana", 12,"bold"), bg='white', fg='black')

        def dispMin(self):
            total_minutes = (int(self.Hour) * 60) + int(self.M)
            res = f'{total_minutes} minutes'
            answer_lbl.config(text=res, font=("Verdana", 12,"bold"), bg='white', fg='black')

    obj4 = Time(Hour, M)
    if x == 1:
        obj4.addtime()
    elif x == 2:
        obj4.display()
    elif x == 3:
        obj4.dispMin()
    else:
        invalid(answer_lbl)


# GUI
def gui(root):
    root.title("task 4")
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

    # Header
    name = tk.Label(frame, text="Shanu Martin", bg='black', fg='white')
    name.pack(side=tk.TOP, pady=0)

    # Answer Section
    answer_container = tk.Frame(frame, bg='white', width=400, height=100, relief="solid", bd=5)
    answer_container.pack(anchor="nw", pady=10, padx=50)

    # Answer Frame
    answer_frame = tk.Frame(answer_container, bg='white', width=350, height=100, borderwidth=5, relief="ridge", highlightbackground="black")
    answer_frame.pack_propagate(False)
    answer_frame.pack()

    answer_lbl = tk.Label(answer_frame, text="Answers to your question will be here !", font=("Verdana", 8), bg='white', fg='black')
    answer_lbl.pack(pady=5, padx=5, fill='both', expand=True) 
    answer_lbl2 = tk.Label(answer_frame, text=" ", font=("Verdana", 8), bg='white', fg='black')
    answer_lbl2.pack(pady=5, padx=5, fill='both', expand=True)

    # Content
    content = tk.Frame(frame, bg='black')
    content.pack(anchor="nw", pady=10, padx=3)

    # Question Section
    q1_lbl=tk.Label(content, text="Class Name : Word ", bg='black', fg='white')
    q1_lbl.grid(row=0, column=0,columnspan=2, padx=20,sticky='w')
    
    get_String_lbl = tk.Label(content, text="String:", bg='black', fg='white')
    get_String_lbl.grid(row=1, column=0, padx=20, pady=10,sticky='w')
    get_String_value = ttk.Entry(content, style="TEntry")
    get_String_value.grid(row=1, column=1, pady=10)
    get_String_btn = tk.Button(content, text='Display', command=lambda: q1(get_String_value, answer_lbl), bg='brown', font=('Arial', 10))
    get_String_btn.grid(row=1, column=2, padx=20)
    
    #Question 2
    q2_lbl=tk.Label(content, text="Enter Radious to Create Object to Class Circle ", bg='black', fg='white' ,font=('Arial', 12))
    q2_lbl.grid(row=2, column=0,columnspan=3, padx=20,sticky='w')
    q2_info=tk.Label(content, text="Class Name : Circle ", bg='black', fg='white')
    q2_info.grid(row=3, column=0,columnspan=2, padx=20,sticky='w')

    radious_lbl = tk.Label(content, text="Radious :", bg='black', fg='white')
    radious_lbl.grid(row=4, column=0, padx=20, pady=10)
    radious_value = ttk.Entry(content, style="TEntry")
    radious_value.grid(row=4, column=1, pady=10)
    get_radious = tk.Button(content, text='Create', command=lambda: q2(radious_value, answer_lbl), bg='brown', font=('Arial', 10))
    get_radious.grid(row=4, column=2, padx=20)

    #Question 3
    q3_lbl3=tk.Label(content, text="Student", bg='black', fg='white' ,font=('Arial', 14,"bold"))
    q3_lbl3.grid(row=5, column=0, padx=20,sticky='w')
    q3_lbl=tk.Label(content, text="Enter Name & Roll no Create Student ", bg='black', fg='white' ,font=('Arial', 12))
    q3_lbl.grid(row=5, column=1,columnspan=2, padx=3,sticky='w')

    sname_lbl = tk.Label(content, text="Name :", bg='black', fg='white')
    sname_lbl.grid(row=6, column=0, padx=20, pady=10)
    sname_value = ttk.Entry(content, style="TEntry")
    sname_value.grid(row=6, column=1, pady=10)

    roll_lbl = tk.Label(content, text="Roll no :", bg='black', fg='white')
    roll_lbl.grid(row=7, column=0, padx=20, pady=10)
    roll_value = ttk.Entry(content, style="TEntry")
    roll_value.grid(row=7, column=1, pady=10)

    screate = tk.Button(content, text='Create', command=lambda: q3(sname_value,roll_value,age_value,mark_value, answer_lbl), bg='brown', font=('Arial', 10))
    screate.grid(row=7, column=2, padx=20)

    q3_lbl2=tk.Label(content, text="Age & Mark are optional !", bg='black', fg='white' ,font=('Arial', 12))
    q3_lbl2.grid(row=8, column=0,columnspan=2, padx=20,sticky='w')



    age_lbl = tk.Label(content, text="Age :", bg='black', fg='white')
    age_lbl.grid(row=9, column=0, padx=20, pady=10,sticky='w')
    age_value = ttk.Entry(content, style="TEntry")
    age_value.grid(row=9, column=1, pady=10)

    mark_lbl = tk.Label(content, text="Mark :", bg='black', fg='white')
    mark_lbl.grid(row=10, column=0, padx=20, pady=10,sticky='w')
    mark_value = ttk.Entry(content, style="TEntry")
    mark_value.grid(row=10, column=1, pady=10)

    screate = tk.Button(content, text='Create', command=lambda: q3(sname_value,roll_value,age_value,mark_value, answer_lbl), bg='brown', font=('Arial', 10))
    screate.grid(row=10, column=2, padx=20)

    q4_lbl=tk.Label(content, text="Class :Time ", bg='black', fg='white' ,font=('Arial', 14, "bold"))
    q4_lbl.grid(row=11, column=0,columnspan=2, padx=20,sticky='w')

    q4_lbl2=tk.Label(content, text="Enter Hour & Minute in respective Fields.", bg='black', fg='white' ,font=('Arial', 12))
    q4_lbl2.grid(row=12, column=0,columnspan=2, padx=20,sticky='w')
 
    hour_lbl = tk.Label(content, text="Hour:", bg='black', fg='white')
    hour_lbl.grid(row=13, column=0, padx=20, pady=10,sticky='w')
    hour_value = ttk.Entry(content, style="TEntry")
    hour_value.grid(row=13, column=1, pady=10)
    min_lbl = tk.Label(content, text="Minute:", bg='black', fg='white')
    min_lbl.grid(row=14, column=0, padx=20, pady=10,sticky='w')
    min_value = ttk.Entry(content, style="TEntry")
    min_value.grid(row=14, column=1, pady=10)

    q4_lbl3=tk.Label(content, text="*Incase you fail to input in above fields Current time will be Considered.", bg='black', fg='white' ,font=('Arial', 8,"bold"))
    q4_lbl3.grid(row=15, column=0,columnspan=3, padx=20,sticky='w')

    add_btn = tk.Button(content, text='Add', command=lambda: q4(hour_value,min_value,1, answer_lbl), bg='brown', font=('Arial', 10))
    add_btn.grid(row=16, column=0, padx=10)
    display = tk.Button(content, text='Display', command=lambda: q4(hour_value,min_value,2, answer_lbl), bg='brown', font=('Arial', 10))
    display.grid(row=16, column=1, padx=10)
    display = tk.Button(content, text='Convert', command=lambda: q4(hour_value,min_value,3, answer_lbl), bg='brown', font=('Arial', 10))
    display.grid(row=16, column=2, padx=10)

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

