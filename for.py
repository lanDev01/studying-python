# for i in range(10):
#     print("Hello Word!")

listaPrecos = [1500, 1000, 800, 2000]
imposto = 0.1

for preco in listaPrecos:
    print(f"Preço {preco}, Imposto: {preco * imposto}")

for preco in listaPrecos:
    if preco > 1000:
        imposto = preco * 0.15
    else:
        imposto = preco * 0.1
        
    print(f"Preço {preco}, Imposto: {imposto}")



totalImposto = 0
for preco in listaPrecos:
    if preco > 1000:
        imposto = preco * 0.15
    else:
        imposto = preco * 0.1
        
    print(f"Preço {preco}, Imposto: {imposto}")
    totalImposto = totalImposto + imposto
print(totalImposto)