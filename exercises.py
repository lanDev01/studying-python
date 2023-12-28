# Exercícios

nome = "Alan Gonçalves"
email = "lnjnr9215@gmail.com"

# Descobrir o servidor do email

position = email.find("@")
separator = email[position:]
print(f"{separator}\n")

# pegar o 1° nome do usuário

separatorfirstName = nome.find(" ")
firstName = nome[:separatorfirstName]
print(f"{firstName}\n")

# Construir uma mensagem: Usuario {primeiro nome} cadastrado com sucesso com o {email}

print(f"Usuário {firstName} cadastrado com sucesso com o {email}\n")

# construir uma mensagem: Enviamos um link de confirmação para o email j***@gmail.com

firstLetter = email[0]

print(f"Enviamos um link de confirmação para o email {firstLetter}***{separator}\n")