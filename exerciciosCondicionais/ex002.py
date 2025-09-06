# Verfica se o número inteiro é igual, menor ou maior que zero

num = int(input('Informe um número inteiro: '))

# com if aninhado
if(num == 0):
    print(f'O número {num} é igual a zero!')
else:
    if(num > 0):
        print(f'o número {num} é maior que zero!')
    else:
        print(f'O número {num} é menor que zero!')

# com elif
if(num == 0):
    print(f'O número {num} é igual a zero!')
elif(num > 0):
    print(f'o número {num} é maior que zero!')
else:
    print(f'O número {num} é menor que zero!')