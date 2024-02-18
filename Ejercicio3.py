""""Crear un programa que genere una lista de números aleatorios y los imprima en pantalla."""
import random
lista_numeros = [random.randint(1, 100) for _ in range(100)]
print("La lista de los numeros aleatorios es: ")
print(lista_numeros)