# -----------------------------------------------------------
# ConéctateUIS - Versión 3 (implementación con grafos, solo terminal)
# -----------------------------------------------------------
# Autor: David Sandoval
# Descripción:
# Sistema de rutas internas del campus basado en grafos,
# usando la librería NetworkX. Permite agregar edificios,
# conectar nodos bidireccionalmente y calcular la ruta más corta.
# -----------------------------------------------------------

import networkx as nx

# -----------------------------------------------------------
# Inicialización del grafo
# -----------------------------------------------------------
campus = nx.Graph()

# -----------------------------------------------------------
# Datos de ejemplo precargados
# -----------------------------------------------------------
def cargar_datos_iniciales():
    agregar_edificio("Edificio Central", "Académico", "Edificio principal de clases")
    agregar_edificio("Biblioteca", "Académico", "Espacio de estudio y préstamo de libros")
    agregar_edificio("Cafetería", "Servicios", "Zona de comidas para estudiantes y personal")
    agregar_edificio("Laboratorio de Sistemas", "Académico", "Laboratorio con equipos de cómputo")
    agregar_edificio("Cancha", "Recreación", "Espacio deportivo para actividades físicas")

    conectar_edificios("Edificio Central", "Biblioteca", 5)
    conectar_edificios("Edificio Central", "Cafetería", 3)
    conectar_edificios("Biblioteca", "Laboratorio de Sistemas", 4)
    conectar_edificios("Cafetería", "Cancha", 6)
    conectar_edificios("Laboratorio de Sistemas", "Cancha", 7)

# -----------------------------------------------------------
# Funciones principales
# -----------------------------------------------------------

def agregar_edificio(nombre, tipo, descripcion, accesible=True):
    campus.add_node(nombre, tipo=tipo, descripcion=descripcion, accesible=accesible)
    print(f"Se agregó el edificio '{nombre}' correctamente.")


def conectar_edificios(origen, destino, distancia=1):
    if origen not in campus or destino not in campus:
        print("Uno o ambos edificios no existen.")
        return
    campus.add_edge(origen, destino, peso=distancia)
    print(f"Conectado '{origen}' ↔ '{destino}' (distancia {distancia}).")


def mostrar_estructura():
    print("\nEstructura actual del campus:")
    for nodo, datos in campus.nodes(data=True):
        print(f"- {nodo} ({datos['tipo']}) - accesible: {datos['accesible']}")
    print("\nConexiones:")
    for origen, destino, datos in campus.edges(data=True):
        print(f"  {origen} ↔ {destino} (distancia {datos['peso']})")


def listar_accesibles():
    print("\nLugares accesibles:")
    for nodo, datos in campus.nodes(data=True):
        if datos.get("accesible"):
            print(f" - {nodo}")


def buscar_ruta_corta(origen, destino):
    if origen not in campus or destino not in campus:
        print("Uno o ambos edificios no existen.")
        return
    try:
        ruta = nx.shortest_path(campus, source=origen, target=destino, weight="peso")
        distancia_total = nx.shortest_path_length(campus, source=origen, target=destino, weight="peso")
        print("\nRuta más corta encontrada:")
        print(" → ".join(ruta))
        print(f"Distancia total: {distancia_total}")
    except nx.NetworkXNoPath:
        print("No hay conexión entre esos lugares.")


def mostrar_grafo_texto():
    if campus.number_of_nodes() == 0:
        print("El grafo está vacío, no hay nada que mostrar.")
        return

    print("\nRepresentación del grafo (modo texto):\n")
    for origen, destino, datos in campus.edges(data=True):
        print(f"{origen} --({datos['peso']})--> {destino}")

# -----------------------------------------------------------
# Menú interactivo
# -----------------------------------------------------------

def menu():
    while True:
        print("\n===== MENÚ DEL CAMPUS (GRAFOS) =====")
        print("1. Agregar edificio o punto principal")
        print("2. Conectar edificios")
        print("3. Mostrar estructura del grafo")
        print("4. Listar accesibles")
        print("5. Buscar ruta más corta")
        print("6. Mostrar grafo (texto)")
        print("7. Salir")

        opcion = input("\nElige una opción (1-7): ").strip()

        if opcion == "1":
            nombre = input("Nombre del edificio o zona: ").strip()
            tipo = input("Tipo: ").strip()
            descripcion = input("Descripción: ").strip()
            accesible = input("¿Es accesible? (s/n): ").strip().lower() == "s"
            agregar_edificio(nombre, tipo, descripcion, accesible)

        elif opcion == "2":
            origen = input("Nombre del edificio origen: ").strip()
            destino = input("Nombre del edificio destino: ").strip()
            try:
                distancia = float(input("Distancia entre ellos: "))
            except ValueError:
                distancia = 1
            conectar_edificios(origen, destino, distancia)

        elif opcion == "3":
            mostrar_estructura()

        elif opcion == "4":
            listar_accesibles()

        elif opcion == "5":
            origen = input("Lugar de origen: ").strip()
            destino = input("Lugar de destino: ").strip()
            buscar_ruta_corta(origen, destino)

        elif opcion == "6":
            mostrar_grafo_texto()

        elif opcion == "7":
            print("Saliendo del sistema de rutas (versión grafo).")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# -----------------------------------------------------------
# Ejecución principal
# -----------------------------------------------------------
if __name__ == "__main__":
    print("Bienvenido a ConéctateUIS - versión con grafos (solo terminal).")
    cargar_datos_iniciales()
    menu()
