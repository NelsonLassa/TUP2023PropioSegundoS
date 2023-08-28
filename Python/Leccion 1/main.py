# lista = Nelson, Mariano, Valentin, Jose
nombres = ["Nelson", "Mariano", "Valentin", "Jose"]

print(nombres)  # imrpimira lista completa
"""
print(nombres[0]) imprimira solo el primer conjunto
print(nombres[1])
print(nombres[3])
print(nombres[-1])
print(nombres[-2])
"""
print(nombres[0:2])  # el intervalo a mostrar es del 0 al 2 pero no incluye el 2
print(nombres[:3])  # muestra del inicio sin incluir el valor 3
print(nombres[1:])  # muestra del valor 1 hasta el ultimo

#Modificamos un valor

nombres[3]= "Papá"
print(nombres)

#Iterar una lista
for nombre in nombres: # nombre es singular, la lista esta en plurarl
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")

# Preguntamos cuantos elementos tiene la lista
print(len(nombres)) # pasamos como parametro la lista

# Agregamos un elemento
nombres.append("Sofi")
print(nombres)

# Agregamos un elemento en un indice especifico
nombres.insert(4, "Daniela")
print(nombres)
nombres.insert(3, "Ezequiel")
print(nombres)

# Eliminamos un elemento
nombres.remove("Ezequiel")
print(nombres)

# Eliminar el ultimo elemnto
nombres.pop()
print(nombres)

# Eliminar un indice especifico
del nombres[1] # del significa delete (eliminar)
print(nombres)

# Eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres) # borra el contenido

# Eliminar lista
del nombres
print(nombres) # este borra la variable nombre