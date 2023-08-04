# Uso de extends

frutasVerdes=["Manzana","Uva","Banana"]
frutasMaduras=["Fresa","Pera"]

print(frutasVerdes)

# a la lista de frutas verdes agrego las frutas maduras
frutasVerdes.extend(frutasMaduras) # 
print(frutasVerdes)

frutas=[]
frutas.extend(frutasVerdes)
frutas.extend(frutasMaduras)
print(frutas)
