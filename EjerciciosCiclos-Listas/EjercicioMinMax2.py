lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
#Solución 1
valor_maximo = max(lista_numeros)
valor_minimo = min(lista_numeros)
rango = valor_maximo - valor_minimo
print("La diferencia es:", rango)

#Solución 2
valor_maximo2 = lista_numeros[0]
valor_minimo2 = lista_numeros[0]
for numero in lista_numeros:
    if numero > valor_maximo2:
        valor_maximo2 = numero
    elif numero < valor_minimo2:
        valor_minimo2 = numero
    rango2 = valor_maximo2 - valor_minimo2
print("La diferencia es:", rango2)