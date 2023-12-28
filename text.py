email = "lnjnr9215@gmail.com"

faturamento = 1000
custo = 700

lucro = faturamento - custo

# print(f"Faturamento: { faturamento }, custo: { custo }, lucro: { lucro }")
# print("faturamento: " + str(faturamento) + ", custo: " + str(custo) + ", lucro: " + str(lucro))

# print(email.lower())
# print(email.find("@"))



posicao = email.find("@")
servidor = email[posicao + 1 :]
print(servidor)
nome_email = email[:posicao]
print(nome_email)

# tamanho de um texto

tamanho = len(email)
print(tamanho)

# Trocar um pedaço do texto
email_trocado = email.replace("gmail.com", "outlook.com")
print(email_trocado)

nome = "alan dev"
print(nome.capitalize()) # Alan dev
print(nome.title()) # Alan Dev

# Especiais
margem = lucro / faturamento
print(f"Faturamento: R${faturamento:,.2f}\n custo: { custo },\n lucro: { lucro }")
print(f"Margem: {margem:.0%}")