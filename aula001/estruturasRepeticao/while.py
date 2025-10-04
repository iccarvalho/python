# Contando com while

a = int(input('Informe o valor A: '))
b = int(input('Informe o valor B: '))

while a <= b:
    print(a)
    a = a + 1

print('Fim do programa')

# Média

media = 0
i = 0
qtdeNum = int(input('Quer calcular a média de quantos números? '))
while (i < qtdeNum):
    num = int(input(f'Informe o {i+1}º número: '))
    media += num
    i = i + 1
media = media / qtdeNum
print(f'A média dos números informados é {media}')