def main():
    import random

    matriz = [[random.randrange(0, 9) for _ in range(5)] for _ in range(5)]

    mostrarMatriz(matriz)
    soma = somarMatriz(matriz)
    maior = maiorValor(matriz)
    print(f"\nSoma dos elementos da matriz: {soma}")
    print(f"Maior valor da matriz: {maior}\n")

    multiplicarPares(matriz)
    mostrarMatriz(matriz)
    
    somaMult = somarMatriz(matriz)
    maiorMulti = maiorValor(matriz)

    print(f"\nSoma dos elementos da matriz após a multiplicação dos elementos pares: {somaMult}")
    print(f"Maior valor da matriz após a multiplicação dos elementos pares: {maiorMulti}\n")

def somarMatriz(matriz):
    soma = 0
    for linha in matriz:
        for n in linha:
            soma += n
    
    return soma

def mostrarMatriz(matriz):
    for linha in matriz:
        for n in linha:
            print(n, end=" ")
        print()

def multiplicarPares(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] % 2 == 0:
                matriz[i][j] *= 3


def maiorValor(matriz):
    maior = matriz[0][0]

    for linha in matriz:
        for n in linha:
            if maior < n:
                maior = n
    
    return maior

main()