"""
Exercícios
Crie funções que duplicam, triplicam e quadruplicam
o número recebido
"""

# def  duplica(n):
#    return n * 2

# def triplica(n):
#    return n * 3

# def quadruplica(n):
#    return n * 4

# print(duplica(3))
# print(triplica(3))
# print(quadruplica(3))



def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))


    






