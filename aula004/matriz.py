# Matriz (ou lista aninhada)

matriz = [[1,2,3],[4,5,6],[7,8,9]]
print(matriz)
print(matriz[1]) # retorna [4,5,6]
print(matriz[0][2]) # retorna 3

# del remove o elemento no índice indicado

del matriz[2][0]
print(matriz)

# Imprimir matriz e somar

matriz = [[1,2,3],[4,5,6],[7,8,9]]
soma = 0
for coluna in matriz:
    for linha in coluna:
        print(linha)
        soma += linha

print(soma)
