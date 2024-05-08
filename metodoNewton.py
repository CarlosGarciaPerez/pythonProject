# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 23:00:10 2021

@author: PC-GARCIA
"""

import sympy as sp
import os
import matplotlib.pyplot as plt   # libreria pàra graficar


#print("funcion F(x) =x^3 + 4x^2 - 10 \n")

# se declara la funcion para evaluar la expresion matematica
def fx(x):   
     return eval(ec)
 
def dfx(x):   
     return eval(dx)
 
ejex = range(-100, 100)     

# INGRESO
#fx = lambda x: x**3 + 4*x**2 - 10 
#dfx = lambda x: 3*x**2 + 8*x**1 
listXi=[]   # arreglo que almacena valor de Xi
tolera = 0.000001
i=0
ejeXi=[]    # arreglo de ejer X con valor  Xi
ejeY=[]     # arreglo de ejer Y con valor  f(xi)

os.system ("cls") 
print("\n\n Este programa realiza el NEWTON - RAPHSON\n ")

ec=input('De la funcion a resolver: ') 
x = sp.Symbol('x') 
#Utilizamos el método init_printing
sp.init_printing(use_unicode=True)
y = ec 
dxTem=sp.diff(y,x)  #calcula la derivada
dx= str(dxTem)  #convierte a string
x0 =  float( input("Introduce el valor inicial de Xi : "))

tramo = abs(2*tolera)
print("\n")
# PROCEDIMIENTO
print("i ", " ", "Xi "," "," f(xi) "," "," df(xi) ", " ",  " error")

xi = x0


while (tramo>=tolera):       
     fxi = round(fx(xi),6)
     dfxi = round(dfx(xi),6)
     xnuevo = xi - fxi/dfxi
     #tramo  = abs(x-xi)
     tramo  = abs(xnuevo-xi)
     listXi.append(xi) 
     ejeXi.append(xi)
     ejeY.append(fxi)
     
     error = round(abs(listXi[i] - listXi[i-1]), 6)
     print(i+1," ",xi," ", fxi, " ",dfxi," ", error )
     i=i+1
     xi = round(xnuevo,6)
     
     
print("\n El valor de la solucion  es x : ", round(xi,6))
print("\n cuando f(x), es = 0; es decir, pasa por la raiz")  

i=0 
plt.plot(ejeXi,ejeY)  #grafica los valores de Xi y f(xi)  
plt.plot(ejex, [fx(i) for i in ejex])       
plt.show()        
