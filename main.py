import tkinter as tk
from tkinter import ttk

from src.ruta_minima import (
    ARCHIVO_DATOS,
    cargar_conexiones,
    crear_grafo,
    dijkstra,
    obtener_tamano_grafo,
    verificar_conexo,
)


POSICIONES = {
    # Coordenadas manuales para ubicar las ciudades dentro del canvas.
    # No son coordenadas geograficas reales; sirven para visualizar el grafo de forma clara.
    "Hamburg": (260, 70),
    "Bremen": (160, 140),
    "Hannover": (280, 170),
    "Berlin": (520, 120),
    "Leipzig": (490, 270),
    "Dresden": (650, 280),
    "Dortmund": (150, 310),
    "Essen": (90, 360),
    "Dusseldorf": (120, 430),
    "Cologne": (190, 500),
    "Frankfurt": (360, 470),
    "Mannheim": (390, 590),
    "Stuttgart": (520, 640),
    "Nuremberg": (610, 500),
    "Munich": (680, 650),
}

COLORES = {
    # Paleta usada por la interfaz grafica.
    "fondo": "#fff7df",
    "panel": "#fff1f1",
    "mapa": "#fffaf0",
    "borde": "#e8c7a2",
    "boton_suave": "#fff0b8",
    "boton_suave_activo": "#ffe48a",
    "texto": "#111111",
    "suave": "#5f5f5f",
    "primario": "#dd0000",
    "primario_oscuro": "#990000",
    "ruta": "#ffce00",
    "arista": "#8a8a8a",
    "negro": "#000000",
}


def obtener_aristas_ruta(ruta):
    # Convierte la secuencia de ciudades en un conjunto de aristas para poder resaltarlas.
    aristas = set()

    for i in range(len(ruta) - 1):
        aristas.add(frozenset([ruta[i], ruta[i + 1]]))

    return aristas


def dibujar_grafo(canvas, grafo, ruta):
    # Redibuja todo el grafo y resalta las ciudades/aristas que pertenecen a la ruta minima.
    # Se llama al iniciar, al calcular una ruta y al limpiar la seleccion.
    canvas.delete("all")
    aristas_ruta = obtener_aristas_ruta(ruta)

    # Primero se dibujan las aristas para que los nodos queden encima.
    for ciudad in grafo:
        x1, y1 = POSICIONES[ciudad]

        for vecino, peso in grafo[ciudad]:
            if ciudad < vecino:
                x2, y2 = POSICIONES[vecino]
                arista = frozenset([ciudad, vecino])

                if arista in aristas_ruta:
                    # Las aristas de la ruta optima se muestran mas gruesas y en amarillo.
                    color = COLORES["ruta"]
                    ancho = 4
                else:
                    color = COLORES["arista"]
                    ancho = 1

                canvas.create_line(x1, y1, x2, y2, fill=color, width=ancho)

                if arista in aristas_ruta:
                    # Solo se muestran los pesos sobre las aristas usadas en la ruta seleccionada.
                    canvas.create_text(
                        (x1 + x2) / 2,
                        (y1 + y2) / 2 - 8,
                        text=str(round(peso)) + " km",
                        fill=COLORES["ruta"],
                        font=("Segoe UI", 8, "bold"),
                    )

    # Luego se dibujan los nodos y sus etiquetas.
    for ciudad in grafo:
        x, y = POSICIONES[ciudad]

        if ciudad in ruta:
            # Las ciudades que pertenecen a la ruta se diferencian del resto.
            relleno = COLORES["ruta"]
            radio = 18
        else:
            relleno = COLORES["negro"]
            radio = 15

        canvas.create_oval(
            x - radio,
            y - radio,
            x + radio,
            y + radio,
            fill=relleno,
            outline="white",
            width=2,
        )
        canvas.create_text(
            x,
            y,
            text=ciudad[:3],
            fill="white",
            font=("Segoe UI", 8, "bold"),
        )
        canvas.create_text(
            x,
            y + 27,
            text=ciudad,
            fill=COLORES["texto"],
            font=("Segoe UI", 8),
        )


def calcular(grafo, canvas, origen_var, destino_var, resultado_var):
    # Obtiene las ciudades seleccionadas y calcula la ruta minima entre ellas.
    origen = origen_var.get()
    destino = destino_var.get()

    # Los textos por defecto del combobox no son ciudades reales del grafo.
    if origen not in grafo or destino not in grafo:
        resultado_var.set("Selecciona una ciudad de origen y una ciudad de destino.")
        dibujar_grafo(canvas, grafo, [])
        return

    if origen == destino:
        resultado_var.set("El origen y el destino deben ser ciudades diferentes.")
        dibujar_grafo(canvas, grafo, [])
        return

    ruta, distancia = dijkstra(grafo, origen, destino)

    # Si el grafo fuera desconexo, podria no existir ruta entre dos ciudades.
    if not ruta:
        resultado_var.set("No existe una ruta entre esas ciudades.")
        dibujar_grafo(canvas, grafo, [])
        return

    resultado = "Ruta minima:\n"
    resultado = resultado + " -> ".join(ruta)
    resultado = resultado + "\n\nDistancia total: " + str(round(distancia)) + " km"

    resultado_var.set(resultado)
    dibujar_grafo(canvas, grafo, ruta)


def limpiar(canvas, grafo, origen_var, destino_var, resultado_var):
    # Restablece los selectores y vuelve a mostrar el grafo sin ruta resaltada.
    origen_var.set("Selecciona el origen")
    destino_var.set("Selecciona el destino")
    resultado_var.set("Selecciona una ciudad de origen y una ciudad de destino.")
    dibujar_grafo(canvas, grafo, [])


