lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melissa"]
for indices, nombre in enumerate(lista_nombres):
    if nombre.startswith("M"):
        print(indices)