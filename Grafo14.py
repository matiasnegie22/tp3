# 14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las si-
# guientes tareas:

from Grafo import Graph
from random import randint

grafo = Graph(dirigido=False)

# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,

casa=["cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2", "habitacion 1", "habitacion 2", "sala de estar", "terraza", "patio"]

for ambiente in casa:
    grafo.insert_vertice(ambiente)

# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista 

for ambiente in casa:
    adyacentes=[]
    can_aristas = 5 if ambiente in ["sala de estar", "patio"] else 3
    while len(adyacentes)<can_aristas:
        destino=casa[randint(0,len(casa)-1)]
        personaje1=grafo.search_arista(destino, ambiente)
        personaje2 =grafo.search_arista(ambiente, destino)
        if destino!=ambiente and destino not in adyacentes and personaje1 is None:
            adyacentes.append(destino)
    for destino in adyacentes:
        grafo.insert_arista(ambiente, destino, randint(3,20))

#c
cable=0

for nodo in grafo.kruskal("sala de estar")[0].split(';'):
    cable += int(nodo.split('-')[-1])
print(f"Se necesitan  metros de cable")
print("")

# d.
camino=grafo.dijkstra("habitacion 1")
destino="sala de estar"
camino_completo=[]
peso=0
while camino.size()>0:
    ambiente= camino.pop()
    if ambiente[1][0] == destino:
        camino_completo.append(ambiente[1][0])
        peso+=ambiente[0]
        destino=ambiente[1][2]
camino_completo.reverse()        
print(f"El camino mas corto desde la habitacion 1 es  {camino_completo}, y {peso} metros de cable seran necesarios.")