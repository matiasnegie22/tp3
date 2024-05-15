# Desarrollar una función que permita convertir un número romano en un número decimal.

valores={ "I":1, "V":5, "X":10, "L":50, "C":100, "D":500,"M":1.000}
romano="XIV"

def decimalaromano(romano,acumulador=0):
    if (len(romano) >1):
        if valores[romano[0]]>=valores[romano[1]]:
            acumulador+=valores[romano[0]]
            return decimalaromano(romano[1:],acumulador)
        else:
            acumulador= acumulador - valores[romano[0]]
            return decimalaromano(romano[1:],acumulador)
    elif len(romano) == 1:
        return acumulador+valores[romano[0]]
    else:
        return acumulador
    

            
print(decimalaromano(romano))

