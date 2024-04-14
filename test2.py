import subprocess
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Global variable to store the root window
root = None

# Function to install required packages
def install_packages():
    req = ['pillow', 'requests']
    for package in req:
        subprocess.run(['pip', 'install', package])
    print('\033[2J\033[H', end='')
    print('\033[96m' + 'loading Gui please wait...' + '\033[0m')

# Function to display the logo
def display_logo(root, url):
    response = requests.get(url)
    image_data = response.content
    image = Image.open(BytesIO(image_data))
    image = image.resize((300, 300), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo, bg=root["bg"])
    label.image = photo
    label.pack(pady=0)

# Function to reload the window
def reload_gui():
    global root
    if root:
        print('\033[91m' + 'you Initiated a reload\nNow I`m terminating the current window\n ' + '\033[0m')
        print('\033[32m'+'Opening new window now !\n'+'\033[0m')
        root.destroy()  # Destroy the current window
    root = tk.Tk()  # Create a new root Tk instance
    gui(root)

# Function to shake the window
def shake(root):
    dx = 5  # Initial displacement
    for _ in range(5):  # Adjust the range to control the intensity of the shake
        root.geometry(f"450x750+{root.winfo_x() + dx}+{root.winfo_y()}")  # Move the window to the right
        root.update()
        root.geometry(f"450x750+{root.winfo_x() - dx}+{root.winfo_y()}")  # Move the window to the left
        root.update()
        dx *= -1  # Reverse the direction of displacement

# Temporary Function to handle submission
def submit(age_value, email_value, answer_lbl):
    age = age_value.get()  
    email = email_value.get()
    x = f'age is : {age} , email is : {email}'
    answer_lbl.config(text=x)

# Function to close the window
def killer():
    global root
    if root:
        root.destroy()

# Function to calculate factorial
def fact(n):
    return 1 if n == 0 else n * fact(n - 1)

# Function to compute factorial and handle invalid entries
def factorial(fact_value, answer_lbl):
    try:
        n = abs(int(fact_value.get()))
        res = fact(n)
        answer_lbl.config(text=res)
    except ValueError:
        answer_lbl.config(text='INVALID')
        shake(root)  # Shake the window if an invalid entry is made

# GUI
def gui(root):
    root.title("Nyctophile")
    root.minsize(width=450, height=750)
    root.maxsize(width=450, height=root.winfo_screenheight()) 
    root.config(background='black')
    root.option_add("*Font", "Times 16 bold")
    root.option_add("*Foreground", "white")
    root.option_add("*Label.Background", root["bg"])

    ttk.Style().theme_use("alt")
    style = ttk.Style()
    style.configure("TEntry", borderwidth=2, relief="solid", padding=5, bordercolor="black")

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

    # Bind the frame to the canvas
    frame.bind("<Configure>", lambda event, canvas=canvas: on_frame_configure(canvas))
    frame.bind_all("<MouseWheel>", lambda event, canvas=canvas: on_mousewheel(event, canvas))
    frame.bind_all("<KeyPress-Up>", lambda event, canvas=canvas: on_arrow_key(event, canvas))
    frame.bind_all("<KeyPress-Down>", lambda event, canvas=canvas: on_arrow_key(event, canvas))

    rld_btn = tk.Button(frame, text='refresh', bg='brown', font=('Arial', 8),command=reload_gui)
    rld_btn.pack(side=tk.TOP, anchor=tk.NE,padx=30,pady=5)
    
    # Display the logo
    hawk_logo_url = "https://i.ibb.co/RYg12BN/full-LOGO.jpg"
    display_logo(frame, hawk_logo_url)
    
    # Header
    name = tk.Label(frame, text="Shanu Martin", bg='black', fg='white')
    name.pack(side=tk.TOP,pady=0)

    # Answer Section
    answer_container = tk.Frame(frame, bg='white', width=400, height=100, relief="solid", bd=5)
    answer_container.pack(anchor="nw", pady=10, padx=50)

    # Answer Frame with Label inside
    answer_frame = tk.Frame(answer_container, bg='white', width=350, height=100, borderwidth=5, relief="ridge", highlightbackground="black")
    answer_frame.pack_propagate(False)  # Prevent the frame from resizing to fit its contents
    answer_frame.pack()

    answer_lbl = tk.Label(answer_frame, text="Answers to your question will be here !", font=("Verdana", 8), bg='white', fg='black')
    answer_lbl.pack(pady=5, padx=5, fill='both', expand=True)  # Make the label fill the frame

    # Content
    content = tk.Frame(frame, bg='black')
    content.pack(anchor="nw", pady=10, padx=3)

    # Age Section
    age_lbl = tk.Label(content, text="Age", bg='black', fg='white')
    age_lbl.grid(row=0, column=0, padx=20)
    age_value = ttk.Entry(content, style="TEntry")
    age_value.grid(row=0, column=1)
    age_btn = tk.Button(content, text='ok', command=lambda: submit(age_value, email_value, answer_lbl), bg='brown', font=('Arial', 10))
    age_btn.grid(row=0, column=2, padx=20)

    # Email Section
    email_lbl = tk.Label(content, text="Email", bg='black', fg='white')
    email_lbl.grid(row=1, column=0, padx=20, pady=10)
    email_value = ttk.Entry(content, style="TEntry")
    email_value.grid(row=1, column=1, pady=10)

    # ------------------------------------------------------------------------
    # Fact Section
    fact_lbl = tk.Label(content, text="Factorial", bg='black', fg='white')
    fact_lbl.grid(row=2, column=0, padx=20)
    fact_value = ttk.Entry(content, style="TEntry")
    fact_value.grid(row=2, column=1)
    fact_btn = tk.Button(content, text='ok', command=lambda: factorial(fact_value, answer_lbl), bg='brown', font=('Arial', 10))
    fact_btn.grid(row=2, column=2, padx=20)

    # trash
    for i in range(3, 15):
        e_lbl = tk.Label(content, text="Trash", bg='black', fg='white')
        e_lbl.grid(row=i, column=0, padx=20, pady=10)
        e_value = ttk.Entry(content, style="TEntry")
        e_value.grid(row=i, column=1, pady=10)

    # Exit Button
    btn = tk.Button(frame, text='exit', command=killer, bg='dark gray', font=('Arial', 14))
    btn.pack()

    # footer 
    foot = tk.Label(frame, text='Made by shanu as template for Datapy daily tasks', bg='white', fg='black', font=("Verdana", 8, "bold"))
    foot.pack(side=tk.BOTTOM, fill='x',pady=5)


   
    root.mainloop()  #evdey closing window 

# Function to adjust canvas scroll region when widgets are added or removed
def on_frame_configure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

# Function to handle mouse wheel scrolling
def on_mousewheel(event, canvas):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

# Function to handle arrow key scrolling
def on_arrow_key(event, canvas):
    if event.keysym == "Up":
        canvas.yview_scroll(-1, "units")
    elif event.keysym == "Down":
        canvas.yview_scroll(1, "units")

# Install required packages
install_packages()

# Create Tkinter window
root = tk.Tk()

# Run GUI
gui(root) 

print("You are done !")
