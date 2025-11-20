
# ConectateUIS - VRS Arboles

from bigtree import Node, print_tree, findall

# Node: representa un nodo del árbol.
# Tiene: name, parent, children, data, etc.

# print_tree: imprime el árbol en formato texto.

# findall: permite buscar nodos bajo una condición.


def buscar_nodo_por_nombre(raiz, nombre):

    nombre = nombre.strip().lower()
# El usuario puede escribir "biblioteca" o "Biblioteca" por eso normalizamos el texto a minúsculas.
   
    nodos = findall(raiz, lambda n: (
# findall recorre TODO el árbol desde la raíz.  

    (isinstance(n.name, str) and n.name.lower() == nombre) or
# El lambda dice:
# “Devuélveme los nodos cuyo nombre visible (n.name) coincida”.  
        
        (hasattr(n, "data") and isinstance(n.data, dict) and str(n.data.get("nombre", "")).lower() == nombre)
 # o cuyo dato interno (data["nombre"]) coincida.   
    ))
    
    return nodos[0] if nodos else None
# Si encuentra varios, tomamos solo el primero.



def buscar_nodo_por_id(raiz, id_buscar):
    id_s = str(id_buscar).strip().lower()
#Convertimos a string por si el usuario ingresa "4", "04" o un int.

    nodos = findall(raiz, lambda n: (
        hasattr(n, "data") and isinstance(n.data, dict) and str(n.data.get("id", "")).lower() == id_s
#Igual que la búsqueda por nombre, pero comparando data["id"].

    ))
    return nodos[0] if nodos else None

# -----------------------------------------------------------
# Creamos la raíz 
# -----------------------------------------------------------
campus = Node("Campus Principal", data={
    "id": 0,
    "nombre": "Campus Principal",
    "tipo": "Raíz",
    "descripcion": "Centro del sistema",
    "accesible": True,
    "conexiones": []
})

#separamos lo q ve el usuario y los datos que usamos internamente


# Demás Funciones principales 

#Agrega un nodo principal (hijo directo de la raíz).
def agregar_principal(data):

    Node(data["nombre"], data=data, parent=campus)
#Lo conectas como hijo directo del campus.

    print(f" Nodo '{data['nombre']}' agregado al campus.\n")


def conectar_nodos(nombre_padre, data_hijo):
#Conecta un nodo hijo bajo un padre existente (jerárquico).

    padre = buscar_nodo_por_nombre(campus, nombre_padre)
    # Se busca dentro del árbol si existe un nodo cuyo nombre coincida con nombre_padre
    
    if padre is None:
        print(f" El nodo '{nombre_padre}' no existe.\n")
        return

    hijo = Node(data_hijo["nombre"], data=data_hijo, parent=padre)
# Crea un nuevo nodo con el nombre del hijo.
# Le asigna la data_hijo a la data del nuevo nodo.
# Le dice a bigtree: “este nodo pertenece a este padre”.
    
    if isinstance(padre.data, dict):
        padre.data.setdefault("conexiones", []).append(data_hijo["id"])
    print(f" Se agregó '{data_hijo['nombre']}' como hijo de '{nombre_padre}'.\n")
# Guardas esa relación dentro del diccionario de datos del padre.


def mostrar_estructura():
#Imprime el arbol y la jerarquia
    print("\n Estructura actual del campus:\n")
    
    print_tree(campus)  # print_tree usa node.name para mostrar   
    print()


def buscar_por_nombre(nombre):
    nodo = buscar_nodo_por_nombre(campus, nombre)
# Llama a la función interna que recorre TODO el árbol y devuelve el nodo o None
 
    if nodo:
        d = nodo.data if isinstance(nodo.data, dict) else {}
#se asegura que d siempre sea un diccionario

        print(f"\n Encontrado: {d.get('nombre', nodo.name)} ({d.get('tipo', 'N/D')}) - accesible: {d.get('accesible', 'N/D')}\n")
        return nodo
    
    else:
        print("\n No se encontró el nodo.\n")
        return None


def buscar_por_id_func(id_buscar):
    nodo = buscar_nodo_por_id(campus, id_buscar)
# Llama a la función interna que recorre TODO el árbol y devuelve el nodo o None
    
    if nodo:
        d = nodo.data
# buscar por nombre necesita revisar dentro del diccionario del nodo para ver si tiene un campo

        print(f"\n Nodo con ID {d.get('id')}: {d.get('nombre')} ({d.get('tipo')})\n")
        return nodo
    
    else:
        print("\n No se encontró ningún nodo con ese ID.\n")
        return None


def listar_accesibles():
# Muestra los nodos marcados accesibles.

    print("\n Lugares accesibles del campus:")
    encontrados = False
# Si nunca encontramos uno, lo usamos al final para decir "No hay nodos accesibles".

    for nodo in list(campus.descendants):  # convertimos a lista para iterar seguro
        
        if isinstance(nodo.data, dict) and nodo.data.get("accesible"):
            #verificamos q data si sea un diccionario y q rengla la clave accesible como true
            
            print(f" - {nodo.data.get('nombre')}")
            encontrados = True
            
    if not encontrados:
        print(" No hay nodos accesibles registrados.")
    print()


