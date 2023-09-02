<<<<<<< HEAD
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
=======
# Lista de los poderes de Spider-Man
poderes_spiderman = [
    "Agilidad sobrehumana",
    "Fuerza sobrehumana",
    "Sentido arácnido",
    "Lanzar telarañas",
    "Paredes trepadoras",
]

# Función para crear un diccionario de poderes con descripciones cortas
def crear_diccionario_poderes():
    diccionario_poderes = {
        "Agilidad sobrehumana": "Spider-Man posee una agilidad excepcional, lo que le permite moverse con rapidez y agilidad sobrenaturales.",
        "Fuerza sobrehumana": "Tiene una fuerza superior a la de un humano normal, lo que le permite levantar objetos pesados y enfrentarse a enemigos poderosos.",
        "Sentido arácnido": "Su sentido arácnido le proporciona una percepción extraordinaria, permitiéndole detectar peligros y amenazas.",
        "Lanzar telarañas": "Puede lanzar telarañas desde dispositivos en sus muñecas para columpiarse entre edificios y atrapar a sus enemigos.",
        "Paredes trepadoras": "Sus manos y pies pueden adherirse a las superficies, permitiéndole trepar y aferrarse a las paredes."
    }
    return diccionario_poderes

# Función para imprimir el diccionario de poderes con títulos y descripciones
def imprimir_diccionario_poderes():
    diccionario_poderes = crear_diccionario_poderes()
    for poder, descripcion in diccionario_poderes.items():
        print(f"{poder}:")
        print(descripcion)
        print()

# Llamar a la función para imprimir el diccionario de poderes
imprimir_diccionario_poderes()
>>>>>>> 403502b80f5e35b87101a65850b69ded63e10172
