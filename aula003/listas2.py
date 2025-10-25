# Sub-Listas

valores = [1, 3, 4, 5, 6, 7, 8, 20]
print(valores)

subLista1 = valores[1:5] # Cria uma sub-lista com os valores dos índices 1 até 5
print(subLista1)

subLista2 = valores[4:] # Cria uma sub-lista com os valores do índice informado até o final
print(subLista2)

subLista3 = valores[:4] # Cria uma sub-lista com os valores do início até o índice informado
print(subLista3)

subLista4 = valores[1:7:2] # Cria uma sub-lista com os valores dos índices 1 até 7, pulando 2 índices
print(subLista4)

# Unpacking

x = [3, 5, 7]
print(x)

a, b, c = x # atribui os valores dos índices 0, 1 e 2 as variáveis a, b e c respectivamente
print(a) # retorna 3
print(b) # retorna 5
print(c) # retorna 7

# Agrupando listas

num1 = [1, 2, 3]
num2 = [4, 5, 6]

num3 = num1 + num2 # agrupa as duas listas em uma só
print(num3)

num4 = num1 * 3 # repete a lista a 3 vezes e agrupa numa nova lista
print(num4)

# Removendo elementos

del num3[3] # remove o elemento na posição indicada
print(num3)

num3.remove(1) # remove o elemento no índice 3
print(num3)

# Copiando listas

lista1 = [1, 3, 5]
print(lista1)

lista2 = lista1 # lista2 aponta para a mesma referência da lista1


lista1.append(8)
print(lista1)
print(lista2)

# Endereços de memória

print(id(lista1))
print(id(lista2))

lista3 = lista1[:] # copia a lista1
print(lista3)
# lista3 = lista1.copy() também faz uma cópia da lista
print(id(lista3)) # retorna endereço diferente da lista1, portanto não está apontando para a mesma referência

# Procurando elementos numa lista

numero = 3

if numero in lista1:
    print("encontrei!")
else:
    print("não está na lista :(")

