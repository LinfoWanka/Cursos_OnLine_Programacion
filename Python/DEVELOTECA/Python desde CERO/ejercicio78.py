# Borrando elementos de Diccionarios

nombres={"Oscar","Josue","Marisa","Pedro"}
print(nombres) #// {'Oscar', 'Marisa', 'Josue', 'Pedro'}
nombres.remove("Pedro")
print(nombres) #// {'Oscar', 'Marisa', 'Josue'}

nombres.pop() # borra 1 elemento, no necesariamente el ultimo*
print(nombres) #// {'Oscar', 'Josue'}

nombres.clear()
print(nombres) #// set()