# Preenchendo listas

quadrados = []

for i in range(10):
    quadrados.append(i**2)

print(quadrados)

listaQuadrados = [i**2 for i in range(10)]
print(listaQuadrados)

# Sublistas por condicional

num = [1,2,3,4,5,6]

## sublista valores < 4

sublista = []
for i in num:
    if i < 4:
        sublista.append(i)

print(sublista)

sublista2 = [i for i in num if i < 4]
print(sublista2)