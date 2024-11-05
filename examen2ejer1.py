from arbol import BinaryTree
from arbol_avl import BinaryTree

tree_by_name = BinaryTree()
tree_by_number = BinaryTree()
tree_by_type = BinaryTree()

#A)
pokemons = [
    {"nombre": "Bulbasaur", "numero": 1, "tipo": ["planta", "veneno"]},
    {"nombre": "Charmander", "numero": 4, "tipo": ["fuego"]},
    {"nombre": "Jolteon", "numero": 135, "tipo": ["eléctrico"]},
    {"nombre": "Tyrantrum", "numero": 697, "tipo": ["roca", "dragón"]},
    {"nombre": "Pikachu", "numero": 25, "tipo": ["eléctrico"]},
    {"nombre": "Gyarados", "numero": 130, "tipo": ["agua", "volador"]},
    {"nombre": "Torterra", "numero": 389, "tipo": ["planta", "tierra"]},
    {"nombre": "Electrode", "numero": 101, "tipo": ["eléctrico", "veneno"]},
    {"nombre": "Lycanroc", "numero": 745, "tipo": ["roca"]},
    {"nombre": "Squirtle", "numero": 7, "tipo": ["agua"]},
    {"nombre": "Butterfree", "numero": 12, "tipo": ["bicho", "volador"]},
    {"nombre": "Gengar", "numero": 94, "tipo": ["fantasma", "veneno"]},
    {"nombre": "Snorlax", "numero": 143, "tipo": ["normal"]},
    {"nombre": "Lucario", "numero": 448, "tipo": ["lucha", "acero"]},
    {"nombre": "Greninja", "numero": 658, "tipo": ["agua", "siniestro"]},
    {"nombre": "Corviknight", "numero": 822, "tipo": ["volador", "acero"]},
    {"nombre": "Cinderace", "numero": 814, "tipo": ["fuego"]},
    {"nombre": "Dragonite", "numero": 149, "tipo": ["dragón", "volador"]},
    {"nombre": "Metagross", "numero": 376, "tipo": ["psíquico", "acero"]},
]



for pokemon in pokemons:
    tree_by_name.insert_node(pokemon["nombre"], other_value=pokemon)
    tree_by_number.insert_node(pokemon["numero"], other_value=pokemon)
    for tipos in pokemon["tipo"]:
        tree_by_type.insert_node(tipos, other_value=pokemon)
        

#B)
def mostrar_pokemon_n(numero):
    pokemon_bynumber = tree_by_number.search(numero)
    if pokemon_bynumber is not None:
        print(pokemon_bynumber.other_value)
    else: print("no se encontró el pokemon con dicho número", numero)
print()
mostrar_pokemon_n(4)
print()
print(tree_by_name.proximity_search("bul"))


#C)
print()
print("tipo agua")
tree_by_type.mostrar_pokemons_por_tipo("agua")
print()
print("tipo fuego")
tree_by_type.mostrar_pokemons_por_tipo("fuego")
print()
print("tipo planta")
tree_by_type.mostrar_pokemons_por_tipo("planta")
print()
print("tipo electrico")
tree_by_type.mostrar_pokemons_por_tipo("eléctrico")
print()


#D)
print()
print("por numero")
tree_by_number.inorden()
print()
print ("por nombre")
tree_by_name.inorden()
print()
print("por nombre, pero en nivel")
tree_by_name.by_level()


#E)
print()
def mostrar_pokemones():
    for name in ["Jolteon", "Lycanroc", "Tyrantrum"]:
        pokemon = tree_by_name.search(name)
        if pokemon is not None:
            print(pokemon.other_value)

mostrar_pokemones()


#F)
print()
def contartipos():
    electricos = tree_by_type.contar_pokemons_por_tipo("eléctrico")
    if electricos is not None:
        print("Cantidad de Pokémon de tipo eléctrico:", electricos)
    else:
        print("no se encontraron pokemones de tipos eléctrico")

    aceros = tree_by_type.contar_pokemons_por_tipo("acero")
    if aceros is not None:
        print("Cantidad de Pokemones de tipo acero:", aceros)
contartipos()

