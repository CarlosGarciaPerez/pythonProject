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
#print("i  ", "x0 ","    "," X1 ","    "," f(x0) ", "    "," f(x1) ", "    "," Xi", "     "," f(xi) ",  "     "," error")
print('{0:<4}{1:^12}{2:^12}{3:^12}{4:^12}{5:^12}{6:^12}{7:^12}'
          .format("i", "x0", "x1", "fx0", "fx1", "xi", "fxi", "error"))
while abs(error) > toleranciaError :   
    #try:
    fx0= round(fx(x0),6)    
    fx1= round(fx(x1),6)  
    xi = round(x1 - (fx(x1)*(x1-x0))/(fx(x1)-fx(x0)),6)
    fxi = round(fx(xi),6)     
    raiz.append(xi)
    ListaXi.append(xi)
    ListaEjeX.append(xi)
    ListaFxi.append(fxi)
    error=round(abs(raiz[i]-raiz[i-1]),6)
     
    j=j+1
    i=i+1
    #print(j," ", x0,"  ", x1, "  ",fx0 ,"  ", fx1 ,"  ", xi, "  ", fxi,  "  ",   error )
    print('{0:<4}{1:<12}{2:<12}{3:<12}{4:<12}{5:<12}{6:<12}{7:<12}'
          .format(j, x0, x1, fx0, fx1, xi, fxi, error ))
          
    x0 = x1
    x1 = xi 
    
    
  #except ZeroDivisionError:
  #    print ("Fin de iteraciones ")
  
plt.plot(ListaEjeX,ListaFxi)  #grafica los valores de Xi y f(xi)      
plt.show()       
