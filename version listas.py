
# - Cada nodo tiene campo 'accesible' (bool) y 'conexiones' (lista de ids de nodos conectados directamente).
# - Se agregan métodos para listar nodos accesibles, buscar nodos por nombre/id 
#   y encontrar una ruta entre dos nodos usando solo nodos accesibles (BFS simple).

class Nodo:
    def __init__(self, data):
        
        # data propuesta: {'id', 'nombre', 'tipo', 'descripcion', 'accesible', 'conexiones'}

        self.data = data
        self.siguiente = None


class ListaSE:
    def __init__(self):
        self.cabeza = None

    # Verificar si la lista está vacía, devuelve T or F
    def vacio(self):
        return self.cabeza is None

    # Agregar siempre al inicio (requisito)
    def agregarInicio(self, data):
        nuevo_nodo = Nodo(data)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    #supongo q en un futuro nos pedira implementar q se pueda agregar al final o por index pero como la actividad es asi; pues qda asi
    
    # Cantidad de nodos
    def cantidadNodos(self):
        cont = 0
        nodo = self.cabeza
        while nodo:        # El ciclo se repite mientras nodo no sea None
            cont += 1
            nodo = nodo.siguiente
        return cont

    # Imprimir lista (legible)
    def imprimir(self):
        
        if self.vacio():                    #con la funcion creada anteriormente se verifica q si hayan datos para no perder memoria
            print("La lista está vacía.")
            return
        
        nodo = self.cabeza
        i = 0
        while nodo:          #hasta q ya no haya nodo q evaluar  
            d = nodo.data
            print(f"[{i}] id:{d.get('id')} - {d.get('nombre')} ({d.get('tipo')}) - accesible: {d.get('accesible')} - conexiones:{d.get('conexiones')}")
            nodo = nodo.siguiente
            i += 1

    # Buscar nodo por nombre
    def buscar(self, nombre):
        nodo = self.cabeza
            
        while nodo:
            if nodo.data.get('nombre') == nombre:
                return nodo.data
            nodo = nodo.siguiente
                
        return None
        
        
    # Ordenar lista enlazada por nombre (bubble sort básico)
    def ordenar_por_nombre(self):
        
        if self.cabeza is None: #vacio
            return
        
        cambiado = True #Esto controla si hubo algún intercambio. Si en una pasada no cambia nada es pq ya esta ordenado
        
        while cambiado:
            cambiado = False
            nodo = self.cabeza
            
            while nodo.siguiente:  #hasta q ya no haya siguiente     
                
                if nodo.data["nombre"] > nodo.siguiente.data["nombre"]: 
                    #Si el nombre del nodo actual es "mayor" (alfabéticamente) que el del siguiente → los intercambia.
                    
                    nodo.data, nodo.siguiente.data = nodo.siguiente.data, nodo.data
                    #Aquí no movemos los nodos, solo intercambias la información (data) entre ellos. Más fácil que andar reacomodando punteros.
                    
                    cambiado = True
                    #hacemos otra vez True pq lo habiamos hecho false x si no entraba
                    
                nodo = nodo.siguiente

    # Buscar nodo por id
    def buscar_por_id(self, id_buscar):
        nodo = self.cabeza
        while nodo:
            if nodo.data.get('id') == id_buscar:
                return nodo.data
            nodo = nodo.siguiente
        return None

    # Listar todos los nodos accesibles
    def listar_accesibles(self):
        nodo = self.cabeza
        accesibles = []         #Lista vacía donde se van a guardar los nodos que cumplan la condición.
        
        while nodo:
            
            #Usa .get() y busca la palabra clave 'accesible'
            # Si no existe, devuelve False por defecto.
            # Si existe y es True el nodo se considera accesible.    
            if nodo.data.get('accesible', False):
                
                accesibles.append(nodo.data)
                #Guarda el diccionario completo de ese nodo en la lista accesibles.
                
            nodo = nodo.siguiente
            
        return accesibles


# Ej=

lista = ListaSE()

# Creamos nodos con conexiones simples (ids). Nota: agregamos al inicio, por eso insertamos en orden inverso
nodos = [
        {'id': 1, 'nombre': 'Bloque A', 'tipo': 'Edificio',
         'descripcion': 'Aulas 1-10', 'accesible': True, 'conexiones': [2]},
        {'id': 2, 'nombre': 'Biblioteca', 'tipo': 'Servicio',
         'descripcion': 'Sala de lectura', 'accesible': True, 'conexiones': [1, 3]},
        {'id': 3, 'nombre': 'Cafetería', 'tipo': 'Comercio',
         'descripcion': 'Comidas rápidas', 'accesible': False, 'conexiones': [2]}
    ]

#Para agregar es dependiendo de lo buscado
# si queremos q se vea como 1, 2, 3 seria mejor un insertar al final; 
# pero como nos mandaron a agregar al inicio vamos a usar reversed
# 
# for n in nodos:  
#   lista.agregarInicio(n)
# 
# La lista final será: [3, 2, 1]
# 
# Pero si usamos 
# 
# for n in reversed(nodos): 
#    lista.agregarInicio(n)
# 
#si se va a ver como 1, 2, 3
# #

for n in reversed(nodos):
    lista.agregarInicio(n)


print(" Lista completa:")
lista.imprimir()

print("\n Cantidad de nodos en la lista:")
print(lista.cantidadNodos())

print("\n Buscando por nombre 'Biblioteca':")
print(lista.buscar("Biblioteca"))

print("\n Buscando por id 3:")
print(lista.buscar_por_id(3))

print("\n Listar nodos accesibles:")

for a in lista.listar_accesibles():
    print(f"- {a['nombre']}") #a va representando como el index de la lista; avanza conforme avanza la lista llegando al final

print("\n Ordenando por nombre (alfabético):")
lista.ordenar_por_nombre()
lista.imprimir()
