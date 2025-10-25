# Tuplas

aluno = ("João", 105, 6.5)

print(aluno)
print(type(aluno))

print("Acesso posicional da tupla")
print(f"Nome: {aluno[0]}")
print(f"Código: {aluno[1]}")
print(f"Nota: {aluno[2]}")

# Elementos de tuplas são imutáveis, não sendo permitido reatribuição

# aluno[0] = "Ana"  retorna erro

aluno2 = ("Ana", 106, 8)

aluno = aluno + aluno2
print(aluno)

tupla = ([1,2,3], "abc", 10.2)
tupla[0][1] = 55
print(tupla)