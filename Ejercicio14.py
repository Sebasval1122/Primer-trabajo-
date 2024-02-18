""""Escribir una funcion que calcule la mediana aritmetica de una lista de números"""
def media_aritmetica(lista):
    suma = sum(lista)
    media = suma / len(lista)
    return media

numeros = []
numeros_en_la_lista = int(input("Ingrese la cantidad de números que desea ingresar: "))
for i in range(numeros_en_la_lista):
    numero = float(input("Ingrese un número: "))
    numeros.append(numero)

resul=media_aritmetica(numeros)
print("La media aritmética de la lista es:", resul)