import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image

# Supported image formats
image_formats = {
    "ICO": "ico",
    "PNG": "png",
    "JPEG": "jpeg",
    "GIF": "gif",
    "BMP": "bmp",
    "TIFF": "tiff",
}

def convert_image():
    input_format = input_format_var.get()
    output_format = output_format_var.get()

    file_path = filedialog.askopenfilename(filetypes=[(f"{input_format} files", f"*.{image_formats[input_format]}")])
    if file_path:
        img = Image.open(file_path)
        output_extension = image_formats[output_format]
        output_path = filedialog.asksaveasfilename(defaultextension=f".{output_extension}", filetypes=[(f"{output_format} files", f"*.{output_extension}")])
        if output_path:
            img.save(output_path, format=output_extension)
            result_label.config(text=f"Conversion successful: {output_path}")

# Create the main application window
app = tk.Tk()
app.title("Image Format Converter")

# Modern styles
style = ttk.Style()
style.configure("TButton", padding=5, font=("Helvetica", 12))
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TFrame", background="#f0f0f0")

# Create and configure widgets with modern styles
frame = ttk.Frame(app)
frame.grid(row=0, column=0, padx=10, pady=10)

input_format_label = ttk.Label(frame, text="Input Format:")
input_format_var = tk.StringVar()
input_format_combobox = ttk.Combobox(frame, textvariable=input_format_var, values=list(image_formats.keys()))
input_format_combobox.set("ICO")

output_format_label = ttk.Label(frame, text="Output Format:")
output_format_var = tk.StringVar()
output_format_combobox = ttk.Combobox(frame, textvariable=output_format_var, values=list(image_formats.keys()))
output_format_combobox.set("PNG")

convert_button = ttk.Button(frame, text="Convert Image", command=convert_image)
result_label = ttk.Label(frame, text="", font=("Helvetica", 12))

# Layout widgets with modern styling
input_format_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
input_format_combobox.grid(row=0, column=1, padx=10, pady=10)
output_format_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
output_format_combobox.grid(row=1, column=1, padx=10, pady=10)
convert_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI application
app.mainloop()
