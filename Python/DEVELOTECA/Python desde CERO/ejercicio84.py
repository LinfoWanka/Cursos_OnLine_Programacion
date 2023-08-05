# Aplicacion para crear listas y datos

# Crear una aplicacion que le solicite al usuario 
# una cantidad de numerosa ingresar a una lista
# Posteriormente imprimir dicha lista

print("Cuantos numeros desea ingresar?:")
cantidadNumeros=input()

contadorNumeros=0
listaNumeros=[]

# Leer los datos (cantidad de numeros solicitados)

while contadorNumeros<int(cantidadNumeros):
    print("Ingrese un numero en la posicion "+str(contadorNumeros)+": ")
    numeroIngresado=input()
    listaNumeros.append(int(numeroIngresado))
    contadorNumeros+=1
print(listaNumeros)