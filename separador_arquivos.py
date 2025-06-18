import os
import shutil

def organizar_arquivo(diretorio_origem):
    
    # Cria os caminhos das pastas de destino
    
    pasta_docx = os.path.join(diretorio_origem, 'Arquivos_DOCX')
    pasta_pdf = os.path.join(diretorio_origem, 'Arquivos_PDF')
    
    # Cria as pastas se elas não existirem
    os.makedirs(pasta_docx, exist_ok=True) 
    os.makedirs(pasta_pdf, exist_ok=True)
    
    # Lista todos os arquivos no diretório de origem
    for arquivo in os.listdir(diretorio_origem):
        caminho_arquivo = os.path.join(diretorio_origem, arquivo)
        
        # Ignora diretórios (só processa arquivos)
        if os.path.isfile(caminho_arquivo):
            # Move arquivos .txt/docx/jpeg/PNG

            if arquivo.lower().endswith('.docx'):
                shutil.move(caminho_arquivo, os.path.join(pasta_docx, arquivo)) 
                print(f'Arquivo {arquivo} movido para {pasta_docx}') 
            
            # Move os arquivos em .pdf

            elif arquivo.lower().endswith('.pdf'):
                shutil.move(caminho_arquivo, os.path.join(pasta_pdf, arquivo))
                print(f'Arquivo {arquivo} movido para {pasta_pdf}')

if __name__ == '__main__':

    # Substituir pelo caminho que vai ser organizado

    diretorio = r'C:\teste_leo'
    organizar_arquivo(diretorio)
    print("Organização concluída na pasta selecionada!")
