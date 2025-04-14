#Fin en mente: Que el botón huya
#Autor: Adriana Alonzo (e22.adrianamaria.alonzom@suizoamericano.edu.gt)
#Descripción: El programa debe mostrar un botón y cada vez que el cursor se acerce el botón se aleje 
#Recursos: Intérprete de python
#Procesos previos: -----
#Historia: 
#  000 Creación del programa 18/3/25 
#Ajustes pendientes: -----
from tkinter import * 
from random import randint
class app(Tk): 
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.config(bg="purple")
        self.title("Botón que huye - ADRIANA ALONZO")
        self.btn = Button(text="Apáchame... si puedes")
        self.btn.place(x=100,y=100)
        self.btn.bind("<Enter>",self.mover)
    def mover(self, e): #se usa un parámetro para información del evento en este caso "e"
        #Ancho y alto de la ventana
        anchov = self.winfo_width()
        altov = self.winfo_height()
        #Ancho y alto del botón
        anchob = self.btn.winfo_width()
        altob = self.btn.winfo_height()
        px = randint(0, anchov - anchob)
        py = randint(0, altov - altob)
        self.btn.place(x=px,y=py)
app().mainloop()
