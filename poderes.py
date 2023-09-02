# Definición de la función spider_poderes
def spider_poderes():
    # Lista de los poderes de Spider-Man
    poderes_spiderman = [
        "Agilidad sobrehumana",
        "Fuerza sobrehumana",
        "Sentido arácnido",
        "Lanzar telarañas",
        "Paredes trepadoras",
    ]

    # Imprimir los poderes numerados con saltos de línea
    for i, poder in enumerate(poderes_spiderman, start=1):
        print(f"{i}. {poder}")

# Llamar a la función spider_poderes para imprimir los poderes
spider_poderes()
