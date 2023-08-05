# Uniendo los Diccionarios

frutasVerdes={"Manzana","Pera"}
frutasMaduras={"Piña","Uva"}
frutasMaduras.update(frutasVerdes) # Unimos diccionarios

print(frutasMaduras) #// {'Piña', 'Pera', 'Manzana', 'Uva'}
