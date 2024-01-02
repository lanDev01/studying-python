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