# Listas

frutas = ["Maçã", "banana", "Morango"] # atribuíção manual

print(frutas) # retorna a lista completa

print(frutas[2]) # retorna a lista no índice 2 "Morango"

print(len(frutas)) # len() retorna o tamanho da lista

frutas = [] # limpa a lista

print(frutas) # retorna []

x = list(range(5)) # list() preenche uma varíavel com uma lista, neste caso irá preencher com os números de 0 a 4

print(x)

lista = ["Uva", True, 26] # é possível atribuir a uma lista vários tipos de informação (ex: string, boolean, number etc)

print(type(lista)) # retorna "<class 'list'>"


# Percorrendo listas

## Somar elementos

num = [2.3, 5.5, 1, 17, 9, 3]
soma = 0

for n in num: # percorre/itera a lista inteira, sem ter a necessidade de informar seu tamanho
    soma += n

print(soma)

## Lista posicional

alunos = ["Igor", "Cauê", "Lucca", "Miguel"]

for n in range(len(alunos)): # percorre a lista com base no seu tamanho, posicional
    print(f"Posição {n} da lista: {alunos[n]}")

# Atribuição pelo usuário

qtdeAl = 5
notas = []

for i in range(qtdeAl):
    x = int(input(f"Informe a nota do {i+1}º aluno: "))
    notas.append(x) # adiciona o valor no final da lista

print(notas)

media = 0

for n1 in notas:
    media += n1

media /= qtdeAl

for n1 in notas:
    if n1 > media:
        print(f"{n1} | Aprovado")
    else:
        print(f"{n1} | Reprovado")
