import os
import shutil
from pathlib import Path

from send2trash import send2trash

def criar_menu_organizador_arquivo():
    print('=== Separador de arquivos! ===')
    
    # Cria os caminhos das pastas de destino
    caminho = input('Digite o caminho para organização: ').strip()
    diretorio = Path(caminho) 

    if not diretorio.is_dir():
        print('Caminho não encontrado')
        return

    print("\nDigite as extensões de arquivo a serem organizados (separados por vírgula)")
    print("Exemplo: pdf, docx, jpg")
    extensoes = input("Extensões: ").strip().lower().split(',')
    extensoes = [ext.strip() for ext in extensoes if ext.strip()]  

    # O usuário informa as extensões de arquivo que ele quer que sejam separados 
    organizar_arquivos(diretorio, extensoes)

def organizar_arquivos(diretorio, extensoes):
    for ext in extensoes:
        pasta = diretorio / ext.upper()
        pasta.mkdir(exist_ok=True)
    
    # Mover os arquivos para as pastas correspondentes
    for item in diretorio.iterdir():
        if item.is_file():
            ext = item.suffix[1:].lower()  # Remove o ponto e converte para minúsculo
            if ext in extensoes:
                destino = diretorio / ext.upper() / item.name
                try:
                    shutil.move(str(item), str(destino))
                    print(f"Movido: {item.name} -> {ext.upper()}/")
                except Exception as e:
                    print(f"Erro ao mover {item.name}: {e}")
    # INSERT_YOUR_CODE
    # Identificar arquivos repetidos e movê-los para a lixeira
    arquivos_nomes = {}
    for item in diretorio.iterdir():
        if item.is_file():
            nome = item.name
            if nome in arquivos_nomes:
                arquivos_nomes[nome].append(item)
            else:
                arquivos_nomes[nome] = [item]

    repetidos = [lista for lista in arquivos_nomes.values() if len(lista) > 1]
    if repetidos:
        print("\nArquivos repetidos encontrados, movendo para a lixeira:")
        for lista in repetidos:
            # Mantém só o mais recente, envia os outros para a lixeira
            lista_ordenada = sorted(lista, key=lambda x: x.stat().st_mtime, reverse=True)
            for arquivo in lista_ordenada[1:]:
                try:
                    send2trash(str(arquivo))
                    print(f"Movido para lixeira: {arquivo.name}")
                except Exception as e:
                    print(f"Erro ao mover {arquivo.name} para a lixeira: {e}")
    
    print("\nOrganização concluída!")

if __name__ == "__main__":
    criar_menu_organizador_arquivo()