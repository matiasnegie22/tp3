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



# Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se cono-
# ce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino
# F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-
# manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.

# # arrive: agrega elementos al final 
# # attention: elimina el primer elemento pero lo puede devolver
# # size: me devuelve el tamaño de mi cola
# # on_front: me devuelve el valor inicial pero no lo elimina
# # move_to_end: me mueve el primer elemento de la cola al final, y el 2 pasa a ser el primero

cola_personajes=colas()

colapj=[{"nombre":"Tony Stark","personaje":"Iron Man","sexo":"M"},
{"nombre":"Steve Rogers","personaje":"Capitán América","sexo":"M"},
{"nombre":"Natasha Ro-manoff","personaje":"Black Widow","sexo":"F"},
{"nombre":"Carol Danvers","personaje":"Capitana Marvel","sexo":"F"},
{"nombre":"Scott Lang","personaje":"Ant-Man","sexo":"M"}]

for elements in colapj:
    cola_personajes.arrive(elements)

print()

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
def nombre_pj(cola_personajes):
    for i in range (cola_personajes.size()):
        if cola_personajes.on_front()["personaje"] == "Capitana Marvel":
            capi=cola_personajes.on_front()["nombre"]
            cola_personajes.move_to_end()
        if cola_personajes.on_front()["nombre"]=="Scott Lang":
            scot=cola_personajes.on_front()["personaje"]
            cola_personajes.move_to_end()
        else:
            cola_personajes.move_to_end()
    print("el nombre de capitana marvel es:",capi)
    print("el nombre del personaje de scot lang es:",scot)
nombre_pj(cola_personajes)

print()

#b. mostrar los nombres de los superhéroes femeninos;
#c. mostrar los nombres de los personajes masculinos;
def femeninos_masculinos(cola_personajes):
    feme=[]
    mascu=[]
    for i in range (cola_personajes.size()):
        if cola_personajes.on_front()["sexo"] == "F":
            feme.append(cola_personajes.on_front()["personaje"])
            cola_personajes.move_to_end()
        elif cola_personajes.on_front()["sexo"] == "M":
            mascu.append(cola_personajes.on_front()["nombre"])
            cola_personajes.move_to_end()
        else:
            cola_personajes.move_to_end()
    if len(feme) >= 1:
        print("los superheroes femeninos son:",feme)
    if len(mascu) >=1:
        print("los personajes masculinos son:",mascu)
femeninos_masculinos(cola_personajes)

print()

# e. mostrar todos los datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
def let_s(cola_personajes):
    superheores_s=[]
    nombre_s=[]
    for i in range (cola_personajes.size()):
        if cola_personajes.on_front()["nombre"][0]=="S":
            nombre_s.append(cola_personajes.on_front())
            cola_personajes.move_to_end()
        elif cola_personajes.on_front()["personaje"][0]=="S":
            superheores_s.append(cola_personajes.on_front())
            cola_personajes.move_to_end()
        else:
            cola_personajes.move_to_end()
    if len(nombre_s)>=1:
        print("las personas que empiezan con S son:",nombre_s)
    else:
        print("no hay personas que empiecen con S")
    print()
    if len(superheores_s)>=1:
        print("las personas que empiezan con S son:",nombre_s)
    else:
        print("no hay superheroes que empiecen con S")
let_s(cola_personajes)

print()

# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.
def ecnontrar(cola_personajes):
    for i in range (cola_personajes.size()):
        if cola_personajes.on_front()["nombre"]=="Carol Danvers":
            carol=cola_personajes.on_front()["personaje"]
            return print("el perosnaje carol danvers se encuentra, y su superheroe es:",carol)
        else:
            cola_personajes.move_to_end()