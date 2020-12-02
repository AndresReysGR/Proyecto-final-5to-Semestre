from tkinter import *
import pyaudio 
import numpy as np
import wave


ventana = Tk()
ventana.title("Audio")
ventana.geometry("800x600")

#etiqueta = Label(ventana, text="Esto es un label")
#etiqueta.pack()

segundaEtiqueta = Label(ventana, text="Audio")
segundaEtiqueta.pack()

#ingresoTexto = Entry(ventana)
#ingresoTexto.pack()


#Formato de audio de microfono
PROFUNDIDAD_BITS = pyaudio.paInt16
CANALES = 1 
FRECUENCIAS_MUESTREO = 44100

SEGUNDOS_GRABACION = 2

#Tamaño de CHUNK
CHUNK = 2048

window = np.blackman(CHUNK)


strcuerda=StringVar()
strcuerda.set("")

strfrecuencia=StringVar()
strfrecuencia.set("")

strafinar=StringVar()
strafinar.set("")


def iniciar():

    def analizar(stream):
        data = stream.read(CHUNK, exception_on_overflow=False)
        #"2048h"
        waveData = wave.struct.unpack("%dh"%(CHUNK), data) 
        npData = np.array(waveData) 

        dataEntrada = npData * window

        fftData = np.abs(np.fft.rfft(dataEntrada))

        indiceFrecuenciaDominate = fftData[1:].argmax() + 1

        #Cambio de indice a Hz

        y0,y1,y2 = np.log(fftData[indiceFrecuenciaDominate-1: indiceFrecuenciaDominate+2])
        x1 = (y2 - y0) * 0.5 / (2 * y1 - y2 - y0)
        fDominante = (indiceFrecuenciaDominate+x1)*FRECUENCIAS_MUESTREO/CHUNK
        frecuencia = str(fDominante) 
        print("Frecuencia dominante: " + str(fDominante)+ "Hz", end='\r') 
        


        tolerancia=15
        rango = 1.3
        

        if fDominante > 82.4 - tolerancia and fDominante < 82.4 + tolerancia:
            cuerda= "6ta cuerda tono Mi(e) con una frecuencia de 82.40Hz"
            if fDominante > 82.4 - rango and fDominante < 82.4 + rango:
                afinar = "La afinacion es correcta"
            elif fDominante < 82.4 + rango:
                afinar = "Es necesario apretar la cuerda"
            else:
                afinar = "Es necesario aflojar la cuerda"
        elif fDominante > 110.00 - tolerancia and fDominante < 110.00 + tolerancia:
            cuerda= "5ta cuerda tono La(a) con una frecuencia de 110.00"
            if fDominante > 110.00 - rango and fDominante < 110.00 + rango:
                afinar = "La afinacion es correcta"
            elif fDominante < 110.00 + rango:
                afinar = "Es necesario apretar la cuerda"
            else:
                afinar = "Es necesario aflojar la cuerda"
        elif fDominante > 146.83 - tolerancia and fDominante < 146.83 + tolerancia:
            cuerda= "4ta cuerda tono Re(d) con una frecuencia de 146.83"
            if fDominante > 146.83 - rango and fDominante < 146.83 + rango:
                afinar = "La afinacion es correcta"
            elif fDominante < 146.83 + rango:
                afinar = "Es necesario apretar la cuerda"
            else:
                afinar = "Es necesario aflojar la cuerda"
        elif fDominante > 196.00 - tolerancia and fDominante < 196.00 + tolerancia:
            cuerda= "3ra cuerda tono Sol(g) con una frecuencia de 196.00"
            if fDominante > 196.00 - rango and fDominante < 196.00 + rango:
                afinar = "La afinacion es correcta"
            elif fDominante < 196.00 + rango:
                afinar = "Es necesario apretar la cuerda"
            else:
                afinar = "Es necesario aflojar la cuerda"       
        elif fDominante > 246.94 - tolerancia and fDominante < 246.94 + tolerancia:
            cuerda= "2da cuerda tono Si(b) con una frecuencia de 246.94"
            if fDominante > 246.94 - rango and fDominante < 246.94 + rango:
                afinar = "La afinacion es correcta"
            elif fDominante < 246.94 + rango:
                afinar = "Es necesario apretar la cuerda"
            else:
                afinar = "Es necesario aflojar la cuerda"   
        elif fDominante > 329.63 - tolerancia and fDominante < 329.63 + tolerancia:
            cuerda= "1ra cuerda tono Mi(e) con una frecuencia de 329.63"
            if fDominante > 329.63 - rango and fDominante < 329.63 + rango:
                afinar = "La afinacion es correcta"
            elif fDominante < 329.63 + rango:
                afinar = "Es necesario apretar la cuerda"
            else:
                afinar = "Es necesario aflojar la cuerda"         
        else:
            cuerda = "no se escucha correctamente"

        strcuerda.set(cuerda)
        strfrecuencia.set(frecuencia)
        strafinar.set(afinar)
       
    if __name__ == "__main__":
        p = pyaudio.PyAudio()
        stream = p.open(format=PROFUNDIDAD_BITS, channels=CANALES,
        rate=FRECUENCIAS_MUESTREO, input=True, frames_per_buffer=CHUNK)

        for i in range(0, int(FRECUENCIAS_MUESTREO * SEGUNDOS_GRABACION/CHUNK)):
            analizar(stream)

        stream.stop_stream()
        stream.close()
        p.terminate()


boton = Button(ventana, text="Iniciar", command = iniciar)
boton.pack()

cuerdaEtiqueta = Label(ventana, textvariable=strcuerda)
cuerdaEtiqueta.pack()

frecuenciaEtiqueta = Label(ventana, text="frecuencia actual")
frecuenciaEtiqueta.pack()

frecEtiqueta = Label(ventana, textvariable=strfrecuencia)
frecEtiqueta.pack()

afinarEtiqueta = Label(ventana, textvariable=strafinar)
afinarEtiqueta.pack()

ventana.mainloop()
