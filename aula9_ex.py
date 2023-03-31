# Exercícios com funções    

# Crie um função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# Crie uma função fala se um número é par ou impar.
# Retorne se o número é ou impar.


"""
1º exercício 

def multiplica(*args):
    total_m = 1
    for valor in args:
        total_m = total_m * valor
        return total_m


print('O valor de todos os números multiplicados é {} '.format(multiplica(1, 2, 3, 4, 5)))
print(f'O valor total é {multiplica(20, 10, 40, 50)}')
print('O Multiplo é {}'.format(multiplica(123, 123, 45, 56)))

"""



def par_ou_impar(a):
    if a % 2 == 0:
        return f'O número {a} é PAR'
    return f'O número {a} é IMPAR'
    
print(par_ou_impar(2))
print(par_ou_impar(3))
print(par_ou_impar(15))
print(par_ou_impar(16))

