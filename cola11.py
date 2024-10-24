class colas:
    def __init__(self):
        self.elements= []

    def arrive(self,elements):
        self.elements.append(elements)

    def attention(self):
        if len(self.elements) >0:
            return self.elements.pop(0)
        else:
            return None
        
    def size(self):
        return len(self.elements)
    
    def on_front(self):
        if len(self.elements) >0:
            return self.elements[0]
        else:
            return None
        
    def move_to_end(self):
        element=self.attention()
        if element is not None:
            self.arrive(element)

    def insertar_antes_de(self, nuevo_nombre, nuevo_planeta, nombre_existente):
        for i, personaje in enumerate(self.elements):
            if personaje[0] == nombre_existente:  
                self.elements.insert(i, (nuevo_nombre, nuevo_planeta))
                return
        print(f"{nombre_existente} no está en la cola")

    def eliminar_despues(self,nombre_exis):
        for i, personaje in enumerate(self.elements):
            if personaje[0]== nombre_exis:
                if i+1 < len(self.elements):
                    self.elements.pop(i+1)
                    return
        print(f"{nombre_exis} no está en la cola")

# # arrive: agrega elementos al final 
# # attention: elimina el primer elemento pero lo puede devolver
# # size: me devuelve el tamaño de mi cola
# # on_front: me devuelve el valor inicial pero no lo elimina
# # move_to_end: me mueve el primer elemento de la cola al final, y el 2 pasa a ser el primero


#EJERCICIO 11
# Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta
# de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:
# a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
# b. indicar el plantea natal de Luke Skywalker y Han Solo
# c. insertar un nuevo personaje antes del maestro Yoda
# d. eliminar el personaje ubicado después de Jar Jar Binks

lacola=colas()


jedis =[
    (
        "Luke Skywalker",
        "Tatooine"
    ),
    (
        "Han Solo",    
        "Corellia"
    ),
    (
        "Anakin Skywalker/Darth Vader",
        "Tatooine"
    ),
    (
        "Quinlan Vos",   
        "Kiffu"  
    ),
    (
        "Yoda",
        None
    ),
    (
        "Mace Windu",
        "Haruun Kal"
    ),
    (
        "leia organa",
        "Alderaan"
    ),
    (
        "Jar Jar Binks",
        "Naboo"
    ),
    (   
        "Teek",
        "Endor"
    )
]

print()

for elements in jedis:
    lacola.arrive(elements)
print("la cola antes de insertar un nuevo personaje",lacola.elements)

print()

lacola.insertar_antes_de("Obi-Wan Kenobi","Stewjon","Yoda")
print("la cola despues de insertar un nuevo perosnajes",lacola.elements)

print()

lacola.eliminar_despues("Jar Jar Binks")
print("la cola despues de eliminar al personaje despues de Jar Jar Binks",lacola.elements)

print()

def mosplaneta(lacola):
    endor=[]
    alderaan=[]
    tatooine=[]
    for i in range (lacola.size()):
        if lacola.on_front()[-1] == "Endor":
            endor.append(lacola.on_front()[-2])
            lacola.move_to_end()
        elif lacola.on_front()[-1] == "Alderaan":
            alderaan.append(lacola.on_front()[-2])
            lacola.move_to_end()
        elif lacola.on_front()[-1] == "Tatooine":
            tatooine.append(lacola.on_front()[-2])
            lacola.move_to_end()
        else:
            lacola.move_to_end()
    if len(endor) > 0:
        print("los/las que pertenecen a endor son,",endor)
    if len(alderaan) > 0:
        print("los/las que pertenecen a alderaan son,",alderaan)
    if len(tatooine) > 0:
        print("los/las que pertenecen a tatooine son,",tatooine)
mosplaneta(lacola)

print()

def luke_han(lacola):
    luke=[]
    han=[]
    for i in range (lacola.size()):
        if lacola.on_front()[-2]=="Luke Skywalker":
            luke.append(lacola.on_front()[-1])    
            lacola.move_to_end()                   
        elif lacola.on_front()[-2]=="Han Solo":
            han.append(lacola.on_front()[-1])
            lacola.move_to_end()
        else:
            lacola.move_to_end()
    print("Luke Skuwalker esta en el planeta",luke)
    print("Han soloesta en el planeta",han)
luke_han(lacola)
