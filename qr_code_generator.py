#importing libraries
import tkinter as tk
from urllib.parse import urlparse
import qrcode
from PIL import Image, ImageTk
from tkinter import filedialog


# Create a function to validate URL
def is_valid_url(url):
    parsed_url = urlparse(url)
    return parsed_url.scheme and parsed_url.netloc  #checks if ulr has a scheme and netloc, which are required for a valid URL

# Create a function to generate QR code
def generate_qrcode():
    url = entry.get().strip() #get the URL from the entry box and remove any leading/trailing whitespace

    if url == "":
        msg_lbl.config(text="Please enter a URL", fg="red") #display message if URL is empty
        return

    if is_valid_url(url):
        # Open a file picker window
        filepath = filedialog.asksaveasfilename(
            initialfile="qrcode.png",
            defaultextension=".png",
            filetypes=[("PNG files", "*.png")],
        )

        # Handle Cancel
        if not filepath:
            msg_lbl.config(text="Save Cancelled!", fg="red") #display message if save is cancelled
            return

        # Generate the QR code
        img = qrcode.make(url) #generate the QR code image

        # Save image
        img.save(filepath) #save the QR code image to the specified filepath

        # Resize the image to fit in the GUI
        img = img.resize((200, 200)) #resize the image to 200x200 pixels

        # Convert the image into Tkinter format
        tk_img = ImageTk.PhotoImage(img) #convert the image to a format that can be displayed in Tkinter

        # Display the image inside qr_lbl
        qr_lbl.config(image=tk_img)

        # Prevent the image from disappearing
        qr_lbl.image = tk_img

        # Display the success message
        msg_lbl.config(text="QR Code generated successfully!", fg="green") #display success message

    else:
        msg_lbl.config(text="Invalid URL. Please enter a valid URL.", fg="red") #display message if URL is invalid



# Building the GUI interface
root = tk.Tk() #main window
root.title("QR Code Generator") #title of the window
root.geometry("400x400") #size of the window
root.configure(bg="#e3acdc") #background color of the window

#Create a Label
tk.Label(root, text="Enter URL: ", font=("Century Gothic", 12), bg="#41d2bd").pack(pady=10) #label for the URL entry

#Create an Entry box
entry = tk.Entry(root, width=40, font=("Century Gothic", 12)) #entry box for the URL
entry.pack(pady=10) #packing the entry box

#Create a Button to generate QR code
btn = tk.Button(root, text="Generate QR Code", font=("Century Gothic", 12), bg="#600854", fg="white", command=generate_qrcode) #button to generate QR code
btn.pack(pady=10) #packing the button

#Create a Label
msg_lbl = tk.Label(root, font=("Century Gothic", 12), bg="#a3bdc8") #label to display messages
msg_lbl.pack(pady=10) #packing the message label

# Create a label to display the generated QR code
qr_lbl = tk.Label(root, bg="#e3acdc")
qr_lbl.pack(pady=10)

#Run the app
root.mainloop() #running the main loop of the GUI
