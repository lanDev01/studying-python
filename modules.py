# Bibliotecas
import os # lib Os
import requests # Lib Request

fileList = os.listdir("files") # Ela lista tudo que está no diretorio
print(fileList)

for file in fileList:
    if "txt" in file:
        if "22" in file:
            os.rename(f"files/{file}", f"files/22/{file}")
        elif "23" in file:
            os.rename(f"files/{file}", f"files/23/{file}")

link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL" # Link da API

res = requests.get(link) # Fazendo requisição a API
resJson = res.json() # transformando a resposta em Json
print(resJson) # exibindo a resposta
print(resJson["USDBRL"]) # pegando item expecifico