produtos = ["iphone", "ipad", "airpod", "monitor"]
precos = [1500, 1000, 800, 2000]

# dicionários
dictionaries = {
    "iphone": 1500,
    "ipad": 1000,
    "airpod": 800,
    "monitor": 2000
}

# Pegar um item no dicionários

dictionariesData = dictionaries["iphone"]
print(f"{dictionariesData}\n")

# Mudar o valor de um item

dictionaries["iphone"] = 2000
print(f"{dictionaries}\n")

# Incluir um novo item se ele não tiver

dictionaries["celular"] = 4500
print(f"{dictionaries}\n")

# Como deletar

dictionaries.pop("iphone")
print(f"{dictionaries}\n")

# Pegando o tamanho do dicionario

print(len(dictionaries))

# Verificando os valores

print(dictionaries.keys())
print(dictionaries.values())
print(1500 in dictionaries.values())