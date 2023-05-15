lista = ["João", 30, "Cohab"]
pessoa = {
    "Nome":"Maria",
    "idade": 24,
    "Bairro":"Renascença"
}#criado dicionario

print(lista[0],"\n")

# Exibindo as chaves utilizando o comando keys()
print(pessoa.keys())

# Exibindo os valores utilizando o comando values()
print(pessoa.values())

# Exibindo tanto a chave como valor utilizando o comando items()
print(pessoa.items())

#OBS: o items() é o padrão caso eu não diga como quero mostrar 
print(pessoa)

# Exibindo o dicionário mais detalhado
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")