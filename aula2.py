"""
Argumentos nomeados e não nomeados em função Python
Argumento nomeado temnome com sinal de igual
Argunebto não nomeado recebe apenas o argumanto (valor)
"""
def soma(x, y, z):      # Definição
    print(f'{x=}, {z=},  y={y}', '|', 'x + y + z = ', x + y + z)    


soma(1, 2, 3)
soma(1, y=2, z=5)
print(1, 2, 3, sep='-')

