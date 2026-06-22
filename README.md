# Rutas en Alemania con Grafos Ponderados

Proyecto final de Matemática Discreta — Universidad Católica de Temuco.

Proyecto de Matemática Discreta sobre rutas óptimas entre ciudades de Alemania usando grafos ponderados.

## Descripción

El proyecto modela una red de ciudades alemanas mediante un grafo ponderado. Las ciudades son vértices, las conexiones entre ciudades son aristas y cada peso representa una distancia aproximada por carretera en kilómetros.

El objetivo es calcular la ruta de menor distancia entre una ciudad de origen y una ciudad de destino usando el algoritmo de Dijkstra.

## Modelo del grafo

El grafo se representa como:

```text
G = (V, E, w)
```

Donde:

- `V` representa las ciudades seleccionadas.
- `E` representa las conexiones por carretera entre ciudades.
- `w` representa la distancia por carretera entre dos ciudades conectadas.

El grafo construido tiene:

- Orden `|V| = 15`, porque contiene 15 ciudades.
- Tamaño `|E| = 25`, porque contiene 25 conexiones.
- Tipo: grafo no dirigido y ponderado.
- Conexidad: el grafo es conexo, ya que existe al menos un camino entre cualquier par de ciudades.

## Datos y fuentes

Los datos del grafo se encuentran en:

```text
data/conexiones_alemania.csv
```

Cada fila contiene:

- ciudad de origen
- ciudad de destino
- distancia en kilómetros
- criterio de ponderación
- fuente usada
- enlace de consulta
- fecha de consulta

Las distancias fueron consultadas en OpenStreetMap Directions usando el motor OSRM para rutas en automóvil. Se usó un único criterio de ponderación durante todo el proyecto: distancia aproximada por carretera en kilómetros.

Fuentes generales:

- OpenStreetMap: https://www.openstreetmap.org/
- OSRM: https://project-osrm.org/

## Funcionalidades

Este repositorio contiene:

- Datos del grafo con 15 ciudades de Alemania.
- 25 conexiones por carretera entre ciudades.
- Programa por consola para calcular una ruta mínima.
- Interfaz gráfica para seleccionar origen, destino y visualizar la ruta.
- Representación visual del grafo, con la ruta óptima resaltada.
- Resumen del grafo: orden, tamaño, tipo de grafo y conexidad.

## Algoritmo usado

La función `dijkstra` implementa el algoritmo de Dijkstra, recomendado para encontrar caminos mínimos en grafos ponderados con pesos positivos.

En este proyecto, Dijkstra es adecuado porque el costo de cada arista corresponde a una distancia por carretera. Como las distancias son valores positivos, el algoritmo puede calcular correctamente el camino de menor costo entre una ciudad de origen y una ciudad de destino.

El costo total de una ruta corresponde a la suma de las distancias de todas las aristas recorridas.

## Representación en el código

El grafo se representa mediante un diccionario de listas de adyacencia. Cada ciudad guarda una lista de ciudades vecinas junto con la distancia correspondiente.

Ejemplo conceptual:

```text
grafo["Berlin"] = [
  ("Hamburg", 289),
  ("Leipzig", 189),
  ("Dresden", 191),
  ("Hannover", 290)
]
```

Como el grafo es no dirigido, cada conexión se agrega en ambos sentidos.

## Estructura del proyecto

```text
data/
  conexiones_alemania.csv
main.py
src/
  ruta_minima.py
README.md
```

## Requisitos

- Python 3.10 o superior.
- Tkinter, incluido normalmente con Python en Windows.

El proyecto no necesita instalar librerías externas. Las librerías usadas son:

- `csv`: lectura del archivo de conexiones.
- `tkinter`: construcción de la interfaz gráfica.
- `ttk`: componentes visuales de la interfaz.

Nota: `tkinter` no se instala con `pip`. Si Python fue instalado sin soporte para Tkinter, se debe instalar o activar desde la instalación de Python o desde el gestor de paquetes del sistema operativo. En Windows normalmente viene incluido con Python. En Linux puede requerir un paquete como `python3-tk`.

## Cómo ejecutar por consola

Desde la carpeta raíz del proyecto:

```bash
python src/ruta_minima.py
```

## Cómo ejecutar la interfaz gráfica

Desde la carpeta raíz del proyecto:

```bash
python main.py
```

## Pruebas de funcionamiento

Ejemplos de rutas obtenidas con el programa:

| Origen  | Destino | Ruta mínima                                         | Distancia total |
| ------- | ------- | --------------------------------------------------- | --------------- |
| Berlin  | Munich  | Berlin -> Leipzig -> Nuremberg -> Munich            | 642 km          |
| Hamburg | Cologne | Hamburg -> Hannover -> Dortmund -> Cologne          | 457 km          |
| Dresden | Essen   | Dresden -> Leipzig -> Hannover -> Dortmund -> Essen | 629 km          |

## Integrantes

- Piero Soto
- Lucas Villegas
- Nicolás Calderón
- Mauricio Valdés
