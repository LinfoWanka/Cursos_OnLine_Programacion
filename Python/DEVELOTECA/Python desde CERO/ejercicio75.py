# Agregar datos a Diccionarios

frutas={"Manzana","Pera","Uva"}
print(frutas) #// {'Manzana', 'Pera', 'Uva'}
frutas.add("Piña") # con la instruccion podemos agregar varios elementos (no lo agrega necesariamente en orden o al ultimo)
print(frutas) #// {'Manzana', 'Pera', 'Uva', 'Piña'}

print("Escriba una fruta:")
nuevaFruta=input()
frutas.add(nuevaFruta)
print("Esta es la coleccion de frutas que Ud tiene:")
print(frutas) #// {'Manzana', 'Pera', 'Uva', 'Fresa', 'Piña'}

