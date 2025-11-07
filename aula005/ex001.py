"""
    Um investidor tem 3 opções de aplicações:
    
    a) CDB -> 14,5% a.a.
    b) LCA -> 11,5% a.a.
    c) Poupança  6% a.a.

    Ambos invesimentos são ppor prazo fixo, com 5, 10 ou 20 anos.
    Calcule a rentabilidade ano a ano e total.
    OBS: Para CDB há imposto de renda sobre o rendimento de 15%
"""

def main():
    investimento = float(input("Informe o valor que será investido: "))
    while(True):
        prazo = int(input("Escolha o prazo em anos [5, 10 , 20]: "))
        if prazo == 5 or prazo == 10 or prazo == 20:
            break
        else:
            print("Prazo Inválido! Tente novamente.")

    while(True):
        aplicacao = int(input("Escolha uma aplicação:\n1 - CDB\n2 - LCA\n3 - Poupança\n"))
        match aplicacao:
            case 1:
                cdb(investimento, prazo)
                break
            case 2:
                lca(investimento, prazo)
                break
            case 3:
                poupanca(investimento, prazo)
                break
            case _:
                print("Aplicação inválida!")

def cdb(valor, prazo, juros = 0.145, IR = 0.85):
    rendimentos = []
    for _ in range(1, prazo+1):
        valor += (valor * juros) * IR
        rendimentos.append(valor)

    for i, rendimento in enumerate(rendimentos, start=1):
        print(f"Ano {i}: R$ {rendimento:.2f}")


def lca(valor, prazo, juros = 0.115):
    rendimentos = []
    for _ in range(1, prazo+1):
        valor += valor * juros
        rendimentos.append(valor)
    
    for i, rendimento in enumerate(rendimentos, start=1):
        print(f"Ano {i}: R$ {rendimento:.2f}")


def poupanca(valor, prazo, juros = 0.06):
    rendimentos = []
    for _ in range(1, prazo+1):
        valor += valor * juros
        rendimentos.append(valor)
    
    for i, rendimento in enumerate(rendimentos, start=1):
        print(f"Ano {i}: R$ {rendimento:.2f}")

main()