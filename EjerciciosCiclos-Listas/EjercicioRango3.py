lista_numeros = range(1, 16)
suma_cuadrados = 0
for numero in lista_numeros:
    numeros_potencia = numero ** 2
    suma_cuadrados += numeros_potencia
print("La suma de todos los valores al cuadrado es:", suma_cuadrados)