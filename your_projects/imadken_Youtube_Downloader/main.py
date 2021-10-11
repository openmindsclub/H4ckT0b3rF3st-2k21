
from tkinter import *
from pytube import YouTube
import pytube




root = Tk()

root.geometry('500x300+500+200')


root.resizable(0,0)

root.configure(background="tomato")

root.title("Youtube downloader")

video_link = StringVar()

Label(root, text = 'Enter the link:', font=  'Modern',bg="white").place(x= 180 , y = 60)

link_enter = Entry(root,width = 70,textvariable = video_link).place(x = 40, y = 110)

def Downloader(): 
    
    
        url =YouTube(str(video_link.get()))

    
        # video = url.streams.get_by_resolution("enter the resolution here")

        # video = url.streams.get_audio_only()   
    
        video = url.streams.get_highest_resolution()

        video.download(r"Enter the path where you want to save the video") # Otherwise it will be saved in the cwd
    
    
        Label(root, text = 'DOWNLOADED!!', font = 'Modern').place(x= 190 , y = 200) 


Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'white', padx = 2, command = Downloader,activebackground='green').place(x=170 ,y = 150)



root.mainloop()

