# Funciones de argumentos variables

def algoritmo(*valores): #// al poner *valores podemos manipular "n" datos
    a=valores[0]
    b=valores[1]
    c=valores[2]
    d=a+b+c
    print("La suma del numero es: " + str(d))

algoritmo(2,5,10)



