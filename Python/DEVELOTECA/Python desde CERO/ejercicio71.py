# Asignacion de datos a tuplas

marcasCarros= ("Mazda", "Ford", "BMW", "VM", "Chevrolet")
(marca1,marca2,*marca3) = marcasCarros # con el * asignamos mas valores

print(marca1) #// Mazda
print(marca2) #// Ford
print(marca3) #// [BMW', 'VM', 'Chevrolet']
