faturamento = 1000
custo = 700

novas_vendas = 300

faturamento = faturamento + novas_vendas # Soma
imposto = faturamento * 0.1 # multiplicar
lucro = faturamento - custo - imposto # subtrair
margem_lucro = lucro / faturamento # dividir

print(faturamento)
print(lucro)
print(margem_lucro)

restituicao = imposto * 0.1
print(restituicao)

# Mod resto da divisão
# 10 % 3
tempo_em_meses = 160
tempo_em_anos = int(tempo_em_meses / 12) # pega a parte inteira
print(tempo_em_anos, "anos")
print(tempo_em_meses % 12, "meses")

numero = 123.57
print(round(numero)) # arrendonda de acordo com a regra matemática

faturamento = 139_018_182 # o anderline facile a visualização do numero dentro do python