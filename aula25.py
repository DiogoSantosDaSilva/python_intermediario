# Função lambda em Python
# A função lambda é uma função como qualquer 
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de única
# expressão.
# lista = [
#       {'nome': 'Luiz', 'sobrenome': 'Miranda'},
#       {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#       {'nome': 'Daniel', 'Sobrenome': 'Silva'},
#       {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#       {'nome': 'Aline', 'sobrenome': 'Souza'},
#]
# lista = [4, 32, 1, 34, 5, 6, 6, 21,]
# lista.sort(reverse=True)
# sorted(lista)

lista = [
       {'nome': 'Luiz', 'sobrenome': 'Miranda'},
       {'nome': 'Maria', 'sobrenome': 'Oliveira'},
       {'nome': 'Daniel', 'sobrenome': 'Silva'},
       {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
       {'nome': 'Aline', 'sobrenome': 'Souza'},
]

def exibir(lista):
    for item in lista:
        print(item)
    print()




l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])



exibir(l1)
exibir(l2)
