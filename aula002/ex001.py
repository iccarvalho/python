"""
Crie um programa que controle vendas e solicite ao usuário: 
    -nome do produto
    -valor
    -quantidade
    -método de pagamento (1 - a vista, 2 - a prazo)

Se a prazo solicite o nº de parcelas e, calcule o total:
- a vista => desconto de 10%
- a prazo => acréscimo de:
    - 15% até 5 parcelas
    - 20% acima de 5 parcelas

Calcule e mostre o total da venda, desconto e líquido a pagar;
Se a prazo, mostre o valor de cada parcela, e o adicional.
"""

nomeProduto = str(input("Informe o nome do produto: "))
valor = float(input("Informe o valor do produto: "))
qtde = int(input("Informe a quantidade do produto: "))
metodoPag = int(input("Informe o método de pagamento: \n1 - a vista\n2 - a prazo\n"))

total = valor * qtde

match metodoPag:
    case 1:
        totalDesconto = total * 0.9
        print(f"Total da venda: R${total:.2f}")
        print(f"Desconto a vista: R${(total - totalDesconto):.2f}")
        print(f"Total líquido a pagar: R${totalDesconto:.2f}")
    case 2:
        parcelas = int(input("Informe a quantidade de parcelas: "))
        if(parcelas <= 5):
            totalAcrescimo = (total * 1.15)
        elif(parcelas > 5):
            totalAcrescimo = (total * 1.2)
        print(f"Total da venda com adicional a prazo: R${(totalAcrescimo):.2f}")
        print(f"Valor de cada parcela: R${(totalAcrescimo / parcelas):.2f}")
    case _:
        print("Método inválido")
        
