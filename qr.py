import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import qrcode

def generate_qrcode():
    text = url_entry.get()  
    name = img_place.get()  
    
    if not text or not name:
        messagebox.showwarning("Input Error", "Both fields are required.")
        return
    
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4
        )
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(name)
        messagebox.showinfo("Success", f"QR code saved as {name} in C:\\Users\\jaker\\ansel")
        img_tk = ImageTk.PhotoImage(img)
    except Exception as e:
        messagebox.showerror("Error", str(e))


window = tk.Tk()
window.title("QR CODE GENERATOR")
window.config(background="blue")


tk.Label(window, text="Enter The URL:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
url_entry = tk.Entry(window, width=40)
url_entry.grid(row=0, column=1, padx=10, pady=10)


tk.Label(window, text="Enter the image name with extension you want to save it as:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
img_place = tk.Entry(window, width=40)
img_place.grid(row=1, column=1, padx=10, pady=10)


gen_but = tk.Button(window, text="Generate QR Code", command=generate_qrcode)
gen_but.grid(row=2, column=1, padx=10, pady=10)



window.mainloop()
