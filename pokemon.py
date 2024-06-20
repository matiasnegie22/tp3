# Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, can-
# tidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y ade-
# más la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver
# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:

# a. obtener la cantidad de Pokémons de un determinado entrenador;

# b. listar los entrenadores que hayan ganado más de tres torneos;

# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;

# d. mostrar todos los datos de un entrenador y sus Pokémos;

# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;

# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);

# g. el promedio de nivel de los Pokémons de un determinado entrenador;

# h. determinar cuántos entrenadores tienen a un determinado Pokémon;

# i. mostrar los entrenadores que tienen Pokémons repetidos;

# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Te-
# rrakion o Wingull;

# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;
from LISTA import by_name,search,by_tournament,nivel,show_list_list
from random import choice


entrenadores = [
    {
        "nombre": "Ash Ketchum",
        "torneos_ganados": 7,
        "batallas_perdidas": 50,
        "batallas_ganadas": 120
    },
    {
        "nombre": "Goh",
        "torneos_ganados": 2,
        "batallas_perdidas": 10,
        "batallas_ganadas": 40
    },
    {
        "nombre": "Leon",
        "torneos_ganados": 10,
        "batallas_perdidas": 5,
        "batallas_ganadas": 100
    },
    {
        "nombre": "Chloe",
        "torneos_ganados": 1,
        "batallas_perdidas": 8,
        "batallas_ganadas": 30
    },
    {
        "nombre": "Raihan",
        "torneos_ganados": 4,
        "batallas_perdidas": 15,
        "batallas_ganadas": 60
    }
]


pokemones = [
     {
        "nombre": "Pikachu",
        "nivel": 10,
        "tipo": "Eléctrico",
        "subtipo": None
    },
     {
        "nombre": "Pikachu",
        "nivel": 10,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "nombre": "Pikachu",
        "nivel": 10,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "nombre": "Pikachu",
        "nivel": 35,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "nombre": "Charizard",
        "nivel": 40,
        "tipo": "Fuego",
        "subtipo": "Planta"
    },
    {
        "nombre": "Bulbasaur",
        "nivel": 30,
        "tipo": "Planta",
        "subtipo": "Veneno"
    },
    {
        "nombre": "Starmie",
        "nivel": 30,
        "tipo": "Agua",
        "subtipo": "Psíquico"
    },
    {
        "nombre": "Psyduck",
        "nivel": 25,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Gyarados",
        "nivel": 35,
        "tipo": "Agua",
        "subtipo": "Volador"
    },
    {
        "nombre": "Terrakion",
        "nivel": 38,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Geodude",
        "nivel": 28,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Vulpix",
        "nivel": 20,
        "tipo": "Fuego",
        "subtipo": None
    },
    {
        "nombre": "Blastoise",
        "nivel": 50,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Umbreon",
        "nivel": 45,
        "tipo": "Siniestro",
        "subtipo": None
    },
    {
        "nombre": "Nidoking",
        "nivel": 40,
        "tipo": "Veneno",
        "subtipo": "Tierra"
    }
]

list_pokemones=[ "Pikachu","Charizard","Bulbasaur","Starmie","Psyduck","Gyarados","Onix","Geodude","Vulpix","Blastoise","Umbreon","Nidoking",]
list_nombre=["Ash Ketchum","Goh","Leon","Chloe","Raihan"]
list_completa=[]

for entrenador in entrenadores:
    entrenador.update({'pokemones':[]})
    list_completa.append(entrenador)


for pokemon in pokemones:
    pos=search(list_completa,'nombre',choice(list_nombre))
    if pos is not None:
        list_completa[pos]['pokemones'].append(pokemon)
    else:
        print("no existe el entrenador")

for pokemon in pokemones:
    pos=search(list_completa,'nombre',choice(list_nombre))
    if pos is not None:
        list_completa[pos]['pokemones'].append(pokemon)
    else:
        print("no existe el entrenador")

# a) obtener la cantidad de Pokémons de un determinado entrenador;
print()
def cant_pokemones(list_completa):
    pos=search(list_completa,'nombre','Goh')
    return len(list_completa[pos]['pokemones'])
det_entrenador=cant_pokemones(list_completa)
print("el entrenador Goh tiene",det_entrenador,"pokemones")


# b. listar los entrenadores que hayan ganado más de tres torneos;
print()
entrenadores.sort(key=by_tournament,reverse=True)
print("los que ganaron mas torneos son:")
def mas_de_3(entrenadores):
    for index,elements in enumerate(entrenadores):
        if elements['torneos_ganados']>3:
            print(index,elements['nombre'])
    return ()
mas_de_3(entrenadores)


# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
print()
def mas_lvl_mas_torneo(list_completa):
    aux=0
    aux2=0
    for index,elements in enumerate(list_completa):
        if list_completa[index]['torneos_ganados'] > aux:
            aux=list_completa[index]['torneos_ganados']
            nombre=list_completa[index]['nombre']
            pos=index
    for index,elements in enumerate(list_completa):
        list_completa[pos]['pokemones'].sort(key=nivel,reverse=True)
        aux2=list_completa[pos]['pokemones'][0]
    return print("el pokemon con mayor nivel es ",aux2,"y pertenece a",nombre)
