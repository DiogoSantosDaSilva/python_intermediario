"""
Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
Mutáveis [] {} set()
Imutáveis () "" 0 0.0 None False renge(0, 10)
"""
lista = [1, 2, 3]
dicionario = {'nome': 'Diogo'}
conjunto = set('Jesus')
tupla = ('nome', 'idade')
string = 'Deus é bom!'
inteiro = 41
flutuante = 10.5
nada = None
falso = True
intervalo = range(0, 5)

def falsy(valor):
    return 'falsy'if not valor else 'truthy'


print(f'TESTE', falsy('TESTE'))
print(f'{lista=}', falsy(lista))
print(f'{dicionario=}', falsy(dicionario))
print(f'{conjunto=}', falsy(conjunto))
print(f'{tupla=}', falsy(tupla))
print(f'{string=}', falsy(string))
print(f'{inteiro=}', falsy(inteiro))
print(f'{flutuante=}', falsy(flutuante))
print(f'{nada}', falsy(nada))
print(f'{falso}', falsy(falso))
print(f'{intervalo}', falsy(intervalo))
