listaPrecos = [1500, 1000, 800, 2000, 300]

def calcImposto(preco, aliquota1 = 0.2, aliquota2 = 0.15, aliquota3 = 0.1):
    if preco > 2000:
        imposto = preco * aliquota1
    elif preco > 1000:
        imposto = preco * aliquota2
    else:
        imposto = preco * aliquota3
        
    print(f"Preço {preco}, Imposto: {imposto}")
    return imposto

totalImposto = 0 # acumulado

for preco in listaPrecos:
    imposto = calcImposto(preco, 0.25) # positional argument

    totalImposto = totalImposto + imposto
print(totalImposto)

def calcImposto2(preco, ir=0.275, csll=0.035, iss=0.05):
    impostoIr = preco * ir
    impostoCsll = preco * csll
    impostoIss = preco * iss
    return impostoIr, impostoCsll, impostoIss

resposta = calcImposto2(1000)
print(resposta)