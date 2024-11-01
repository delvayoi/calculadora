from tkinter import *
raiz=Tk()
miframe=Frame(raiz)
miframe.pack()
#--------------pantalla----------------#
numeroPantalla=StringVar()

pantalla=Entry(miframe, textvariable=numeroPantalla)
pantalla=Entry(miframe)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4 )
pantalla.config(background="black", fg="#03f943", justify="right")

#--------------pulsaciones de teclado----------------#
def numeroPulsado(num):
    numeroPantalla.set(numeroPantalla.get() + num)

#--------------fila 1-------------------#
boton7=Button(miframe, text="CE", width=3, command=lambda:numeroPulsado(""))
boton7.grid(row=2, column=1)

boton8=Button(miframe, text="C", width=3, command=lambda:numeroPulsado(""))
boton8.grid(row=2, column=2)

boton9=Button(miframe, text="←", width=3, command=lambda:numeroPulsado(""))
boton9.grid(row=2, column=3)

botonMult=Button(miframe, text="÷", width=3, command=lambda:numeroPulsado(""))
botonMult.grid(row=2, column=4)
#--------------fila 2-------------------#
boton7=Button(miframe, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=3, column=1)

boton8=Button(miframe, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=3, column=2)

boton9=Button(miframe, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=3, column=3)

botonMult=Button(miframe, text="x", width=3, command=lambda:numeroPulsado(""))
botonMult.grid(row=3, column=4)
#--------------fila 3-------------------#
boton4=Button(miframe, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=4, column=1)

boton5=Button(miframe, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=4, column=2)

boton6=Button(miframe, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=4, column=3)

botonMenos=Button(miframe, text="-", width=3, command=lambda:numeroPulsado(""))
botonMenos.grid(row=4, column=4)
#--------------fila 4-------------------#
boton1=Button(miframe, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=5, column=1)

boton2=Button(miframe, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=5, column=2)

boton3=Button(miframe, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=5, column=3)

botonSuma=Button(miframe, text="+", width=3, command=lambda:numeroPulsado("+"))
botonSuma.grid(row=5, column=4)
#--------------fila 5-------------------#
botonMasMenos=Button(miframe, text="±", width=3, command=lambda:numeroPulsado("±"))
botonMasMenos.grid(row=6, column=1)

boton0=Button(miframe, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=6, column=2)

botonComa=Button(miframe, text=".", width=3, command=lambda:numeroPulsado("."))
botonComa.grid(row=6, column=3)

botonIgual=Button(miframe, text="=", width=3, command=lambda:numeroPulsado("="))
botonIgual.grid(row=6, column=4)

raiz.mainloop()