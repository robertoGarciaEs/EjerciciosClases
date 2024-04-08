lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for i in range(0,len(lista_numeros)):
    if lista_numeros[i] < 0:
        break
    print(lista_numeros[i])