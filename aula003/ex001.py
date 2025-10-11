"""
Solicite ao usuário informar a quantidade e o valor de 5 produtos, e:
a) mostre a quantidade, valor e total;
b) qual a quantidade do produto de maior valor;
c) Calcule a soma do total de cada produto.
"""

qtdeProduto = []
valorProduto = []
total = []

for i in range(5):
    valorProduto.append(int(input(f"Informe o valor do {i+1}º produto: ")))
    qtdeProduto.append(int(input(f"Informe a quantidade do {i+1}º produto: ")))
    total.append(valorProduto[i] * qtdeProduto[i])

qtdeMaiorValor = 0
maior = valorProduto[0]

for i in range(len(valorProduto)):
    if(maior < valorProduto[i]):
        qtdeMaiorValor = qtdeProduto[i]

somaTotal = 0

for i in range(5):
    somaTotal += valorProduto[i] * qtdeProduto[i]

for i in range(5):
    print(f"\nValor: R${valorProduto[i]} | Qtde: {qtdeProduto[i]} | Total: {total[i]}")

print(f"\nQuantidade do produto de maior valor: {qtdeMaiorValor}")
print(f"\nSoma total de cada produto: R${somaTotal}")
