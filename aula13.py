"""
Dicionários em Python (tipo dict)
Dicionários são estruras de dados do tipo
par de "chave" e "valor".
Chaves podem ser consideradas como o "índice"
que vimos na lista e podem ser de tipos imutáves
como: str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro
dicionário.
Usamos as chaves - {} - ou classe dict para criar
dicionários.
Imutáveis: str, int, float, bool, tuple
Mutável: dict, list
passoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321}
    ]
}

pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda') -> exemplo de dict
"""
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321}
    ],
}

# print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])
print()
for chave in pessoa:
    print(chave, pessoa[chave])
    

