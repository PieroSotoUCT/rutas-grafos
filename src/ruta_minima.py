import csv


ARCHIVO_DATOS = "data/conexiones_alemania.csv"


def cargar_conexiones(nombre_archivo):
    conexiones = []

    with open(nombre_archivo, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            origen = fila["origen"]
            destino = fila["destino"]
            distancia = float(fila["distancia_km"])
            fuente = fila["fuente"]
            conexiones.append((origen, destino, distancia, fuente))

    return conexiones


def crear_grafo(conexiones):
    grafo = {}

    for origen, destino, distancia, fuente in conexiones:
        if origen not in grafo:
            grafo[origen] = []
        if destino not in grafo:
            grafo[destino] = []

        grafo[origen].append((destino, distancia))
        grafo[destino].append((origen, distancia))

    return grafo


def obtener_tamano_grafo(grafo):
    cantidad_aristas_repetidas = 0

    for ciudad in grafo:
        cantidad_aristas_repetidas = cantidad_aristas_repetidas + len(grafo[ciudad])

    return cantidad_aristas_repetidas // 2


def verificar_conexo(grafo):
    ciudades = list(grafo.keys())
    pendientes = [ciudades[0]]
    visitados = set()

    while pendientes:
        ciudad_actual = pendientes.pop()

        if ciudad_actual not in visitados:
            visitados.add(ciudad_actual)

            for vecino, distancia in grafo[ciudad_actual]:
                if vecino not in visitados:
                    pendientes.append(vecino)

    return len(visitados) == len(ciudades)


def buscar_ciudad_menor_distancia(distancias, visitados):
    ciudad_menor = None
    distancia_menor = float("inf")

    for ciudad in distancias:
        if ciudad not in visitados and distancias[ciudad] < distancia_menor:
            ciudad_menor = ciudad
            distancia_menor = distancias[ciudad]

    return ciudad_menor


def dijkstra(grafo, origen, destino):
    distancias = {}
    anteriores = {}
    visitados = set()

    for ciudad in grafo:
        distancias[ciudad] = float("inf")
        anteriores[ciudad] = None

    distancias[origen] = 0

    while len(visitados) < len(grafo):
        ciudad_actual = buscar_ciudad_menor_distancia(distancias, visitados)

        if ciudad_actual is None:
            break

        if ciudad_actual == destino:
            break

        visitados.add(ciudad_actual)

        for vecino, peso in grafo[ciudad_actual]:
            nueva_distancia = distancias[ciudad_actual] + peso

            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                anteriores[vecino] = ciudad_actual

    ruta = reconstruir_ruta(anteriores, origen, destino)
    return ruta, distancias[destino]


def reconstruir_ruta(anteriores, origen, destino):
    ruta = []
    ciudad_actual = destino

    while ciudad_actual is not None:
        ruta.append(ciudad_actual)
        ciudad_actual = anteriores[ciudad_actual]

    ruta.reverse()

    if len(ruta) == 0 or ruta[0] != origen:
        return []

    return ruta


def mostrar_ciudades(grafo):
    print("Ciudades disponibles:")

    for ciudad in sorted(grafo):
        print("-", ciudad)


def mostrar_resumen_grafo(grafo):
    orden = len(grafo)
    tamano = obtener_tamano_grafo(grafo)

    print("Resumen del grafo:")
    print("Orden |V|:", orden, "vertices")
    print("Tamano |E|:", tamano, "aristas")
    print("Tipo: grafo no dirigido y ponderado")

    if verificar_conexo(grafo):
        print("Conexidad: el grafo es conexo")
    else:
        print("Conexidad: el grafo es desconexo")


def ejecutar_programa():
    conexiones = cargar_conexiones(ARCHIVO_DATOS)
    grafo = crear_grafo(conexiones)

    print("Ruta minima entre ciudades de Alemania")
    print()
    mostrar_resumen_grafo(grafo)
    print()
    mostrar_ciudades(grafo)
    print()

    origen = input("Ciudad de origen: ").strip()
    destino = input("Ciudad de destino: ").strip()

    if origen not in grafo:
        print("La ciudad de origen no existe en el grafo.")
        return

    if destino not in grafo:
        print("La ciudad de destino no existe en el grafo.")
        return

    if origen == destino:
        print("El origen y el destino deben ser distintos.")
        return

    ruta, distancia_total = dijkstra(grafo, origen, destino)

    if not ruta:
        print("No existe una ruta entre esas ciudades.")
        return

    print()
    print("Ruta minima:")
    print(" -> ".join(ruta))
    print("Distancia total:", round(distancia_total), "km")


if __name__ == "__main__":
    ejecutar_programa()
