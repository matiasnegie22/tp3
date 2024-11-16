# 15. 
from Grafo import Graph
from random import randint

#
grafo = Graph(dirigido=False)

arquitectonicas=[
    {'nombre': 'Chichén Itzá', 'other_values': {'pais': 'México', 'tipo': 'arquitectónica'}},
    {'nombre': 'Cristo Redentor', 'other_values': {'pais': 'Brasil', 'tipo': 'arquitectónica'}},
    {'nombre': 'Machu Picchu', 'other_values': {'pais': 'Perú', 'tipo': 'arquitectónica'}},
    {'nombre': 'Gran Muralla China', 'other_values': {'pais': 'China', 'tipo': 'arquitectónica'}},
    {'nombre': 'Petra', 'other_values': {'pais': 'Jordania', 'tipo': 'arquitectónica'}},
    {'nombre': 'Coliseo', 'other_values': {'pais': 'Italia', 'tipo': 'arquitectónica'}},
    {'nombre': 'Taj Mahal', 'other_values': {'pais': 'India', 'tipo': 'arquitectónica'}}
]

naturales=[
    {'nombre': 'Amazonas', 'other_values': {'pais': 'Brasil', 'tipo': 'natural'}},
    {'nombre': 'Bahía de Ha-Long', 'other_values': {'pais': 'Vietnam', 'tipo': 'natural'}},
    {'nombre': 'Cataratas del Iguazú', 'other_values': {'pais': 'Argentina', 'tipo': 'natural'}},
    {'nombre': 'Isla Jeju', 'other_values': {'pais': 'Corea del Sur', 'tipo': 'natural'}},
    {'nombre': 'Parque Nacional de Komodo', 'other_values': {'pais': 'Indonesia', 'tipo': 'natural'}},
    {'nombre': 'Río Subterráneo de Puerto Princesa', 'other_values': {'pais': 'Filipinas', 'tipo': 'natural'}},
    {'nombre': 'Montaña de la Mesa', 'other_values': {'pais': 'Sudáfrica', 'tipo': 'natural'}}
]

for h in range (2):
    maravillas = arquitectonicas if h == 0 else naturales
    for maravilla in maravillas:
        grafo.insert_vertice(maravilla['nombre'], maravilla['other_values'])

# b.
for h in range (2):
    maravillas = arquitectonicas if h == 0 else naturales
    for i in range(0, len(maravillas)-1):
        for j in range(i+1, len(maravillas)):
            grafo.insert_arista(maravillas[i]['nombre'], maravillas[j]['nombre'], randint(500, 20000))

# c.
for h in range (2):
    maravillas = arquitectonicas if h == 0 else naturales
    for i in range(0, len(maravillas)-1):
        print(f"El arbol de expansion minimo de {maravillas[i]['nombre']} es {grafo.kruskal(maravillas[i]['nombre'])}")
print("")

# d
paisarquitectonica= []
paisnatural= []
for h in range (2):
    maravillas = arquitectonicas if h == 0 else naturales
    pais= paisarquitectonica if h == 0 else paisnatural
    for maravilla in maravillas:
        value=grafo.search_other(maravilla['nombre'], None)
        pais.append(value)

for i in paisarquitectonica:
    for j in pais_natural:
        if i['pais']==j['pais']:
            print(f"En {i['pais']} existen maravillas arquitectonicas y naturales")
print("")

# e.
for h in range (2):
    pais = paisarquitectonica if h == 0 else paisnatural
    tipo = "arquitectonica" if h == 0 else "natural"    
    for i in range (0, len(pais)-1):
        for j in range (i+1, len(pais)):
            if pais[i]['pais']==pais[j]['pais']:
                print(f"En {pais[i]['pais']} hay mas de una maravilla {tipo}")
