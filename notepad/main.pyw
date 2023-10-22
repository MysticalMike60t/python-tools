import tkinter as tk
from tkinter import filedialog, Text, Menu
from tkinter import ttk

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text.delete('1.0', tk.END)
            text.insert(tk.END, file.read())

def save_file(event=None):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get('1.0', tk.END))

app = tk.Tk()
app.geometry("800x600")

app.iconbitmap('./lib/icons/note.ico')

style = ttk.Style()
style.theme_use('clam')

app.title("Notepad")

menu = Menu(app)
app.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)

app.bind("<Control-s>", save_file)

frame = ttk.Frame(app)
frame.pack(fill=tk.BOTH, expand=True)

text = Text(frame)
text.pack(fill=tk.BOTH, expand=True)

app.mainloop()
