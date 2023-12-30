faturamento = 1000
custo = 800

lucro = faturamento - custo

if (lucro > 0):
    print(lucro)
else:
    print("Prejuízo!" , lucro)

produtos = ["iphone", "ipad", "airpod"]
novo_produto = input("Digite aqui o produto ")
novo_produto = novo_produto.lower()

if novo_produto in produtos:
    print("Produto já cadastrado")
else:
    print("Produto cadastrado com sucesso")
    produtos.append(novo_produto)

print(produtos)

vendas = 10000

if vendas > 15000:
    bonus = 500
elif vendas > 10000:
    bonus = 150
elif vendas > 5000:
    bonus = 50
else: 
    bonus = 0

print("Bonus", bonus)

if vendas > 5000:
    if vendas > 10000:
        bonus = 150
    else:
        bonus = 50
else:
    bonus = 0

print("Bonus", bonus)