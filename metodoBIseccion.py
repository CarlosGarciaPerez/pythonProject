# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 14:44:36 2021

@author: PC-GARCIA
"""

import numpy as np
import math
import os
import sys
import matplotlib.pyplot as plt   # libreria pàra graficar

os.system ("cls") 
print("\n\n Este programa realiza el METODO DE BISECCION\n ")

# INICIO DE VARIABLES
toleranciaError = 0.0001
i=0 # contador de iteraciones
listXi=[]   # arreglo que almacena valor de Xi
ejeXi=[]    # arreglo de ejer X con valor  Xi
ejeY=[]    # arreglo de ejer Y con valor  f(xi)

# se declara la funcion para evaluar la expresion matematica
def fx(x):   
     return eval(ec)
 
x = range(-100, 100)    

# INGRESO por TECLADO
#funcionStrig = input("Introduce la funcion a evaluar: ")
ec=input('De la funcion a resolver: ') 
#fx = lambda ec: eval(ec)
#fx = lambda x: x**3 + 3*x**2 - 50 

a =  float( input("Introduce el valor de a : "))
b =  float( input("Introduce el valor de b : "))
print ("\n")
nIteraciones = math.ceil((math.log(b - a) - math.log(toleranciaError)) / math.log(2))


# PROCEDIMIENTO
getSignfa = np.sign(fx(a))  #Obtiene el signo de la funcion f(a)
getSignfb = np.sign(fx(b))  #Obtiene el signo de la funcion f(a)

if getSignfa == getSignfb:
    print (" NO SE PUEDE realizar este metodo porque "+
           "la f(a) y f(b) tienen el mismo signo \n")
    
    print (" *** ADIOS")
    sys.exit()
    
else:    
    print("i "," ", "a "," ", "b "," ", "f(a) ","  ","f(b)  "," ", "xi  ", " ", "f(xi) "," ", "error")
    
    for i in range(nIteraciones):     
       fa = round(fx(a),4)
       fb = round(fx(b),4)
       xi = round(a + (b-a)/2,4)
       fxi =round(fx(xi),4)
       listXi.append(xi)  
       ejeXi.append(xi)
       ejeY.append(fxi)
       
       #print(i+1, " ", a," ",b, " ",fa," ", fb," ", xi, " ", fxi, " ", listXi[i])
       error = round(abs(listXi[i] - listXi[i-1]), 4)
           
       i=i+1
       print(i, " ",    a," ",   b, " ",   fa," ",   fb," ",    xi, " ",    fxi, " ",   error )
       
       cambiasigno= np.sign(fa)*np.sign(fxi)
       if cambiasigno < 0:
            a = a
            b = xi
            
       if cambiasigno > 0:   
           a = xi
           b = b
           
print("\n El valor de la solucion  es x : ", round(xi,6))
print("\n cuando f(x), es = 0; es decir, pasa por la raiz")            

i=0  
plt.plot(ejeXi,ejeY, 'b--d')  #grafica los valores de Xi y f(xi)   
plt.plot(x, [fx(i) for i in x])   
#plt.scatter(ejeXi,ejeY)
plt.show()   
          
print (" \n*** Fin del programa ")     
   