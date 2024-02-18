""""Escribir un programa que encuentre el numero mas grande y el mas pequeño en una lista dada"""
lista = []
numbers = int(input("Ingrese la cantidad de números que desea ingresar: "))
for i in range(numbers):
    num = int(input(f"Ingrese el número {i+1}: "))
    lista.append(num)

maximo = max(lista)
minimo = min(lista)

print(f"El número más grande es: {maximo}")
print(f"El número más pequeño es: {minimo}")