""""Crear un programa que genere una lista de numeros pares entre 1 y 100"""
import random
lista=[]
i=0
while i<=99:
    if i%2==0:
        print(i)
        i+=2
        lista.append(i)
print(lista)