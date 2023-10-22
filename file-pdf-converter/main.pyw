import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PyPDF2 import PdfFileReader
from docx import Document
from PIL import Image

def pdf_to_text(input_file, output_file):
    try:
        pdf_reader = PdfFileReader(open(input_file, 'rb'))
        text = ''
        for page_num in range(pdf_reader.getNumPages()):
            text += pdf_reader.getPage(page_num).extract_text()
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
        messagebox.showinfo("Success", "Conversion completed successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Conversion failed: {str(e)}")

def image_to_pdf(input_file, output_file):
    try:
        image = Image.open(input_file)
        image.save(output_file, 'PDF')
        messagebox.showinfo("Success", "Conversion completed successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Conversion failed: {str(e)}")

def browse_input_file():
    input_file_path = filedialog.askopenfilename()
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(0, input_file_path)

def browse_output_file():
    output_file_path = filedialog.asksaveasfilename(defaultextension=".pdf")
    output_file_entry.delete(0, tk.END)
    output_file_entry.insert(0, output_file_path)

def convert_file():
    input_file = input_file_entry.get()
    output_file = output_file_entry.get()
    file_ext = input_file.split('.')[-1].lower()

    if file_ext in ('pdf', 'jpg', 'jpeg', 'png'):
        if file_ext == 'pdf':
            if output_file.endswith(".pdf"):
                messagebox.showerror("Error", "Output file format should be different from PDF.")
            else:
                pdf_to_text(input_file, output_file)
        else:
            if not output_file.endswith(".pdf"):
                output_file += ".pdf"
            image_to_pdf(input_file, output_file)
    else:
        messagebox.showerror("Error", "Unsupported file format for conversion")

# Create the main tkinter window
root = tk.Tk()
root.title("Modern File Converter")

# Create frames for better organization
input_frame = tk.Frame(root, bg='white')  # Set background to white
input_frame.pack(pady=10)

output_frame = tk.Frame(root, bg='white')  # Set background to white
output_frame.pack(pady=10)

button_frame = tk.Frame(root, bg='white')  # Set background to white
button_frame.pack(pady=10)

# Configure the style for different widgets
style = ttk.Style(root)
style.theme_use("clam")  # You can change the theme as needed
style.configure("TButton", foreground="black", background="white", font=("Segoe UI", 12))
style.configure("TLabel", foreground="black", font=("Segoe UI", 12))
style.configure("TEntry", font=("Segoe UI", 12))

# Labels and Entry fields
input_file_label = ttk.Label(input_frame, text="Select Input File:")
input_file_label.pack()

input_file_entry = ttk.Entry(input_frame, width=40)
input_file_entry.pack()

browse_input_button = ttk.Button(input_frame, text="Browse", command=browse_input_file)
browse_input_button.pack()

output_file_label = ttk.Label(output_frame, text="Select Output File:")
output_file_label.pack()

output_file_entry = ttk.Entry(output_frame, width=40)
output_file_entry.pack()

browse_output_button = ttk.Button(output_frame, text="Browse", command=browse_output_file)
browse_output_button.pack()

# Convert button
convert_button = ttk.Button(button_frame, text="Convert", command=convert_file)
convert_button.pack()

# Set the window icon (you may need to provide the correct icon path)
# root.iconbitmap('./lib/icons/convert.ico')

# Set the initial window size
root.geometry("400x300")  # Increased the height to accommodate the widgets

# Start the GUI event loop
root.mainloop()
