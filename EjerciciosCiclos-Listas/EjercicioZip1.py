capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
capital_pais = zip(capitales, paises)
for capital, pais in capital_pais:
    print(f"La capital de {pais} es {capital}")