# Format con strig (indices)

cantidad=3
numeroControl=10
precio=59.90

PrecioDeVenta="El producto vale {2} y son cantidad {0} productos el numero de control es {1} " # indicamos el indice que ira con el print

print(PrecioDeVenta.format(cantidad,numeroControl,precio))  # porque si no indicamos el indice andra en ese oren el print

