"""
Crie um programa que dado valor n exiba sua tabuada
"""

n = int(input("Informe um número para saber sua tabuada: "))
limite = int(input("Informe até onde quer a tabuada: "))

for x in range(0, limite+1):
    print(f"{n} x {x} = {n*x}")