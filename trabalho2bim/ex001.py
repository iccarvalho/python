valorCompra = float(input("Informe o valor da compra: R$"))
idade = int(input("Informe sua idade: "))

descontoBase = 0

if valorCompra > 200 and valorCompra <= 500:
    descontoBase = valorCompra * 0.10
elif valorCompra > 500:
    descontoBase = valorCompra * 0.15

descontoAdicional = valorCompra * 0.05 if idade < 25 else 0

descontoAdicional = valorCompra * 0.07 if idade >= 60 else 0

valorFinal = valorCompra - descontoBase - descontoAdicional

print(f"\nValor da compra: R${valorCompra:.2f}")
print(f"    Desc. base: - R${descontoBase:.2f}")
print(f"    Desc. adicional: - R${descontoAdicional:.2f}")
print(f"Valor final a ser pago: R${valorFinal:.2f}")

