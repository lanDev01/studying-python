# Quando uma função devolve mais de uma resposta ela devolve uma tupla python

# Uma tupla é uma lista de resposta

# A tupla devolve a resposta entre parenteses e ela é -> imutável (ou seja ela não suporta edições)

def calcImposto2(preco, ir=0.275, csll=0.035, iss=0.05):
    impostoIr = preco * ir
    impostoCsll = preco * csll
    impostoIss = preco * iss
    return impostoIr, impostoCsll, impostoIss

ir, csll, iss = calcImposto2(1000) # unpacking
print(ir, csll, iss, sep="\n")



vendas = {
    "André": [1000, 500, 300, 5000, 1500, 80, 3000],
    "Andressa": [1500, 9000, 300, 150, 1500, 120, 130, 55, 500, 8500],
    "Alan": [800, 100],
    "Ana": [800, 900, 950, 1200, 1600, 130, 50, 50, 50, 65, 60, 70, 70, 70, 200, 180,]
}

def calcVendas(listaVendas):
    qtde = len(listaVendas)
    bonus1 = qtde * 2
    valorTotal = sum(listaVendas)
    bonus2 = 0.01 * valorTotal
    bonus = bonus1 + bonus2

    return bonus

bonusTotal = 0
for vendedor in vendas:
    listaVendas = vendas[vendedor]
    bonus = calcVendas(listaVendas)
    print(f"Vendedor: {vendedor}, Bonus: {bonus} \n")
    bonusTotal = bonusTotal + bonus

print(vendas.items(), "\n") # transforma o dicionario em uma lista de tuplas
# ou seja você pode fazer o unpaking dessa tupla

for vendendor, listaVendas in vendas.items():
    print(vendedor)
    print(listaVendas)