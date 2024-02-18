"""Crear un programa que le pida dos numeros al usuario y que calcule la suma resta multiplicación y divición"""
numero1=float(input("Ingrese el primer numero: "))
numero2=float(input("Ingrese el segundo numero: "))
multiplicacion=numero1*numero2
suma=numero1+numero2
resta=numero1-numero2

if numero2==0:
    print("La divicion por cero no existe")
else:
    divicion=numero1/numero2
print("El resultado de la multiplicacion es: ",multiplicacion)
print("El resultado de la suma es: ",suma)
print("El resultado de la resta es:",resta)
print("El resultado de la divicion es: ",divicion)