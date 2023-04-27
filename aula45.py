# Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece as pastas e módulos acima do __main__ por 
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

import aula45_m
from aula45_m import variavel_modulo, soma

# print('Este módulo se chama', __name__)
print(aula45_m.variavel_modulo)
print(variavel_modulo)
print(soma(2, 3))
print(aula45_m.soma(2, 3))



