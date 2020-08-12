#ignore esta clase rey, solo estaba haciendo una prueba para las interfaces
import tkinter


def actBut():
    print("Hola Bro")


ventana = tkinter.Tk()
ventana.geometry("500x500")
etiqueta = tkinter.Label(ventana)
etiqueta.pack()



caja = tkinter.Entry(ventana)
caja.pack( )

def textoCaja():
    texto = caja.get()
    etiqueta["text"] = texto
    

buttonInicio = tkinter.Button(ventana, text="START", padx=40, pady=10,
                              command=textoCaja)
buttonInicio.pack()

ventana.mainloop()
