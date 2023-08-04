# Aplicacion IMC

# Crear una aplicacion para calcular el IMC (Indice de Masa Corporal)
# IMC = peso / (altura)*(altura)

print("Proporcione el peso:")
peso=input()
print("Proporcione el valor de la altura:")
altura=input()

imc = int(peso)/((float(altura)) * (float(altura)))

print("Su IMC es :",imc)


