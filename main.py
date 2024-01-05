import tkinter as tk
import customtkinter as ctk
from tkinter import ttk 
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
app.title("YT / IMAGE - program!")
# TABBED WIGET 
tabs = ttk.Notebook(app)
tab1 = ttk.Frame(tabs)
tab2 = ttk.Frame(tabs)

tabs.add(tab1, text = "Downloader")
tabs.add(tab2, text = "Remove Bacground")
tabs.pack(expand=1, fill = "both")



# TABBED WIGET
#First Tab
title = ctk.CTkLabel(tab1, text="Insert YT link:", text_color="red")
title.pack(padx= 10, pady= 10)

url_text = tk.StringVar()
link = ctk.CTkEntry(tab1, width=300, height=50, textvariable=url_text)
link.pack()

finishLabel = ctk.CTkLabel(tab1, text="")
finishLabel.pack()

progressPercents = ctk.CTkLabel(tab1, text="0%", text_color="black")
progressPercents.pack()

progressBar = ctk.CTkProgressBar(tab1, width=300)
progressBar.set(0)
progressBar.pack(padx= 10, pady= 10)

download = ctk.CTkButton(tab1, text="DOWNLOAD", command=downloadfilm)
download.pack(padx= 10, pady= 10)

### Secound tab




app.mainloop()