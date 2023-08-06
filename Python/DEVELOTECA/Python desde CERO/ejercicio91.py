# Calcular el IMC

# Hacer una aplicacionpara calcular el IMC 
# y mostrarle al usuario su peso indicandole, si tiene peso bajo, normalu obesidad
# IMC  = peso / (estatura)*(estatura)
# IMC < 18.5 (peso bajo), IMC > 18.5 y < 29.9 (Normal), IMC > 29.9 (Obesidad)

def calcularIMC(peso,estatura):
    IMC = peso /(estatura*estatura)
    # print("Valor del IMC "+str(IMC))

    if IMC < 18.5:
        print("Peso bajo")
    else:
        if IMC > 18.5 and IMC < 29.9:
            print("peso normal")
        else:
            if IMC > 29.9:
                print("Obesidad")





print("Escriba su estatura (m) ") # 1.8 m
estatura=float(input())

print("Escriba su peso ") # (kg)
peso=int(input())

calcularIMC(peso,estatura)








