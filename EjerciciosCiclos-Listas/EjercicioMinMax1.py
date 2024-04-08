lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
#Solución 1
valor_maximo = max(lista_numeros)
print("El valor máximo es:", valor_maximo)

#Solución 2
valor_maximo2 = lista_numeros[0]
for numero in lista_numeros:
    if numero > valor_maximo2:
        valor_maximo2 = numero
print("El valor máximo es:", valor_maximo2)