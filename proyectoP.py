#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 01:29:55 2019

@author: Jhonny#26
"""
import numpy as np
import matplotlib.pyplot as plt
import random
#Recibimos una Matriz
def Prom(Matriz):
    
    #Obtenemos las dimensiones de la matriz 
    Ren = Matriz.shape[0]
    Col = Matriz.shape[1]
    aux = np.zeros(Ren)
    for i in range(Col):
        
        suma = 0
        
        for j in range (Ren):
            
            suma += Matriz[i][j]
        
        #Obteniendo el promedio
        aux[i] = suma / Ren
    return aux

#Proceso principial que recibe la matriz a analizar
def Process(Matriz):
    Ren = 5
    Col = 5
    
    Matriz = np.zeros((Ren,Col))
    for i in range (Col):
        for j in range(Ren):
            Matriz[i][j] = random.randint(1,23)
    #print(Matriz)
    #Obteniendo el vector de los promedios
    Promedios = Prom(Matriz)
    
    plt.figure()
    for i in range(Col):
        cad = "Empresa "+str(i+1)
        plt.plot(Matriz[:][i],label = cad)
        #print(Matriz[:][i])
    
    
    plt.plot(Promedios,label = "Promedio",color= "Black")
       
    plt.xlabel("Categorías")
    plt.ylabel("Valores por Empresa")
    plt.title("Categoría Mensual")
    
    plt.xlim(0,4)
    plt.ylim(0,23)
    
    plt.grid()
    plt.legend(loc = "upper right")
    for i in range (Col):
        print("\n\tCambio Columna")
        for j in range (Ren):
            Resta = Matriz[j][i]-Promedios[i]
            print("Diferencia entre Valor y promedio de la empresa: ",j+1," : ", int(Resta))
    plt.show()
    
    


Holi = np.zeros((5,5))
Process(Holi)