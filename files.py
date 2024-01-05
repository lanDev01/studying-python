# file = open("vendas.txt", "r") # abrir o arquivo

# file.close() # fechar o arquivo

with open("vendas.txt", "r") as file:
    info = file.readlines()

vendasTotais = 0
for item in info:
    item = item.replace("\n", "")
    item = item.replace(" ", "")
    result = item.split(",")
    value = result[1]
    value = float(value)
    vendasTotais = vendasTotais + value
    print(value)
print(vendasTotais)