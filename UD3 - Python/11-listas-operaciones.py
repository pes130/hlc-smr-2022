miLista = ['Amparo', 12, 'Julio', 7.5, True]
print("Lista original: ")
print(miLista)

# Tamaño de una lista
size = len(miLista)
print(f"Tamaño: {size} o también {len(miLista)}")

# Añadir elemento a una lista
# 1. añadir elemento al final
miLista.append('Hola')
print(miLista)
# 2. Añadirlo en cualquier posición: insert(índice, elemento_a_añadir)
miLista.insert(3, 'Uranio')
print(miLista)


# Eliminar elemento de una lista
# Si sabemos el valor del elemento: remove(elemento)
miLista.remove('Julio')
print(miLista)

# Si sabemos su posición + PLUS: nos devuelve el elemento borrado!
elemento = miLista.pop(5)
print(miLista)
print(f"Elemento borrado: {elemento}")

# Si a pop no le indico nada, me devuelve el último elemento de la lista.
elemento = miLista.pop()
print(miLista)
print(f"Elemento borrado: {elemento}")

