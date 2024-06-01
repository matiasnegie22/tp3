class Stack:

        def __init__(self):
            self.elements =[]

        def push(self,element):
            self.elements.append(element)

        def pop(self):
            if len(self.elements) > 0:
                return self.elements.pop()
            else:
                return None

        def on_top(self):
            if len(self.elements) > 0:
                return self.elements[-1]
            else:
                return None

        def size(self):
            return len(self.elements)
        

pila_personajes = Stack()
pilaaux = Stack()
Personajes=[('Iron Man',5),("Rocket Raccoon",6),('Capitan America',9),('Groot',2),('Black Widow',8)]
buscado="Black Widow"
buscado_groot = ('Groot',2)
buscado_rocket = ("Rocket Raccoon",6)

for element in Personajes:
    pila_personajes.push(element) 


def encontrar_groot(pila_personajes, buscado_groot):
    for i in range (pila_personajes.size()):
        if buscado_groot != pila_personajes.on_top():
            data=pila_personajes.pop()
            pilaaux.push(data)
        else:
            buscado_groot == pila_personajes.on_top()
            data=pila_personajes.pop()
            pilaaux.push(data)
            posicion = i
    return(posicion)

def encontrar_rocket(pila_personajes,buscado_rocket):
    for i in range (pila_personajes.size()):
        if buscado_rocket != pila_personajes.on_top():
            data=pila_personajes.pop()
            pilaaux.push(data)
        else:
            buscado_rocket == pila_personajes.on_top()
            data=pila_personajes.pop()
            pilaaux.push(data)
            posicion_2 = i
    return (posicion_2)


print(buscado_rocket, "esta en la posicion: ", encontrar_rocket(pila_personajes, buscado_rocket))
while pilaaux.size() >0:
    pila_personajes.push(pilaaux.pop())

print(buscado_groot,"esta en la posicion", encontrar_groot(pila_personajes, buscado_groot))
while pilaaux.size() >0:
    pila_personajes.push(pilaaux.pop())


while pila_personajes.size()>0:
        cuebana3=pila_personajes.on_top()[-1]
        if cuebana3<5:
            data2=pila_personajes.pop()
            pilaaux.push(data2)
        elif cuebana3>5:
            print(pila_personajes.on_top()[-2],"aparece en mas de 5 peliculas y tiene:",cuebana3,"peliculas")
            data2=pila_personajes.pop()
            pilaaux.push(data2)
        else:
            data2=pila_personajes.pop()
            pilaaux.push(data2)

while pilaaux.size() >0:
    pila_personajes.push(pilaaux.pop())


while pila_personajes.size()>0:
    peliswidow=pila_personajes.on_top()[-1]
    nombre=pila_personajes.on_top()[-2]
    if nombre == buscado:
        print(buscado,"tiene",peliswidow,"peliculas")
        data3=pila_personajes.pop()
        pilaaux.push(data3)
    else:
        data3=pila_personajes.pop()
        pilaaux.push(data3)

while pilaaux.size() >0:
    pila_personajes.push(pilaaux.pop())


while pila_personajes.size()>0:
    nombre2=pila_personajes.on_top()[-2]
    if (nombre2[:1] == "C" ):
        print("El nombre de ",nombre2,"empieza por: C")
        pila_personajes.pop()
    elif (nombre2[:1]=="D"):
        print("El nombre de ",nombre2,"empieza por: D") 
        pila_personajes.pop()
    elif (nombre2[:1]=="G"):
        print("El nombre de ",nombre2,"empieza por: G")
        pila_personajes.pop()
    else:
        pila_personajes.pop()




