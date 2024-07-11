
#Escribir un algoritmo que permita utilizar tres tablas hash para guardar los datos de Pokémons,
#que contemple las siguientes actividades: 

#a. en la primera tabla hash la función hash debe ser sobre el tipo de Pokémon, en la segunda
#tabla la función hash deberá utilizar el ultimo dígito del número del Pokémon como clave y
#  la tercera sera en base  a su nivel repartiéndolos en 10 posiciones dentro de la tabla; 

def hash_tipo(pokemons):
    return pokemon["tipo"]

def hash_subtipo(pokemons):
    return pokemon["subtipo"]

def hash_numero(pokemons):
    return pokemon["numero"]%10

def hash_nivel(pokemons):
    return pokemon["nivel"]%10


table_tipo={}
table_numero={}
table_nivel={}
table_subtipo={}

pokemons=[
    {"nombre": "Bulbasaur", "tipo": "Plantas","subtipo":"veneno", "nivel": 5, "numero": 1},
    {"nombre": "Charmander", "tipo": "Fuego","subtipo":"", "nivel": 4, "numero": 4},
    {"nombre": "Squirtle", "tipo": "Agua","subtipo":"", "nivel": 88, "numero": 7},
    {"nombre": "Pikachu", "tipo": "Eléctrico","subtipo":"", "nivel": 61, "numero": 25},
    {"nombre": "Jigglypuff", "tipo": "Normal","subtipo":"Hada", "nivel": 5, "numero": 39},
    {"nombre": "Meowth", "tipo": "Normal","subtipo":"", "nivel": 1, "numero": 52},
    {"nombre": "Psyduck", "tipo": "Agua","subtipo":"", "nivel": 25, "numero": 54},
    {"nombre": "Machop", "tipo": "Lucha","subtipo":"", "nivel": 38, "numero": 66},
    {"nombre": "Tentacool", "tipo": "Agua","subtipo":"", "nivel": 55, "numero": 72},
    {"nombre": "Geodude", "tipo": "Roca","subtipo":"Tierra", "nivel": 10, "numero": 74},
    {"nombre": "Nidorino" , "tipo": "Veneno","subtipo":"", "nivel": 32, "numero":33 },
    {"nombre": "Blastoise" , "tipo": "Agua","subtipo":"", "nivel": 5, "numero":9},
    {"nombre": "Glaceon" , "tipo": "Hielo","subtipo":"", "nivel": 5 , "numero":471},
    {"nombre": "Metagross" , "tipo": "Acero","subtipo":"Psíquico", "nivel": 55 , "numero":376}
]


#b. debe utilizar tablas hash abiertas con listas como estructura secundaria;

for pokemon in pokemons:
    valur=hash_tipo(pokemon)
    if valur not in table_tipo:
        table_tipo[valur]=[]
    table_tipo[valur].append(pokemon)

    valur_2=hash_nivel(pokemon)
    if valur_2 not in table_nivel:
        table_nivel[valur_2]=[]
    table_nivel[valur_2].append(pokemon)

    valur_3=hash_numero(pokemon)
    if valur_3 not in table_numero:
        table_numero[valur_3]=[]
    table_numero[valur_3].append(pokemon)

    valur_4=hash_subtipo(pokemon)
    if valur_4 not in table_subtipo:
            table_subtipo[valur_4]=[]
    table_subtipo[valur_4].append(pokemon)

    

#print(f"tipo de pokemon: {table_tipo}")
#print()
#print(f"digito del pokemon: {table_numero}")
#print()
#print(f"nivel de pokemon: {table_nivel}")
#print()
#print(table_subtipo)
#print()
#c. si el Pokémon es de más de un tipo deberá cargarlo en cada uno de las tabla que indiquen estos tipos;

def subtipo_pokemon(pokemons):
    for pokemon in pokemons:
        if pokemon["subtipo"] !="":
            print("este pokemon tiene dos tipos: ",pokemon["nombre"])

subtipo_pokemon(pokemons)

print()
#d. deberá permitir cargar Pokémons de los cuales se dispone de su número, nombre, tipo/s, nivel.
def agregar_pokemon(numero, nombre, tipo, nivel):
    pokemon = {"numero": numero, "nombre": nombre, "tipo": tipo, "nivel": nivel}
    pokemons.append(pokemon)

#numero=input(int("ingrese el numero de el pokemon: "))
#nombre=input("ingrese el nombre de el pokemon: ")
#tipo=input("ingrese el tipo de pokemon, en el caso que tenga mas de un tipo agregar de la siguiente manera,["tipo", "subtipo"]: ")
#nivel=input(int("ingrese el nivel de el pokemon: "))
numero = 33  
nombre = "Nidorino" 
tipo = ["Veneno"]  
nivel = 32 

agregar_pokemon(numero, nombre, tipo, nivel)
print()
#e. mostrar todos los Pokémons cuyos numeros terminan en 3, 7 y 9;
print(f"los pokemons cuyos numero terminan en 3 son: {table_numero[3]}")
print(f"los pokemons cuyos numero terminan en 7 son: {table_numero[7]}")
print(f"los pokemons cuyos numero terminan en 9 son: {table_numero[9]}")
print()
#f. mostrar todos los Pokémons cuyos niveles son multiplos de 2, 5 y 10;

def niveles_multiplos(pokemos):
    for pokemon in pokemons:
        if (pokemon["nivel"] % 2)== 0:
            print(f"estos son los pokemon cuyos niveles son multiplos de 2: {pokemon}")
        if (pokemon["nivel"] % 5)== 0:
            print(f"estos son los pokemon cuyos niveles son multiplos de 5: {pokemon}")
        if (pokemon["nivel"] % 10)== 0:
            print(f"estos son los pokemon cuyos niveles son multiplos de 10: {pokemon}")

niveles_multiplos(pokemons)
print()
#g. mostrar todos los Pokémons de los siguientes tipo: Acero, Fuego, Electrifico, Hielo

print("los pokemon de tipo Acero son: ",table_tipo["Acero"])
print("los pokemon de tipo Fuego son: ",table_tipo["Fuego"])
print("los pokemon de tipo Electrifico son: ",table_tipo["Eléctrico"])
print("los pokemon de tipo Hielo son: ",table_tipo["Hielo"])
