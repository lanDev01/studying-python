faturamento = 1200 # numero inteiro -> int
custo = 770

novas_vendas = 300
faturamento = faturamento + novas_vendas

taxa_imposto = 0.1 # numero decimal -> Float

mensagem = "O faturamento foi de"  # string = texto

lucro = True # boolean

imposto = taxa_imposto * faturamento
print("Faturament", faturamento)
print("Custo", custo)
print("Lucro", faturamento - custo - imposto)
print(mensagem, faturamento)
