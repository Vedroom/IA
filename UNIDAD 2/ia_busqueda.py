from collections import deque

#Clase que define un nodo en el 8-puzzle.
class Nodo:
    def __init__(self, estado, padre, movimiento, profundidad, piezas_correctas):        
        self.estado = estado                        #Posición atual de las piezas.
        self.padre = padre                          #Nodo desde el que se llega a este nodo.
        self.movimiento = movimiento                #Movimiento para encontrar este nodo desde el padre.
        self.profundidad = profundidad              #Posición del nodo en el árbol de búsqueda.
        self.piezas_correctas = piezas_correctas    #Total de piezas en su lugar para este estado.

    #Método para mover las piezas en direcciones posibles.
    def mover(self, direccion):
        estado = list(self.estado)
        ind = estado.index(0)

        if direccion == "arriba":            
            if ind not in [6, 7, 8]:                
                temp = estado[ind + 3]
                estado[ind + 3] = estado[ind]
                estado[ind] = temp
                return tuple(estado)
            else:                
                return None

        elif direccion == "abajo":            
            if ind not in [0, 1, 2]:                
                temp = estado[ind - 3]
                estado[ind - 3] = estado[ind]
                estado[ind] = temp
                return tuple(estado)
            else:                
                return None

        elif direccion == "derecha":            
            if ind not in [0, 3, 6]:                
                temp = estado[ind - 1]
                estado[ind - 1] = estado[ind]
                estado[ind] = temp
                return tuple(estado)
            else:                
                return None

        elif direccion == "izquierda":            
            if ind not in [2, 5, 8]:                
                temp = estado[ind + 1]
                estado[ind + 1] = estado[ind]
                estado[ind] = temp
                return tuple(estado)
            else:                
                return None        

    #Método que encuentra y regresa todos los nodos sucesores del nodo actual.
    def encontrar_sucesores(self):
        sucesores = []
        sucesorN = self.mover("arriba")
        sucesorS = self.mover("abajo")
        sucesorE = self.mover("derecha")
        sucesorO = self.mover("izquierda")
        
        sucesores.append(Nodo(sucesorN, self, "arriba", self.profundidad + 1, calcular_heurisitica(sucesorN)))
        sucesores.append(Nodo(sucesorS, self, "abajo", self.profundidad + 1, calcular_heurisitica(sucesorS)))
        sucesores.append(Nodo(sucesorE, self, "derecha", self.profundidad + 1, calcular_heurisitica(sucesorE)))
        sucesores.append(Nodo(sucesorO, self, "izquierda", self.profundidad + 1, calcular_heurisitica(sucesorO)))
        
        sucesores = [nodo for nodo in sucesores if nodo.estado != None]  
        return sucesores

    #Método que encuentra el camino desde el nodo inicial hasta el actual.
    def encontrar_camino(self, inicial):
        camino = []
        nodo_actual = self
        while nodo_actual.profundidad >= 1:
            camino.append(nodo_actual)
            nodo_actual = nodo_actual.padre
        camino.reverse()
        return camino

    #Método que imprime ordenadamente el estado (piezas) de un nodo.
    def imprimir_nodo(self):
        renglon = 0
        for pieza in self.estado:
            if pieza == 0:
                print(" ", end = " ")
            else:
                print (pieza, end = " ")
            renglon += 1
            if renglon == 3:
                print()
                renglon = 0       

#Función que calcula la cantidad de piezas que están en su lugar para un estado dado.
def calcular_heurisitica(estado):
    correcto = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    valor_correcto = 0
    piezas_correctas = 0
    if estado:
        for valor_pieza, valor_correcto in zip(estado, correcto):
            if valor_pieza == valor_correcto:
                piezas_correctas += 1
            valor_correcto += 1
    return piezas_correctas   

#Algoritmo Breadth First Search.
def bfs(inicial, meta):
    visitados = set()   #Conjunto de estados visitados para no visitar el mismo estado más de una vez.
    frontera = deque()  #Cola de nodos aún por explorar. Se agrega el nodo inicial.  
    frontera.append(Nodo(inicial, None, None, 0, calcular_heurisitica(inicial)))
    
    while frontera:                         #Mientras haya nodos por explorar:
        nodo = frontera.popleft()           #Se toma el primer nodo de la cola.

        if nodo.estado not in visitados:    #Si no se había visitado, 
            visitados.add(nodo.estado)      #se agrega al conjunto de visitados.
        else:                               #Si ya se había visitado
            continue                        #se ignora.
        
        if nodo.estado == meta:                         #Si es una meta, 
            print("\n¡Se encontró la meta!")            
            return nodo.encontrar_camino(inicial)       #se regresa el camino para llegar a él y termina el algoritmo.        
        else:                                           #Si no es una meta, 
            frontera.extend(nodo.encontrar_sucesores()) #se agregan sus sucesores a los nodos por explorar.

#Función main.
def main():
    estado_final =(1, 2, 3, 4, 5, 6, 7, 8, 0)
    estado_in = []
    # Inicializar un conjunto para realizar verificación de duplicados
    valores_previos = set()        
    # Solicitar al usuario que ingrese los valores del arreglo
    print("\n\nIngresa los valores del estado inicial, ingresa 0 para el espacio vacío \n")
    for i in range(3):
        for j in range(3):
            while True:
                valor = int(input(f"\tValor : {i},{j} = "))
                #estado_inicial.append(valor)
                if valor not in estado_in:
                    valores_previos.add(valor)
                    estado_in.append(valor)
                    break
                else:
                    print("\t\n Error: El valor ya existe en el arreglo. Introduce un valor diferente.")
    estado_inicial = tuple(estado_in)
    
    #Menú principal
    print("\nEl estado inicial del juego es: ")
    (Nodo(estado_inicial, None, None, 0, calcular_heurisitica(estado_inicial))).imprimir_nodo()
    print("\nResolucion de puzzle deslizante através del algoritmo Breadth-First Search")
    print("\nIngresa el valor a rastrear")
    n = int(input(f"\n\tValor =  "))
    
    #Coordenadas iniciales       
    x = estado_inicial.index(n) // 3
    y = estado_inicial.index(n) % 3
    
    #Coordenadas finales
    xf = estado_final.index(n) // 3
    yf = estado_final.index(n) % 3
    
    print(f"\n\t {n} se encuentra inicialmente en la coordenada {x},{y}")
    print(f"\n\t {n} se encuentra finalmene en la coordenada {xf},{yf}")
    nodos_camino = bfs(estado_inicial, estado_final)
    
    #Se imprime el camino si existe y si el usuario lo desea.
    if nodos_camino:
        print ("El camino tiene", len(nodos_camino), "movimientos.")
        imprimir_camino = (input ("¿Desea imprimir camino? s/n: "))

        if imprimir_camino == "s" or imprimir_camino == "S":
            print("\nEstado inicial:")
            (Nodo(estado_inicial, None, None, 0, calcular_heurisitica(estado_inicial))).imprimir_nodo()
            print ("Piezas correctas:", calcular_heurisitica(estado_inicial), "\n")
            input("Presione \"enter\" para continuar.")
            
            for nodo in nodos_camino:
                print("\nSiguiente movimiento:", nodo.movimiento)
                print("Estado actual:")
                nodo.imprimir_nodo()
                print("Piezas correctas:", nodo.piezas_correctas, "\n")     
                input("Presione \"enter\" para continuar.")
    else:
        print ("\nNo se encontró un camino")

    return 0    

if __name__ == "__main__":
    main()