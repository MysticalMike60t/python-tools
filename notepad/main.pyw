from tkinter import filedialog
from tkinter import Tk, Menu, Text

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text.delete('1.0', Tk().END)
            text.insert(Tk().END, file.read())

def save_file(event=None):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get('1.0', Tk().END))

app = Tk()
app.title("Notepad")

app.iconbitmap('./lib/icons/note.ico')

menu = Menu(app)
app.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)

app.bind("<Control-s>", save_file)

text = Text(app)
text.pack()

app.mainloop()
