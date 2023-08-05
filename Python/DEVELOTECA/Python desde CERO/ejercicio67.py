# Uso de tuplas
# la diferencia entre Listas y Tuplas, en tuplas no se puede modificar y se define con "()"


marcasCarros=["Ford","Mazda"] # Lista, se puede manipular dinamicamente
marcasCarrosTupla= ("Ford","Mazda") # Tuplas, no son modificables pero si se pueden unir dos tuplas

marcasCarros.append("BMW")
# marcasCarrosTupla.append("BMW") ## Da error
print(marcasCarros)
print(marcasCarrosTupla)


