from tkinter import *

ventana = Tk()
ventana.title("Audio")
ventana.geometry("800x600")

etiqueta = Label(ventana, text="Esto es un label")
etiqueta.pack()

segundaEtiqueta = Label(ventana, text="Segunda Etiqueta")
segundaEtiqueta.pack()

ingresoTexto = Entry(ventana)
ingresoTexto.pack()

boton = Button(ventana, text="Texto del boton")
boton.pack()


ventana.mainloop()
