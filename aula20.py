# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.oul.com.br/matematica/conjunto.html
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor inteiro.


# Criando um set
# set(iterável) ou {1, 2, 3}


# s1 = set('Luiz')
# s1 = set()  # vazio
# s1 = {'Luiz', 1, 2, 3}  # com dados



# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - eles não tem índexes;
# - eles não garantem ordem;
# - eles são iteráveis (for, in, not in)


# l1 = [1, 2, 3, 4, 4, 3, 3, 1]
# s1 = set(l1)
# print(s1)
# l2 = list(s1)
# print(l2)
 

s1 = {1, 2, 3}
# print(3 not in s1)
# for numero in s1:
#    print(numero)


# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda