import tkinter as tk
import customtkinter as ctk
from pytube import YouTube

def downloadfilm():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded")
    except Exception as exc:
        print(exc)
        finishLabel.configure(text="Error", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    sum_size = stream.filesize
    bytes_downloaded = sum_size - bytes_remaining
    percent_downloaded = bytes_downloaded / sum_size * 100
    per = str(int(percent_downloaded))

    progressPercents.configure(text=per + "%")
    progressPercents.update()

    progressBar.set(float(percent_downloaded / 100))

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

finishLabel = ctk.CTkLabel(app, text="")
finishLabel.pack()

progressPercents = ctk.CTkLabel(app, text="0%")
progressPercents.pack()

progressBar = ctk.CTkProgressBar(app, width=300)
progressBar.set(0)
progressBar.pack(padx= 10, pady= 10)

download = ctk.CTkButton(app, text="DOWNLOAD", command=downloadfilm)
download.pack(padx= 10, pady= 10)


app.mainloop()