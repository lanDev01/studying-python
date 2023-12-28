vendas = [100, 50, 130, 80, 120, 200]

print(vendas[0])

# Soma os valores 

totalVendas = sum(vendas)
print(totalVendas)

# Conta quantos valores tem dentro do array

quantidade = len(vendas)
print(quantidade)

# Valor Maximo e Minino

valorMax = max(vendas)
valorMin = min(vendas)

print(valorMax)
print(valorMin)

# Posição dentro do array

posicao = vendas.index(130)
print(posicao)
print(vendas[:2])

# Verifica se há o pruduto dentro do array

produtos = ["Iphone", "Ipad", "airpod"]
print("Iphone" in produtos)

# Modificando um item da lista

precos = [4000, 8000, 200]
novoPreco = precos[0] * 1.1
precos[0] = novoPreco
print(precos)

print("Iphone" in produtos)

# Adiciona um item na lista

produtos.append("MacBook")
precos.append(10000)

print(produtos)
print(precos)

# Remove um item
produtos.remove("MacBook")
precos.pop(-1)

print(produtos)
print(precos)

# Contar valores

print(produtos.count("airpod"))

# Ordenar

precos.sort(reverse=True)
print(precos)
