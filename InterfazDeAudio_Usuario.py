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



def iniciar():
    terceraEtiqueta = Label(ventana, text="etiqueta1")
    terceraEtiqueta.pack()
    cuartaEtiqueta = Label(ventana, text="etiqueta2")
    cuartaEtiqueta.pack()
    quintaEtiqueta = Label(ventana, text="etiqueta3")
    quintaEtiqueta.pack()


boton = Button(ventana, text="Iniciar", command = iniciar)
boton.pack()

ventana.mainloop()