mas_lvl_mas_torneo(list_completa)


# d. mostrar todos los datos de un entrenador y sus Pokémon;
print()
def todo_dato_pokeyentrenador(list_completa):
    pos=search(list_completa,'nombre',choice(list_nombre))
    return print("los datos del entrenador son:",list_completa[pos])
todo_dato_pokeyentrenador(list_completa)


# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
print()
print("las personas que tienen mas de 79% porciento de victorias son:")
def porcentaje_79(entrenadores):
    for index,elements in enumerate(entrenadores):
        total=entrenadores[index]['batallas_ganadas'] + entrenadores[index]['batallas_perdidas']
        porcentaje=(entrenadores[index]['batallas_ganadas'] / total) * 100
        if porcentaje>79:
            print(entrenadores[index]['nombre'])
    return()
porcentaje_79(entrenadores)


# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);
print()
def tiposde_fuego(lista_completa):
    for index,elements in enumerate(lista_completa):
        pos0=search(lista_completa,'nombre',list_nombre[index])
        if pos0 is not None:
            pos = search(lista_completa[pos0]['pokemones'],'tipo','Fuego')
            if pos is not None:
                pos2=search(lista_completa[pos0]['pokemones'],'subtipo','Planta')
                if pos2 is not None:
                    print("los entrenadores que tienen pokemones de tipo fuego y planta son", lista_completa[pos0]['nombre'])
    return()
tiposde_fuego(list_completa)

def tipos_agua(lista_completa):
    for index,elements in enumerate(lista_completa):
        pos0=search(lista_completa,'nombre',list_nombre[index])
        if pos0 is not None:
            pos = search(lista_completa[pos0]['pokemones'],'tipo','Agua')
            if pos is not None:
                pos2=search(lista_completa[pos0]['pokemones'],'subtipo','Volador')
                if pos2 is not None:
                    print("los entrenadores que tienen pokemones de tipo agua y volador son", lista_completa[pos0]['nombre'])
    return()
tipos_agua(list_completa)


# g. el promedio de nivel de los Pokémons de un determinado entrenador;
print()
def promedio_nivel(list_completa):
    suma=0
    pos=search(list_completa,'nombre',choice(list_nombre))
    cant_pokemones=len(list_completa[pos]['pokemones'])
    for pokemon in list_completa[pos]['pokemones']:
        nivel= pokemon['nivel']   
        suma+=nivel
    promedio=suma/cant_pokemones
    return print("el promedio  en el nivel de los pokemones es de",list_completa[pos]['nombre'],"es de:",promedio,"%")
promedio_nivel(list_completa)


# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
print()
def pokemon_det(list_completa,list_pokemones,list_nombre):
    acm=0
    for index,element in enumerate(list_completa):
        pos0=search(list_completa,'nombre',list_nombre[index])
        if pos0 is not None:
            pos=search(list_completa[pos0]['pokemones'],'nombre','Pikachu')
            if pos is not None:
                acm+=1
                print("las personas que tienen a al pokemon pikachu son:",acm,list_completa[pos0]['nombre'])
    return 
pokemon_det(list_completa,list_pokemones,list_nombre)


# i. mostrar los entrenadores que tienen Pokémons repetidos;
print()
def pokemon_repetido(list_completa):
    for index, entrenador in enumerate(list_completa):
        repetidos=[]
        for index_2, pokemon in range (len((entrenador['pokemones']))):
            for nextPokemon in range (index_2+1,len(entrenador['pokemones'])):
                if pokemon['nombre'] == entrenador['pokemones'][nextPokemon]['nombre']:
                    if pokemon['nombre'] not in repetidos:
                        repetidos.append(pokemon['nombre'])
        if len(repetidos)>0:                 
            print("Los pokemones repetidos son ",repetidos, "y pertenecen a ", list_completa[index]['nombre'])   
    return()     
pokemon_repetido(list_completa)


# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Te-
# rrakion o Wingull;
print()
def det_pokemones(list_completa,list_nombre):
    for index,elements in enumerate(list_completa):
        pos=search(list_completa,'nombre',list_nombre[index])
        for pokemon in list_completa[pos]['pokemones']:
            if pokemon['nombre']== 'Tyrantrum' or pokemon['nombre']=='Terrakion' or pokemon['nombre']=='Wingull':
                print("el entrenador",list_completa[pos]['nombre'],'tiene el pokemon',pokemon['nombre'])
    return
det_pokemones(list_completa,list_nombre)


# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;
print()
def entx_pokemony(list_completa,list_nombre,list_pokemon):
    x=input("ingrese el nombre del entrenador ")
    y=input("ingrese el nombre del pokemon ")
    print()
    for index, elements in enumerate(list_completa):
        pos=search(list_completa,'nombre',x)
        if pos is not None:
            pos2=search(list_completa[pos]['pokemones'],'nombre',y)
            if pos2 is not None:
                print("datos del entrenador",list_completa[pos])
                print()
                print("datos del pokemon",list_completa[pos]['pokemones'][pos2])
                return 
            else:
                return print("el pokemon no se encontro")                            
        


show_list_list('enetrenadores','pokemones',list_completa)