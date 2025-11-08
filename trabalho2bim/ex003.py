def main():
    numeros = []
    while True:
        qtde = int(input("Quantos números quer informar? (Mín 1): "))
        if qtde >= 1:
            break
        else:
            print("Quantidade inválida! Deve informar pelo menos 1 número")
    
    for i in range(qtde):
        while True:
            num = int(input(f"Informe o {i+1}º número: "))
            if num >= 0:
                numeros.append(num)
                break
            else:
                print("São aceitos somente números positivos! Tente novamente.")
    
    print(f"Moda: {moda(numeros)}")

def moda(numeros:list):
    map = {}
    for num in numeros:
        if num in map:
            map[num] += 1
        else:
            map[num] = 1
    
    moda = max(map, key=map.get)
    maior = max(map.values())
    map.pop(moda)
    for k, v in map.items():
        if maior == v:
            return "Não existe moda!"
        
    return moda

main()