# Usando el while con el else

# Realiza una aplicacio que le pida al usuario una cantidad determinada de numeros
# muestre al usuario todos los numeros impares que existen en la longitud proporcionada

print("Proporcione la logitud de numeros a evaluar")

cantidad = int(input())

numero=1

print("Los siguientes numeros son impares")
while numero<cantidad:
    if(numero%2!=0):
        print(numero)
    numero+=1