def buscar_ruta(origen, destino):
# Busca ruta jerárquica simple entre dos nodos: sube hasta ancestro común y baja.

    nodo_origen = buscar_nodo_por_nombre(campus, origen)
    nodo_destino = buscar_nodo_por_nombre(campus, destino)

    if not nodo_origen or not nodo_destino:
        print("\n Uno o ambos lugares no existen.\n")
        return

    # Construimos listas de ascendencia (incluye el nodo mismo)
    anc_origen = [nodo_origen] + list(nodo_origen.ancestors)
    anc_destino = [nodo_destino] + list(nodo_destino.ancestors)

    # Buscamos primer ancestro común (el más cercano a los nodos)
    ancestro_comun = None
    for a in anc_origen:
        if a in anc_destino:
            ancestro_comun = a
            break

    print("\n Ruta sugerida:")
    if ancestro_comun:
        
        # construir ruta: origen -> ... -> ancestro -> ... -> destino
        subida = [
            n.data.get("nombre", n.name)
            for n in anc_origen
            if n != ancestro_comun and n not in anc_destino
        ]
        
        # ponemos ancestro
        medio = ancestro_comun.data.get("nombre", ancestro_comun.name)
        
        bajada = []
        
        # desde ancestro hasta destino (tomamos anc_destino hasta ancestro y la invertimos)
        ruta_dest_hasta_anc = []
        
        for n in anc_destino:
            ruta_dest_hasta_anc.append(n)
            if n == ancestro_comun:
                break
            
        # ruta desde ancestro hacia destino (excluimos ancestro y revertimos)
        ruta_down = list(reversed([
            n for n in ruta_dest_hasta_anc if n != ancestro_comun
        ]))


        bajada = [n.data.get("nombre", n.name) for n in ruta_down]

        ruta_final = subida + [medio] + bajada
        print(" → ".join(ruta_final) + "\n")
        
    else:
        print("3 No hay conexión jerárquica directa entre esos nodos.\n")


# Menú 
def menu():
    while True:
        print("\n===== MENÚ DEL CAMPUS =====")
        print("1. Agregar edificio o punto principal al campus")
        print("2. Agregar edificio o punto desde otro (Padre → Hijo)")
        print("3. Mostrar estructura jerárquica")
        print("4. Buscar por nombre")
        print("5. Buscar por ID")
        print("6. Listar accesibles")
        print("7. Buscar ruta entre lugares")
        print("8. Salir")

        opcion = input("\nElige una opción (1-8): ").strip()

        if opcion == "1":
            # Pedimos todos los datos 
            id_nuevo = len(list(campus.descendants)) + 1  # convertir generator a lista
            nombre = input("Nombre del nuevo edificio o zona: ").strip()
            tipo = input("Tipo: ").strip()
            descripcion = input("Descripción: ").strip()
            accesible = input("¿Es accesible? (s/n): ").strip().lower() == "s"
            data = {"id": id_nuevo, "nombre": nombre, "tipo": tipo,
                    "descripcion": descripcion, "accesible": accesible, "conexiones": []}
            agregar_principal(data)

        elif opcion == "2":
            padre = input("Nombre del nodo padre: ").strip()
            nombre = input("Nombre del nodo hijo: ").strip()
            tipo = input("Tipo del hijo: ").strip()
            descripcion = input("Descripción: ").strip()
            accesible = input("¿Es accesible? (s/n): ").strip().lower() == "s"
            id_nuevo = len(list(campus.descendants)) + 1
            data = {"id": id_nuevo, "nombre": nombre, "tipo": tipo,
                    "descripcion": descripcion, "accesible": accesible, "conexiones": []}
            conectar_nodos(padre, data)

        elif opcion == "3":
            mostrar_estructura()

        elif opcion == "4":
            nombre = input("Nombre del lugar a buscar: ").strip()
            buscar_por_nombre(nombre)

        elif opcion == "5":
            id_buscar = input("ID a buscar: ").strip()
            buscar_por_id_func(id_buscar)

        elif opcion == "6":
            listar_accesibles()

        elif opcion == "7":
            origen = input("Lugar de origen: ").strip()
            destino = input("Lugar de destino: ").strip()
            buscar_ruta(origen, destino)

        elif opcion == "8":
            print("\n Saliendo del sistema de rutas... ¡ Hasta la próxima !\n")
            break
        else:
            print("\n Opción no válida.\n")


# Simulación de edificios creamos como los edificios principales

agregar_principal({"id": 1, "nombre": "Edificio Central", "tipo": "Académico", "descripcion": "Edificio principal de clases", "accesible": True, "conexiones": []})


# Conexiones jerárquicas - Aqui creamos los hijos
conectar_nodos("Edificio Central", {"id": 2, "nombre": "Biblioteca", "tipo": "Académico", "descripcion": "Espacio de estudio y préstamo de libros", "accesible": True, "conexiones": []})

conectar_nodos("Edificio Central", {"id": 3, "nombre": "Cafetería", "tipo": "Servicios", "descripcion": "Zona de comidas para estudiantes y personal", "accesible": True, "conexiones": []})

conectar_nodos("Biblioteca", {"id": 4, "nombre": "Laboratorio de Sistemas", "tipo": "Académico", "descripcion": "Laboratorio con equipos de cómputo", "accesible": True, "conexiones": []})

conectar_nodos("Cafetería", {"id": 5, "nombre": "Cancha", "tipo": "Recreación", "descripcion": "Espacio deportivo para actividades físicas", "accesible": True, "conexiones": []})

conectar_nodos("Laboratorio de Sistemas", {"id": 5, "nombre": "Cancha", "tipo": "Recreación", "descripcion": "Espacio deportivo para actividades físicas", "accesible": True, "conexiones": []})

# Arranque

if __name__ == "__main__":
    print(" Bienvenido al sistema de rutas del campus universitario.")
    menu()
