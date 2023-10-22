import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image
from ttkthemes import ThemedStyle

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
app.title("Custom Image Format Converter")

# Change the window icon
app.iconbitmap("./lib/icons/convert.ico")  # Replace "your_icon.ico" with the path to your icon file

# Apply a modern theme using ttkthemes
style = ThemedStyle(app)
style.set_theme("vista")

# Create and configure widgets
frame = ttk.Frame(app)
frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Custom Header Frame
header_frame = ttk.Frame(app)
header_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Custom Header Title
header_title = ttk.Label(header_frame, text="Custom Image Format Converter", font=("Helvetica", 16, "bold"))
header_title.grid(row=0, column=0, padx=10, pady=10)

# Input Format
input_format_label = ttk.Label(frame, text="Input Format:")
input_format_var = ttk.Combobox(frame, values=list(image_formats.keys()))
input_format_var.set("ICO")

# Output Format
output_format_label = ttk.Label(frame, text="Output Format:")
output_format_var = ttk.Combobox(frame, values=list(image_formats.keys()))
output_format_var.set("PNG")

# Convert Button
convert_button = ttk.Button(frame, text="Convert Image", command=convert_image)

# Result Label
result_label = ttk.Label(frame, text="")

# Layout widgets
input_format_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
input_format_var.grid(row=0, column=1, padx=10, pady=10, sticky="w")
output_format_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
output_format_var.grid(row=1, column=1, padx=10, pady=10, sticky="w")
convert_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Create a centered label to act as a spacer
center_label = ttk.Label(frame, text="", width=20)
center_label.grid(row=0, column=2, rowspan=4)

# Start the GUI application
app.mainloop()
