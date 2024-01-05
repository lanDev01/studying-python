produtos = ["iphone", "ipad", "airpod", "monitor"]

while True:    
    # Pegando o input já com letra minuscula
    product = input("Digite um produto ").lower()

    if "sair" == product:
        break

    # Verificando se há o item na lista
    if(product in produtos):
        print("Produto já cadastrado")
    else:
        print(f"Produto {product} cadastrado com sucesso")
        produtos.append(product)
    
print(produtos)