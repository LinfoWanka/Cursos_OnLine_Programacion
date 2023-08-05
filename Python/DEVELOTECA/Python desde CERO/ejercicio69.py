# Agregar elementos a tupla

marcasCarros= ("Mazda", "Ford", "VM")
print(marcasCarros)
listaMarcasCarros=list(marcasCarros) # transformar la tupla en una lista y almacenar en la nueva variable
listaMarcasCarros.append("BMW") # agrego un nuevo elemento a la lista

marcasCarros = tuple(listaMarcasCarros) # convierto la lista en una tupla
print(marcasCarros)
