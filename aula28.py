# List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de interáveis.
# print(list(range(10)))
lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 2
    for numero in range(10)
]
print(lista)
