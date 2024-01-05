# Exercícios
name = input("Digite seu nome ")
email = input("Digite seu E-mail ")

# Descobrir o servidor do email

position = email.find("@")
separator = email[position:]
print(f"{separator}\n")

# pegar o 1° nome do usuário

separatorfirstName = name.find(" ")
firstName = name[:separatorfirstName]
print(f"{firstName}\n")

# Construir uma mensagem: Usuario {primeiro nome} cadastrado com sucesso com o {email}

print(f"Usuário {firstName} cadastrado com sucesso com o {email}\n")

# construir uma mensagem: Enviamos um link de confirmação para o email j***@gmail.com

firstLetter = email[0]

print(f"Enviamos um link de confirmação para o email {firstLetter}***{separator}\n")

# Exercícios 2

produtos = ["iphone", "ipad", "airpod", "monitor"]
precos = [1500, 1000, 800, 2000]

# Pegando o input já com letra minuscula
product = input("Digite um produto ").lower()

# Verificando se há o item na lista
if(product in produtos):
    #Pegando o index do valor dentro do array e passando como indice dos precos para retornar o valor
    print(precos[produtos.index(product)])
else:
    # se não houver o produto ele retorna um print
    print("Produto não cadastrado")

# Exercícios 3

dictionaries = {
    "iphone": 1500,
    "ipad": 1000,
    "airpod": 800,
    "monitor": 2000
}

# Pegando o input já com letra minuscula
itemIndex = input("Digite um produto ").lower()

#Passado o
if itemIndex in dictionaries:
    itemDictionaries = dictionaries[itemIndex]
    value = dictionaries[itemIndex]
    print(f"Produto {itemIndex}, Preço: {value}")
else:
    print("Produto não cadastrado!")

# Exercícios 4
    
vendas22 = {
    "jan": 15000,
    "fev": 15500,
    "mar": 14000,
    "abr": 16600,
    "mai": 16300,
    "jun": 17000
}

vendas23 = {
    "jan": 17000,
    "fev": 15000,
    "mar": 17500,
    "abr": 16900,
    "mai": 16000,
    "jun": 18500
}

for month in vendas22:
    print(f"Mês {month}: {(vendas23[month] / vendas22[month] - 1):.1%} \n")


total = 0
for month in vendas22:
    value22 = vendas22[month]
    value23 = vendas23[month]
    if value23 < value22:
        total = total + value22
    else: 
        total = total + value23
    print(f"Mês {month}: {(vendas23[month] / vendas22[month] - 1):.1%} \n")
print(f"{total}\n")

# Exercícios 5

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