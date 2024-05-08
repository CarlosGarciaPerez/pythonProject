# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 12:03:21 2021

@author: PC-GARCIA
"""

import os
import matplotlib.pyplot as plt   # libreria pàra graficar

os.system ("cls") 
print("\n\nEste programa realiza de la SECANTE\n ")

def fx(x):   
     return eval(ec)

""" """
# Valores del eje X que toma el gráfico.
x = range(-100, 100)

ec=input('De la funcion a resolver: ') 
x0=float(input('Introduce el valor de inicio x0: '))
x1=float(input('Introduce el valor de inicio x1: '))
#toleranciaError=float(input('Introduce el error '))
toleranciaError=-0.00000016
raiz=[0,0]
ListaXi=[1,0]
ListaEjeX=[]
ListaFxi=[]
#raiz.insert(0,0)
i=1
j=1
error=1

print("\n")
print('{0:<4}{1:^12}{2:^12}{3:^12}{4:^12}{5:^12}{6:^12}{7:^12}'
          .format("i", "x0", "x1", "fx0", "fx1", "xi", "fxi", "error"))
while abs(error) > toleranciaError :   
    # #try:
    fx0= fx(x0)   
    fx1= fx(x1)  
    denominador = (fx(x1)-fx(x0))
    if(denominador == 0):  
        break  
    xi = x1 - (fx(x1)*(x1-x0))/(fx(x1)-fx(x0))
    fxi = fx(xi)   
    raiz.append(xi)
    ListaXi.append(xi)
    ListaEjeX.append(xi)
    ListaFxi.append(fxi)
    error=abs(raiz[i]-raiz[i-1])
     
    j=j+1
    i=i+1  
    print('{0:<4}{1:<12}{2:<12}{3:<12}{4:<12}{5:<12}{6:<12}{7:<12}'
          .format(j,round(x0,6), round(x1,6), round(fx0,6), round(fx1,6), round(xi,6), round(fxi,6), round(error,6) ))
          
    x0 = x1
    x1 = xi 
    
    

print("\n El valor de la solucion  es x : ", round(xi,6))
print("\n cuando f(x), es = 0; es decir, pasa por la raiz")    
  #except ZeroDivisionError:
  #    print ("Fin de iteraciones ")
i=0  
plt.plot(ListaEjeX,ListaFxi)  #grafica los valores de Xi y f(xi)  
plt.plot(x, [fx(i) for i in x])

# Establecer el color de los ejes.
plt.axhline(0, color="black")
plt.axvline(0, color="black")

# Limitar los valores de los ejes.
plt.xlim(-100, 100)
plt.ylim(-100, 100)

   
plt.show()       
