#importing libraries
import tkinter as tk
from urllib.parse import urlparse
import qrcode
from PIL import Image, ImageTk
from tkinter import filedialog

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
btn = tk.Button(root, text="Generate QR Code", font=("Century Gothic", 12), bg="#600854", fg="white", ) #button to generate QR code
btn.pack(pady=10) #packing the button

#Create a Label
msg_lbl = tk.Label(root, font=("Century Gothic", 12), bg="#a3bdc8") #label to display messages
msg_lbl.pack(pady=10) #packing the message label

#Run the app
root.mainloop() #running the main loop of the GUI
