import tkinter as tk
import customtkinter as ctk
from pytube import YouTube

def downloadfilm():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
    except Exception as exc:
        print(exc)
    print("Download Complete! :D")

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("360x240")
app.title("Downloader Youtube!")

title = ctk.CTkLabel(app, text="Insert YT link:", text_color="red")
title.pack(padx= 10, pady= 10)

url_text = tk.StringVar()
link = ctk.CTkEntry(app, width=300, height=50, textvariable=url_text)
link.pack()

download = ctk.CTkButton(app, text="DOWNLOAD", command=downloadfilm)
download.pack(padx= 10, pady= 10)


app.mainloop()