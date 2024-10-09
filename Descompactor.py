import zipfile
import tarfile
import rarfile
import os

def descompactar_zip(arquivo, destino):
    with zipfile.ZipFile(arquivo, 'r') as zip_ref:
        zip_ref.extractall(destino)
    print(f"Arquivo {arquivo} descompactado em {destino}")

def descompactar_tar(arquivo, destino):
    with tarfile.open(arquivo, 'r') as tar_ref:
        tar_ref.extractall(destino)
    print(f"Arquivo {arquivo} descompactado em {destino}")

def descompactar_rar(arquivo, destino):
    with rarfile.RarFile(arquivo, 'r') as rar_ref:
        rar_ref.extractall(destino)
    print(f"Arquivo {arquivo} descompactado em {destino}")

def descompactar_arquivo(arquivo):
    if not os.path.exists(arquivo):
        print(f"O arquivo {arquivo} não foi encontrado.")
        return

    destino = os.path.splitext(arquivo)[0]  # Cria um diretório com o mesmo nome do arquivo

    # Cria o diretório se não existir
    os.makedirs(destino, exist_ok=True)

    ext = os.path.splitext(arquivo)[1].lower()

    if ext == '.zip':
        descompactar_zip(arquivo, destino)
    elif ext == '.tar':
        descompactar_tar(arquivo, destino)
    elif ext == '.rar':
        descompactar_rar(arquivo, destino)
    else:
        print(f"Formato de arquivo {ext} não suportado.")

if __name__ == "__main__":
    arquivo = input("Digite o caminho do arquivo que você deseja descompactar: ")
    descompactar_arquivo(arquivo)
