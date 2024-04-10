from pygame import mixer

class Reporductor:
    archivo = None 
    val_volumen = None
    def __init__(self, archivo):
        self.archivo = archivo
        self.val_volumen = 0
        mixer.init()
        mixer.music.load(archivo)

    def play(self):
        mixer.music.play()
        return "Reproduciendo música"
    
    def pause(self):
        mixer.music.pause()
        return "La música se ha pausado"
    
    def unpasue(self):
        mixer.music.unpause()
        return "La música se ha vuelto a reproducir"
    
    def volumen (self, v):
        self.val_volumen += v

        if(self.val_volumen >= 1):
            self.val_volumen = 1
        elif(self.val_volumen <= 0):
            self.val_volumen = 0
        
        mixer.music.set_volume(self.val_volumen)
        return "El volumen está a ", self.val_volumen