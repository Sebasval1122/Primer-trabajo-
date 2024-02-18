""""Escribir una funcion que calcule el factorial de un numero dado"""
def factorial(numero_para_el_factorial):
    if numero_para_el_factorial < 0:
        return "El factorial no está definido para números negativos."
    elif numero_para_el_factorial == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero_para_el_factorial + 1):
            resultado *= i
        return resultado

numero_para_el_factorial = int(input("Ingrese un número para calcular su factorial: "))
resultado_factorial = factorial(numero_para_el_factorial)
print("El factorial de", numero_para_el_factorial, "es:", resultado_factorial)