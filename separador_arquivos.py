import os
import shutil
from pathlib import Path

def criar_menu_organizador_arquivo():
    print('=== Separador de arquivos! ===')
    
    # Cria os caminhos das pastas de destino
    caminho = input('Digite o caminho para organização: ').strip()
    diretorio = Path(caminho)  # Corrigido: Criar objeto Path a partir da string

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
    
    print("\nOrganização concluída!")

if __name__ == "__main__":
    criar_menu_organizador_arquivo()