import os
import shutil
from tqdm import tqdm


pasta_destino = r"caminho para a pasta de destino"
origem = r"caminho para a pasta de origem"
pastas_origem = []  # será uma lista de pastas
cont = 0

for item in os.listdir(origem):
    if os.path.isdir(fr"{origem}\{item}"):
        pastas_origem.append(item)

print("\n\nPastas de origem:")
print(pastas_origem)
print(f"\nQuantidade de locais listados: {len(pastas_origem)} diretórios.")
print("\n")

for pasta in pastas_origem:
    arquivos = fr"{origem}\{pasta}"
    print(f"\nArquivos da pasta {pasta}:")
    print(os.listdir(arquivos))
    for arq in os.listdir(arquivos):
        cont += 1
        if "jpg" in arq or "JPG" in arq:
            nome = "img" + str(cont) + ".jpg"
            shutil.copy(fr"{arquivos}\{arq}", fr"{pasta_destino}\{nome}")
        elif "png" in arq or "PNG" in arq:
            nome = "img" + str(cont) + ".png"
            shutil.copy(fr"{arquivos}\{arq}", fr"{pasta_destino}\{nome}")

print("\n\nArqivos da pasta de destino:\n")
print(os.listdir(pasta_destino))
print("\n\nRELATÓRIO DE MOVIMENTAÇÃO DE ARQUIVOS\n\n")
print(f"\nQuantidade de locais listados: {len(pastas_origem)} diretórios.")
print(f"Total de arquivos pesquisados: {cont}")
print(f"Total de arquivos copiados {len(os.listdir(pasta_destino))}\n")
