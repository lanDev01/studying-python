# Bibliotecas
import os # lib Os

fileList = os.listdir("files") # Ela lista tudo que está no diretorio
print(fileList)

for file in fileList:
    if "txt" in file:
        if "22" in file:
            os.rename(f"files/{file}", f"files/22/{file}")
        elif "23" in file:
            os.rename(f"files/{file}", f"files/23/{file}")
