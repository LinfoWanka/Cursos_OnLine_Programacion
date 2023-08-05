# Empezando con las funciones
# una funcion es una rutina que podemos llamar en cualquier momento

'''
### este es una programacion secuencial
# dos rutinas que son practica lo mismo
a=3
b=4
c=a+b+4
print("El resutado es: "+str(c)) #// 11

d=4
e=5
f=d+e+4
print("El resutado es: "+str(f)) #// 13

'''

# creamos una funcion
def suma(a,b):
    c=a+b+4
    print("El resutado es: "+str(c))

# Llamar a una funcion para hacer rutina 1
suma(3,4) #// El resutado es: 11
# Llamar a una funcion para hacer rutina 2
suma(4,5) #// El resutado es: 13

