print('Olá, Mundo!')

# comentário

"""
comentário em bloco // docstrings
a
b
c
"""

x = 10
print('x vale', x)
type(x) # retorna 'int'

y = 5.2
print('y vale', y)
type(y) # retorna 'float'

nome = 'Igor'
print('Meu nome é', nome,)
print(f'Meu nome é {nome}')
type(nome) # retorna 'str'

num = input("Digite um número: ") # a função input sempre retorna string
print(f'Seu número é {num}\n')
type(num) # retorna 'str'

# int() converte para inteiro
# srt() converte para string
# float() converte para float
# round() arredonda a parte fracionária, mudando o tipo para int

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
print(f'{a} + {b} = {a+b}\n')

n = 22 / 7
print(f'n = {n}')
print(f'n arredondado = {round(n)}\n')

# Módulos / Bibliotecas

import math

print(math.pi)
print(math.e)
print(math.sqrt(9))
print(dir(math)) # retorna uma lista com todas as funcionalidades do módulo math