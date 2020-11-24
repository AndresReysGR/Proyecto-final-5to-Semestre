from tkinter import *

ventana = Tk()
ventana.title("Audio")
ventana.geometry("800x600")

#etiqueta = Label(ventana, text="Esto es un label")
#etiqueta.pack()

segundaEtiqueta = Label(ventana, text="Audio")
segundaEtiqueta.pack()

#ingresoTexto = Entry(ventana)
#ingresoTexto.pack()

boton = Button(ventana, text="Iniciar")
boton.pack()


ventana.mainloop()
