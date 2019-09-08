#!/usr/bin/env python
# coding: utf-8

# In[4]:


from tkinter import *# Normal Tkinter.*widgets are not themed!from ttkthemes 
from tkinter.ttk import *
from ttkthemes import ThemedTk
import tkinter.messagebox as msg
import tkinter.font as tkFont
raiz = ThemedTk(theme = 'equilux')
#raiz = ThemedTk(theme = 'scidgreen')
raiz.resizable(0,0)
raiz.title('BBVA')

miFrame = Frame(raiz)
miFrame.pack(expand = 1, fill=BOTH)
#miFrame.config(bg = 'blue')
#miFrame.config(width = '650', height = '350')

Cantidad = StringVar()
Nombre = StringVar()
Resultado = StringVar()

resultado = 0
i = 1
def agregar(x = None):
    global resultado
    numero = cuadroCantidad.get()
    nombre = cuadroNombre.get()
    resultado += float(numero)
    cuadroResultado.config(state = ACTIVE)
    Resultado.set(resultado)
    cuadroResultado.config(state = DISABLED)
    a = [float(numero),'\t \t \t', nombre, '\n']
    TextoLargo.config(state = 'normal')
    for i in range(4):
        TextoLargo.insert(END,a[i])
    TextoLargo.config(state = 'disabled')
    
    Cantidad.set('')
    Nombre.set('')

#Crear cuadro para meter cantidades
nombreCantidad_L = Label(miFrame, text = 'Cantidad: ', font = ('Times', 15, 'bold')).grid(row = 0, column = 0, 
                                                                                          sticky = 'w', 
                                                                                          pady = 5, padx = 20)
cuadroCantidad = Entry(miFrame, textvariable = Cantidad)
cuadroCantidad.grid(row = 1, column = 0, padx = 5)
#cuadroCantidad.config(fg = 'green', justify = 'right')
#Atributo del cuadro donde meteremos cantidades

#Nombre del recuadro de lo que estoy
nombreNombre_L = Label(miFrame, text = 'Nombre: ', font = ('Times', 15, 'bold')).grid(row = 0, column = 1, 
                                                                                      sticky = 'w', 
                                                                                      pady = 5, padx = 0)
#Nombre de lo que estoy metiendo en la base
cuadroNombre = Entry(miFrame, textvariable = Nombre)
cuadroNombre.grid(row = 1, column = 1, padx = 0)
if cuadroCantidad.get() == '':
    cuadroNombre.bind('<Return>', agregar)
#cuadroNombre.config(fg = 'green', justify = 'right')

#Nombre del recuadro grande
TextoLargoLabel = Label(miFrame, text = 'Lista de finanzas: ', font = ('Times', 15, 'bold')).grid(row = 2, column = 0, 
                                                                                                  #sticky = 'w', 
                                                                                                  pady = 5, 
                                                                                                  padx = 0)
#Recuadro grande donde irá guardando las cantidadesinsertadas
TextoLargo = Text(miFrame, width = 42, height = 10, bg = 'grey')#, width = 20, height = 8)
TextoLargo.grid(row = 3, column = 0, padx = 0, pady = 5, columnspan = 2, rowspan = 1)
TextoLargo.config(state = 'disabled')

#Scroll del recuadro grande
scrolly = Scrollbar(miFrame, command = TextoLargo.yview)
scrolly.grid(row = 3, column = 2, sticky = 'nsew')
TextoLargo.config(yscrollcommand  = scrolly.set)

#cuadroResultado.config(fg = 'green', justify = 'right')
nombreResultado_L = Label(miFrame, text = 'Balance: ', font = ('Times', 15, 'bold')).grid(row = 4, column = 0, 
                                                                                          sticky = 'w', 
                                                                                          pady = 10, 
                                                                                          padx = 20)
#Recuadro del resultado de la suma de todas las transacciones
cuadroResultado = Entry(miFrame, textvariable = Resultado)
cuadroResultado.grid(row = 5, column = 0, padx = 0)
cuadroResultado.config(state = DISABLED)

#Nombre del recuadro grande
cuadroRecomendacionLabel = Label(miFrame, text = 'Retroalmentación: ', font = ('Times', 15, 'bold')).grid(row = 6, 
                                                                                                          column = 0, 
                                                                                                          #sticky = 'w', 
                                                                                                          pady = 5, 
                                                                                                          padx = 0)
cuadroRecomendacion = Text(miFrame, width = 42, height = 10, bg = 'grey')
cuadroRecomendacion.grid(row = 7, column = 0, padx = 0, pady = 5, columnspan = 2, rowspan = 7)
                         
#Scroll del recuadro grande
scrolly = Scrollbar(miFrame, command = TextoLargo.yview)
scrolly.grid(row = 7, column = 2, sticky = 'nsew')
cuadroRecomendacion.config(yscrollcommand  = scrolly.set)

raiz.mainloop()

