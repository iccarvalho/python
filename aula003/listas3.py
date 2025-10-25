# Metodos de Listas

# .append() adiciona um elemento no final da lista

num = [1,2,3,5,8,4]
num.append(15)
print(num)

# .insert(pos, elemento) adiciona um elemento no índice indicado

lista = ["a", "b", "c"]
lista.insert(1, 25)
print(lista)

# .copy() faz uma cópia da lista

a = [1,6,1,8,2]
b = a.copy()
print(b)

# .reverse() inverte a lista

num = [1,2,3,4,5]
num.reverse()
print(num)

# .sort() Ordena a lista

num = [5,1,3,6,9,7]
num.sort()
print(num) 

# .pop() remove o último elemento da lista

num = [1,2,3,4,5]
num.pop()
print(num) # remove o 5

# .remove() remove o elemento indicado

num = [1,2,3,4,5]
num.remove(3)
print(num)

# del remove o elemento no índice indicado

num = [1,2,3,4,5]
del num[3]
print(num)

