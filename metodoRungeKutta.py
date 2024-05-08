# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 17:12:03 2021

@author: PC-GARCIA
"""

import os
import matplotlib.pyplot as plt   # libreria pàra graficar

def funcion(x, y):
    return eval(ec)

def rungeKutta(h, x0, y0):
    x = x0 + h
    k1 = h * funcion(x0, y0)
    k2 = h * funcion(x0 + (h/2), y0 + (k1/2))
    k3 = h * funcion(x0 + (h/2), y0 + (k2/2))
    k4 = h * funcion(x0 + h, y0 + k3)
    pendiente = (k1 + 2*k2 + 2*k3 + k4)/6
    y = y0 + pendiente
    return [x, y, k1, k2, k3, k4, pendiente]


print("\n\nEste programa realiza el metodo de Runge Kutta\n ")
ListaEjeX=[]
ListaEjeY=[]
ec=input('De la funcion a resolver: ') 
yAprox = float(input("Aproximar 'y' a : "))
h = float(input("Tamano paso (h) : "))
y0 = float(input("y0 : "))
x0 = float(input("x0 : "))
ListaEjeX.append(x0) 
ListaEjeY.append(y0)
   
iteracion = 0

while(x0 < yAprox):
    resultadoIteracion = rungeKutta(h, x0, y0)
    iteracion += 1
    print ("==================================")
    print ("Iteracion %d\n" %(iteracion))
    print ("K1   = %f" %(resultadoIteracion[2]))
    print ("K2   = %f" %(resultadoIteracion[3]))
    print ("K3   = %f" %(resultadoIteracion[4]))
    print ("K4   = %f" %(resultadoIteracion[5]))
    print ("X(%d) = %f"  %(iteracion, resultadoIteracion[0]))
    print ("Y(%d) = %f" %(iteracion, resultadoIteracion[1]))
    print ("==================================")

    y0 = resultadoIteracion[1]
    x0 = resultadoIteracion[0]
    
    ListaEjeX.append(x0) 
    ListaEjeY.append(y0)
    
plt.plot(ListaEjeX,ListaEjeY)  #grafica los valores de Xi y f(xi)  

# Establecer el color de los ejes.
plt.axhline(0, color="black")
plt.axvline(0, color="black")

# Limitar los valores de los ejes.
plt.xlim(0, 5)
plt.ylim(0, 5)
  
plt.show()       
    
