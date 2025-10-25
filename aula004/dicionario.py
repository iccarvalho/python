# Dicionários

# dicionários são compostos por chaves e valores
dicionario = {
    "nome": "Pedro",
    "código": 35,
    "nota": 7.5
}

print(dicionario)

# Acessando dicionário pela chave
print(dicionario["nome"])

# Reatribuição de valores
dicionario["nome"] = "João"
print(dicionario["nome"])

# Adicionando chaves
dicionario["disciplina"] = "programação"
print(dicionario)

# .pop retorna o valor relativo a uma chave e remove do dicionário
print(dicionario.pop("código"))

# .popitem retorna a última chave e valor como tupla e remove do dicionário
a = dicionario.popitem()
print(a)

# limpando dicionário

dicionario.clear()
print(dicionario)

# copiando dicionários

dict1 = {
    "nome": "Lucas",
    "codigo": 105
}

dict2 = dict1 # não fará uma cópia, apenas apontará para o mesmo endereço de memória
dict2["codigo"] = 333
print(dict2)
print(id(dict2))
print(dict1)
print(id(dict1))

dict2 = dict1.copy() # Fará uma cópia do dicionário a
print(dict1)
print(id(dict1))
print(dict2)
print(id(dict2))

# Acessando com .get()

dict3 = {
    "produto": "TV",
    "preco": 1000
}

#retorna o valor de uma chave ou um valor padrão se a chave não existir, mas é opcional
print(dict3.get("codigo", -1)) # retorna o valor da chave 'codigo'
print(dict3.get("numero", -1)) # retorna -1, pois a chave 'numeros' não existe

# Chaves e valores

print(dict3.keys()) # retorna as chaves do dicionário
print(dict3.values()) # retorna os valores do dicionário

