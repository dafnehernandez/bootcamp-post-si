#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Tarea 2:
    Hacer un programa que me pida 2 matrices (no necesariamente cuadradas) y haga la multiplicación si es posible.

m: columnas
n: filas
"""
import random
matriz_final = []
result = int(0)

print("El siguiente programa realiza multiplicacion de matrices\n")
n1 = int(input("Ingresa el numero de filas de la primer matriz: "))
m1 = int(input("Ingresa el numero de columnas de la primer matriz: "))
n2 = int(input("Ingresa el numero de filas de la segunda matriz: "))
m2 = int(input("Ingresa el numero de columnas de la segunda matriz: "))

if(m1 != n2):   # si el numero de columnas de la matriz 1 es diferente al numero de filas de la matriz 2
    print("\nNo se puede hacer mi chato, vuelve a intentarlo")

else:
    print("\nVamonos recio")
    llenado = input("Deseas que las matrices se llenen automaticamente con numero aleatorios? (y/n): ")
    
    if(llenado == 'y'):         # se da la opcion de llenado automatico al usuario
        print("Llenado de matriz automatico random ribunucleico... ")
        matriz1 = [[random.randrange(1,100) for columna in range(m1)] for fila in range(n1)]
        matriz2 = [[random.randrange(1,100) for columna in range(m2)] for fila in range(n2)] 
        
        print("Matriz 1:")      # imprime el resultado de matriz 1 random
        for fila in range(n1):
            print("[", end=" ")
            for columna in range(m1):
                print("\t{:d} ".format(matriz1[fila][columna]), end="\t")
            print("]")
        
        print("\nMatriz 2:")    # imprime el resultado de matriz 2 random
        for fila in range(n2):
            print("[", end=" ")
            for columna in range(m2):
                print("\t{:d} ".format(matriz2[fila][columna]), end="\t")
            print("]")

    else:                       # ingresa los datos de la matriz manualmente:
        print("No lo hagas, ingresa los datos random bro")
         
    # Multiplicacion
    for fila in range(n1):
        matriz_final.append([])
        for columna in range(m2):
            for res in range(n2):   # se intera el numero en comun
                result += matriz1[fila][res] * matriz2[res][columna]
            matriz_final[fila].append(result)
        
    print("\nMatriz Resultante de la Multiplicacion:")
    for fila in range(n1):
        print("[", end=" ")
        for columna in range(m2):
            print("\t{:d} ".format(matriz_final[fila][columna]), end="\t")
        print("]")


