import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
from pytube import YouTube


def Downloadvid():
    try:
        ytLink = link.get()
        ytObj = YouTube(ytLink,on_progress_callback=onprogress)
        video = ytObj.streams.get_highest_resolution()
        video.download(f'{loc}')
        finished.configure(text="Download Finished!")
    except:
        finished.configure(text="Url Error!")

def onprogress(stream, chunk, bytes_remaining):
    total = stream.filesize
    bytes_downloaded = total - bytes_remaining
    percentage = bytes_downloaded / total * 100
    per = str(int(percentage))
    perc.configure(text=per+ ' %')
    perc.update()
    percbar.set(float(per)/100)

def browse():
    path = filedialog.askdirectory()
    global loc
    loc=''+path+''
    print(loc)

# system settings 
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# framework
app = ctk.CTk()
app.geometry("720x480")
app.title("YouTube Video Downloader")

# ui features

title = ctk.CTkLabel(app, font=('Segoe UI',14), text="Enter the link of the youtube video")
title.pack(padx=10,pady=30)

url=tk.StringVar()
link = ctk.CTkEntry(app, width=350, height=50, textvariable=url)
link.pack()

perc = ctk.CTkLabel(app, text="0 %")
perc.pack(pady=20)

percbar = ctk.CTkProgressBar(app, width=400)
percbar.set(0)
percbar.pack(pady=20)

finished = ctk.CTkLabel(app, text="")
finished.pack(pady=10)

button = ctk.CTkButton(app,text="Download", height=50, width=160, command=Downloadvid)
button.pack(side=tk.LEFT, padx=(135,50),pady=10)

buttonpath = ctk.CTkButton(app, text="Change download path", height=50, width=180, command=browse)
buttonpath.pack(side=tk.LEFT, padx=50)

# run app
app.mainloop() 