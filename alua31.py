lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
lista = [
    (x, y)
    for x in range(3)   # Exemplo de list comprehension com mais de um for
    for y in range(3)   
]
lista = [
    [(x, letra) for letra in 'Luiz']
    for x in range(3)
]

print(lista)
