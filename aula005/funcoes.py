# Funções

def imprimirCompras():
    compras = ["Miojo", "Ovos", "Leite", "Pão"]
    print("Lista de compras:")
    for item in compras:
        print(f"Produto: {item}")

imprimirCompras()

# Valor padrão em funções

def reajuste(salario, juros = 0.25): # juros recebe um valor padrão que será utilizado se não for informado um valor para o parâmetro
    return salario + salario * juros

print(f"Reajuste 1: {reajuste(1000)}") # não é informado um valor para o parâmetro juros, então ele assumirá o seu valor padrão de 0.25
print(f"Reajuste 1: {reajuste(1000, 0.5)}")

def maior(x, y):
    if x > y:
        return x
        print("aaaaaaaaa")
    else:
        return y
        print("bbbbbbbbb")
# return interrompe o bloco, não irá executar o restante
    
num1 = int(input("Digitte o valor de x: "))
num2 = int(input("Digitte o valor de y: "))

maiorNum = maior(num1, num2)
print(f"O maior valor é {maiorNum}")

def valor():
    print(f"Valor de x: {x}")
    y = x * 2 # variavel local da função

x = 10

print(f"Antes da função {x}")

valor()
