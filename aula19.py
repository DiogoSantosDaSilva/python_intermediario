# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.oul.com.br/matematica/conjunto.html
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor inteiro.


# Criando um set
# set(iterável) ou {1, 2, 3}


# s1 = set('Luiz')
s1 = set()  # vazio
s1 = {'Luiz', 1, 2, 3}  # com dados



# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - eles não tem índexes;
# - eles não garantem ordem;
# - eles são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - une
# intersercção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