def crear_interfaz():
    # Carga los datos, construye el grafo y prepara la ventana principal.
    # Esta funcion concentra la construccion de todos los elementos visuales.
    conexiones = cargar_conexiones(ARCHIVO_DATOS)
    grafo = crear_grafo(conexiones)
    ciudades = sorted(grafo.keys())

    ventana = tk.Tk()
    ventana.title("Ruta minima en Alemania")
    ventana.geometry("1080x760")
    ventana.configure(bg=COLORES["fondo"])

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TCombobox", padding=6)

    # Franja superior con los colores de la bandera alemana.
    bandera = tk.Frame(ventana, bg=COLORES["fondo"], height=18)
    bandera.pack(fill="x")
    tk.Frame(bandera, bg=COLORES["negro"], height=6).pack(fill="x")
    tk.Frame(bandera, bg=COLORES["primario"], height=6).pack(fill="x")
    tk.Frame(bandera, bg=COLORES["ruta"], height=6).pack(fill="x")

    titulo = tk.Label(
        ventana,
        text="Ruta minima entre ciudades de Alemania",
        bg=COLORES["fondo"],
        fg=COLORES["texto"],
        font=("Segoe UI", 20, "bold"),
    )
    titulo.pack(anchor="w", padx=24, pady=(20, 4))

    subtitulo = tk.Label(
        ventana,
        text="Red de ciudades conectadas por carretera; cada conexion tiene una distancia en kilometros",
        bg=COLORES["fondo"],
        fg=COLORES["suave"],
        font=("Segoe UI", 10),
    )
    subtitulo.pack(anchor="w", padx=24, pady=(0, 14))

    # El panel izquierdo contiene controles; el canvas derecho contiene el grafo.
    contenido = tk.Frame(ventana, bg=COLORES["fondo"])
    contenido.pack(fill="both", expand=True, padx=24, pady=(0, 24))

    panel = tk.Frame(contenido, bg=COLORES["panel"], padx=18, pady=18)
    panel.pack(side="left", fill="y", padx=(0, 16))

    canvas = tk.Canvas(
        # El canvas es el espacio donde se dibujan nodos, aristas y ruta optima.
        contenido,
        width=740,
        height=680,
        bg=COLORES["mapa"],
        highlightthickness=1,
        highlightbackground=COLORES["borde"],
    )
    canvas.pack(side="right", fill="both", expand=True)

    origen_var = tk.StringVar(value="Selecciona el origen")
    destino_var = tk.StringVar(value="Selecciona el destino")
    resultado_var = tk.StringVar(value="Selecciona una ciudad de origen y una ciudad de destino.")

    # Selectores de origen y destino.
    tk.Label(
        panel,
        text="Origen",
        bg=COLORES["panel"],
        fg=COLORES["texto"],
        font=("Segoe UI", 10, "bold"),
    ).pack(anchor="w")
    ttk.Combobox(panel, textvariable=origen_var, values=ciudades, state="readonly", width=24).pack(
        fill="x", pady=(4, 14)
    )

    tk.Label(
        panel,
        text="Destino",
        bg=COLORES["panel"],
        fg=COLORES["texto"],
        font=("Segoe UI", 10, "bold"),
    ).pack(anchor="w")
    ttk.Combobox(panel, textvariable=destino_var, values=ciudades, state="readonly", width=24).pack(
        fill="x", pady=(4, 14)
    )

    tk.Button(
        panel,
        text="Calcular ruta",
        command=lambda: calcular(grafo, canvas, origen_var, destino_var, resultado_var),
        bg=COLORES["primario"],
        fg="white",
        activebackground=COLORES["primario_oscuro"],
        activeforeground="white",
        relief="flat",
        font=("Segoe UI", 10, "bold"),
        pady=10,
    ).pack(fill="x", pady=(0, 8))

    tk.Button(
        panel,
        text="Limpiar",
        command=lambda: limpiar(canvas, grafo, origen_var, destino_var, resultado_var),
        bg=COLORES["boton_suave"],
        fg=COLORES["texto"],
        activebackground=COLORES["boton_suave_activo"],
        relief="flat",
        font=("Segoe UI", 10),
        pady=8,
    ).pack(fill="x")

    tk.Label(
        panel,
        text="Resultado",
        bg=COLORES["panel"],
        fg=COLORES["texto"],
        font=("Segoe UI", 12, "bold"),
    ).pack(anchor="w", pady=(24, 6))
    tk.Label(
        panel,
        textvariable=resultado_var,
        bg=COLORES["panel"],
        fg=COLORES["texto"],
        justify="left",
        wraplength=230,
        font=("Segoe UI", 10),
    ).pack(anchor="w")

    # Resumen calculado desde el grafo construido.
    resumen = "Orden |V|: " + str(len(grafo)) + "\n"
    resumen = resumen + "Tamano |E|: " + str(obtener_tamano_grafo(grafo)) + "\n"
    resumen = resumen + "Conexo: " + ("Si" if verificar_conexo(grafo) else "No")

    tk.Label(
        panel,
        text="Datos del grafo",
        bg=COLORES["panel"],
        fg=COLORES["texto"],
        font=("Segoe UI", 12, "bold"),
    ).pack(anchor="w", pady=(24, 6))
    tk.Label(
        panel,
        text=resumen,
        bg=COLORES["panel"],
        fg=COLORES["suave"],
        justify="left",
        font=("Segoe UI", 10),
    ).pack(anchor="w")

    dibujar_grafo(canvas, grafo, [])
    ventana.mainloop()


if __name__ == "__main__":
    crear_interfaz()
