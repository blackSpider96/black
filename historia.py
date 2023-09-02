# Información sobre Spider-Man
poderes = [
    "Agilidad sobrehumana",
    "Fuerza sobrehumana",
    "Sentido arácnido",
    "Lanzar telarañas"
]
enemigos = [
    "Green Goblin",
    "Doctor Octopus",
    "Venom",
    "Sandman",
    "Rhino"
]
aliados = [
    "Mary Jane Watson",
    "Aunt May",
    "Iron Man",
    "Daredevil",
    "Black Cat"
]
trajes = [
    "Traje clásico rojo y azul",
    "Traje negro simbiótico",
    "Traje Iron Spider",
    "Traje Stealth"
]
equipos = [
    "Los Vengadores",
    "Los Nuevos Guerreros",
    "Los Defensores"
]

# Funciones para imprimir listas
def imprimir_poderes():
    print("Lista de Poderes:")
    for poder in poderes:
        print("- " + poder)

def imprimir_enemigos():
    print("Lista de Enemigos:")
    for enemigo in enemigos:
        print("- " + enemigo)

def imprimir_aliados():
    print("Lista de Aliados:")
    for aliado in aliados:
        print("- " + aliado)

def imprimir_trajes():
    print("Lista de Trajes:")
    for traje in trajes:
        print("- " + traje)

def imprimir_equipos():
    print("Lista de Equipos:")
    for equipo in equipos:
        print("- " + equipo)

# Función para la historia de Spider-Man
def Historia():
    historia = """
    Spider-Man, cuyo nombre real es Peter Parker, es un superhéroe creado por Stan Lee y Steve Ditko. 
    Peter obtuvo sus poderes después de ser mordido por una araña radiactiva. A lo largo de su historia, 
    ha enfrentado a numerosos villanos, incluyendo a Green Goblin, Doctor Octopus y Venom.
    Peter también ha tenido una vida personal complicada, equilibrando su papel como estudiante y fotógrafo 
    con su responsabilidad como Spider-Man. Ha sido miembro de equipos como Los Vengadores y Los Defensores.
    Con su icónico traje rojo y azul, Spider-Man se ha convertido en uno de los superhéroes más queridos y 
    reconocidos en el mundo de los cómics y el cine.
    """

    # Imprimir la historia con saltos de línea cada 30 caracteres
    caracteres_por_linea = 30
    for i in range(0, len(historia), caracteres_por_linea):
        print(historia[i:i+caracteres_por_linea])
