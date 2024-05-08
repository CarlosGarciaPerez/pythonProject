# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 10:30:07 2021

@author: PC-GARCIA
"""

import os
import numpy as np
import math
import sys
import matplotlib.pyplot as plt   # libreria pàra graficar
import sympy as sp


os.system ("cls") 
print("\n\nEste programa calcula Solucion Matematica por distintos Metodos\n ")
print("Selecione el metodo a realizar\n ")
print("METODO DE BISECCION      ...... 1 ")
print("METODO DE NEWTON RAPHSON .......2 ")
print("METODO DE SECANTE        .......3 ")
opcion = int (input ("Eliga una opcion: "))

if  opcion == 1:
    print("Selecciono el metodo de BISECCION ")
    # INICIO DE VARIABLES
    toleranciaError = 0.0001
    i=0 # contador de iteraciones
    listXi=[]   # arreglo que almacena valor de Xi
    ejeXi=[]    # arreglo de ejer X con valor  Xi
    ejeY=[]    # arreglo de ejer Y con valor  f(xi)
    
    # se declara la funcion para evaluar la expresion matematica
    def fx(x):   
         return eval(ec)
    
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
               
    plt.plot(ejeXi,ejeY, 'b--d')  #grafica los valores de Xi y f(xi)      
    #plt.scatter(ejeXi,ejeY)
    plt.show()   
              
    print (" \n*** Fin del programa ")          
elif opcion == 2:
    print("Selecciono el metodo de NEWTON RAPHSON ")     
     
    #print("funcion F(x) =x^3 + 4x^2 - 10 \n")
    
    # se declara la funcion para evaluar la expresion matematica
    def fx(x):   
         return eval(ec)
     
    def dfx(x):   
         return eval(dx)
    
    # INGRESO
    #fx = lambda x: x**3 + 4*x**2 - 10 
    #dfx = lambda x: 3*x**2 + 8*x**1 
    listXi=[]   # arreglo que almacena valor de Xi
    tolera = 0.000001
    i=0
    ejeXi=[]    # arreglo de ejer X con valor  Xi
    ejeY=[]     # arreglo de ejer Y con valor  f(xi)
    
    
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
         
    plt.plot(ejeXi,ejeY)  #grafica los valores de Xi y f(xi)      
    plt.show()        
               
elif opcion == 3:     
    print("Selecciono el metodo de SECANTE")   
    
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
     
       
else :      
     print("OPCION INCORRECTA")
     print("eliga una opcion nuevamente ")