""""Crear un programa que genere una matriz de números y la imprima en pantalla"""
import random
filas = int(input("Ingrese el numero de filas: "))
columnas = int(input("Ingrese el numero de columnas: "))
rango_minimo=int(input("Ingrese un rango minimo: "))
rango_maximo=int(input("Ingrese un rango maximo: "))

matriz_aleatoria = [[random.randint(rango_minimo, rango_maximo) for _ in range(columnas)] for _ in range(filas)]

print(matriz_aleatoria)
