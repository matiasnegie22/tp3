
#implementar una funcion que calcule la suma de todos los entero 
#entre cero y un numero psotivo dado

def sumaenteros (n)
    

    if n== 0:
        
        return n
    
    else : 
  

        return n+  sumaenteros(n-1)
    



n=int(input("ingrese un numero entero "))

print (sumaenteros(n))