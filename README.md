# Rutas en Alemania con Grafos Ponderados

Proyecto de Matematica Discreta sobre rutas optimas entre ciudades de Alemania usando grafos ponderados.

## Descripcion

El proyecto modela una red de ciudades alemanas mediante un grafo ponderado. Las ciudades son vertices, las conexiones entre ciudades son aristas y cada peso representa una distancia aproximada por carretera en kilometros.

El objetivo es calcular la ruta de menor distancia entre una ciudad de origen y una ciudad de destino usando el algoritmo de Dijkstra.

## Modelo del grafo

El grafo se representa como:

```text
G = (V, E, w)
```

Donde:

- `V` es el conjunto de ciudades seleccionadas.
- `E` es el conjunto de conexiones por carretera entre ciudades.
- `w` es la funcion de peso, donde `w(u, v)` representa la distancia por carretera entre las ciudades `u` y `v`.

El grafo construido tiene:

- Orden `|V| = 15`, porque contiene 15 ciudades.
- Tamano `|E| = 25`, porque contiene 25 conexiones.
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
- distancia en kilometros
- criterio de ponderacion
- fuente usada
- enlace de consulta
- fecha de consulta

Las distancias fueron consultadas en OpenStreetMap Directions usando el motor OSRM para rutas en automovil. Se uso un unico criterio de ponderacion durante todo el proyecto: distancia aproximada por carretera en kilometros.

Fuentes generales:

- OpenStreetMap: https://www.openstreetmap.org/
- OSRM: https://project-osrm.org/

## Funcionalidades

Este repositorio contiene:

- Datos del grafo con 15 ciudades de Alemania.
- 25 conexiones por carretera entre ciudades.
- Programa por consola para calcular una ruta minima.
- Interfaz grafica para seleccionar origen, destino y visualizar la ruta.
- Representacion visual del grafo, con la ruta optima resaltada.
- Resumen del grafo: orden, tamano, tipo de grafo y conexidad.

## Algoritmo usado

La funcion `dijkstra` implementa el algoritmo de Dijkstra, recomendado para encontrar caminos minimos en grafos ponderados con pesos positivos.

Se usa este algoritmo porque todos los pesos del grafo representan distancias por carretera, por lo tanto son valores positivos. La implementacion usa diccionarios, listas, ciclos y condicionales para que el codigo sea simple de revisar y defender.

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

El proyecto no necesita instalar librerias externas. Las librerias usadas son:

- `csv`: lectura del archivo de conexiones.
- `tkinter`: construccion de la interfaz grafica.
- `ttk`: componentes visuales de la interfaz.

Nota: `tkinter` no se instala con `pip`. Si Python fue instalado sin soporte para Tkinter, se debe instalar o activar desde la instalacion de Python o desde el gestor de paquetes del sistema operativo. En Windows normalmente viene incluido con Python. En Linux puede requerir un paquete como `python3-tk`.

## Como ejecutar por consola

Desde la carpeta raiz del proyecto:

```bash
python src/ruta_minima.py
```

## Como ejecutar la interfaz grafica

Desde la carpeta raiz del proyecto:

```bash
python main.py
```

## Pruebas de funcionamiento

Ejemplos de rutas obtenidas con el programa:

| Origen | Destino | Ruta minima | Distancia total |
| --- | --- | --- | --- |
| Berlin | Munich | Berlin -> Leipzig -> Nuremberg -> Munich | 642 km |
| Hamburg | Cologne | Hamburg -> Hannover -> Dortmund -> Cologne | 457 km |
| Dresden | Essen | Dresden -> Leipzig -> Hannover -> Dortmund -> Essen | 629 km |

## Integrantes

- Piero Soto - piero.soto2025@alu.uct.cl
- Lucas Villegas - lvillegas2024@alu.uct.cl
- Nicolas Calderon - ncalderon2026@alu.uct.cl
- Mauricio Valdes - mvaldes2026@alu.uct.cl
