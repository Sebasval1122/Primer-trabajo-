""""Crear un programa que calcule la suma de los números en una lista dada"""
si="Si"
if si=="Si":
    entrada=input("Ingrese el numero separado por espacios: ")
    suma=0
    lista=float(input("Ingrese un numero: "))
    list=[int(numero) for numero in entrada.split()]
    list.append(lista)
    suma=sum(list)
    
print("La suma es: ",suma)
print(list)