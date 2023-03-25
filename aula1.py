"""
Introdução as funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumantos)
e retornar um valor específico.
Por padrão, funções Python retorna None (nada).
"""

def saudacao(nome='sem nome'):
    print(f'Olá, {nome}!')


saudacao('Luiz Otávio')
saudacao('Diogo Silva')
saudacao('Isaac Francisco')
saudacao()


