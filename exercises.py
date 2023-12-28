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