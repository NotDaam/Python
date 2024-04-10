from tkinter import *
from tkinter.ttk import *
from Reporductor import *

display = "Reproductor"
musica = Reporductor('wefere.mp3')

def play_musica():
    musica.volumen(0.8)
    display = musica.play()
    label.config(text=display)

def pause_musica():
    display = musica.pause()
    label.config(text=display)

def unpause_musica():
    display = musica.unpasue()
    label.config(text=display)

def vol_mas():
    display = musica.volumen(+0.1)
    label.config(text=display)

def vol_menos():
    display = musica.volumen(-0.1)
    label.config(text=display)

master = Tk()
master.geometry("400x250")

label = Label(master, text = display)
label.pack(padx = 20, pady = 20)

btn_play = Button(master, text = "Reproducir", command = play_musica)
btn_play.pack(padx = 5, pady = 5)

btn_pause = Button(master, text = "Pausar", command = pause_musica)
btn_pause.pack(padx = 5, pady = 5)

btn_unpause = Button(master, text = "Voler a Reproducir", command = unpause_musica)
btn_unpause.pack(padx = 5, pady = 5)

btn_vol_mas = Button(master, text = "Subir Vol.", command = vol_mas)
btn_vol_mas.pack(padx = 5, pady = 5)

btn_vol_menos = Button(master, text = "Bajar Vol.", command = vol_menos)
btn_vol_menos.pack(padx = 5, pady = 5)

mainloop()