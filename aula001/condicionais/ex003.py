nota = int(input('Informe sua nota: '))

if(nota >= 60):
    print(f'Você passou!')
elif(nota >= 30 and nota < 60):
    print(f'Você precisa fazer sub, faz o L')
else:
    print(f'Você reprovou :(')