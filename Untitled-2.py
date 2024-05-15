
# El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
# objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
# ayuda de la fuerza” realizar las siguientes actividades:
# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
# queden más objetos en la mochila;

# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
# car para encontrarlo;

# c. Utilizar un vector para representar la mochila.


mochila=["sable","comida","posion","papa"]

def usarlafuerza(mochila,i=0):
    if len(mochila)==0:
        return print("la mochila esta vacia")
    elif len(mochila)==i:
        return print("no se encontro el sable ")
    elif mochila[i]=="sable":
        return print("se encontro el sable de luz, la cantidad de elementos eliminados para poder encontrarlo fueron de: ",i)
    else:
        return usarlafuerza(mochila,i+1)

objetos=usarlafuerza(mochila)
    


bag=[" celular", "sable de luz","mochila propursora", "equipo de mate", "linterna"]


def busqueda (vector, buscado):

    if (len(vector) == 0): 
        return -1
    elif(buscado == vector [-1]):

        return len(vector) - 1
    else:

        print (" saco la mochila", vector[-1])

    return busqueda(vector[:-1], buscado)


busquedaObjetos= busqueda(bag, " sable de luz")

if(busquedaObjetos != -1):

    print(" se tuvieron que sacar", len(bag)-busquedaObjetos, "objetos de la mochila para econtrar el sable de luz")

else:
    print ("el sabel de luz no se econtro entre ", len(bag), "objetos lamentablemente no podra escapar")