from pytube import YouTube
import tkinter as tk
import os
from tkinter import messagebox

def video():     
    yt =YouTube(str(link.get()))
    video = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
    print(yt.streams)
    video.download('/Desktop')
    tk.Label(window, text = 'Mp4 İndirildi', font = 'arial 15',fg="White",bg="#757575").place(x= 10 , y = 140)
def müzik():
    yt1 = YouTube(str(link.get()))
    music = yt1.streams.filter(only_audio=True).first()
    print(yt1.streams)
    music.download('/Desktop')
    tk.Label(window, text = 'Mp3 İndirildi', font = 'arial 15',fg="White",bg="#757575").place(x= 10 , y = 140)
def yama():
    messagebox.showinfo("Bilgilendirme", "Bu sürüm v2 sürümüdür.v3 sürümünde altyazı seçeneği getirilecektir.")
def bilgilen():
    messagebox.showinfo("Bilgilendirme", "Proje ne zaman üretildi 17.02.2023 16.15")
    messagebox.showinfo("Bilgilendirme", "Kim tarafından üretildi: Mehmet Efe Servili")

window = tk.Tk()
window.geometry("600x200")
window.config(bg="#e1dfe0")
window.resizable(width=False,height=False)
window.title('YouTube Video Downloader | Created by AGO Roboteam')

 
link = tk.StringVar()
link_enter = tk.Entry(window, width = 53,textvariable = link,font = 'arial 15 bold',bg="gray").place(x = 5, y = 100)
tk.Label(window, text = 'Lütfen linkinizi buraya giriniz:', font = 'arial 20 bold',fg="gray",bg="#e1dfe0").place(x= 5 , y = 60)
tk.Button(window,text = 'Mp4', font = 'arial 15 bold' ,fg="white",bg = 'gray', padx = 2,command=video).place(x=350 ,y = 140)
tk.Button(window,text = 'Mp3', font = 'arial 15 bold' ,fg="white",bg = 'gray', padx = 2,command=müzik).place(x=420 ,y = 140)
tk.Button(window,text = 'Bilgilendirme İçin Tıklayınız', font = 'arial 15 bold' ,fg="white",bg = 'gray', padx = 2,command=bilgilen).place(x=250 ,y = 15)
tk.Button(window,text = 'Yama Notları', font = 'arial 15 bold' ,fg="white",bg = 'gray', padx = 2,command=yama).place(x=20 ,y = 15)



window.mainloop()


