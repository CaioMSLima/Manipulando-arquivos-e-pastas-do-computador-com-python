from pathlib import Path
import shutil

estados = ['RJ', 'SP', 'MG', 'GO', 'AM']
for estado in estados:
    Path('Arquivos_Lojas/{}'.format(estado)).mkdir()

caminho = Path('Arquivos_Lojas/')
arquivos = caminho.iterdir()
for arquivo in arquivos:
    nome_arquivo = arquivo.name
    if nome_arquivo[-3:] == 'csv':
        estado = nome_arquivo[-6:-4]
        local_final = caminho / Path('{}/{}'.format(estado, nome_arquivo))
        shutil.move(arquivo, local_final)
