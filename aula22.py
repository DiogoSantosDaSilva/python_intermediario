# Operadores úteis:
# união | união (union) - une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s1 - s2
s3 = s2 - s1
s3 = s2 ^ s1
print(s3)