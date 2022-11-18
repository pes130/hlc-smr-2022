# Para ordenar, todos los elementos de una lista deben de ser del mismo tipo
lista = [7,8,2,1,2,4,5]
print(f"Lista original: {lista}")

# Ordenar la lista
lista.sort()
# Ojo que pierdes el orden original!
print(f"Lista ordenada: {lista}")

# Para no perder el orden, usa sorted(lista)
lista = [7,8,2,1,2,4,5]
lista_ordenada = sorted(lista)
print(f"Lista: {lista}")
print(f"Lista2: {lista_ordenada}")

# Dar la vuelta a una lista: reverse
lista.reverse()
# Ojo que pierdes el orden original!
print(f"Lista revevrsa: {lista}")