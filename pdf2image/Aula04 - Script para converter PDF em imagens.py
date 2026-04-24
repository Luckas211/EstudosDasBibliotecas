from pathlib import Path  # Importa Path para montar caminhos de arquivos e pastas com clareza.
from pdf2image import convert_from_path  # Importa a funcao que converte PDF em imagens Pillow.


CAMINHO_PDF = Path("pdf2image/exemplo.pdf")  # Define o caminho do PDF que sera convertido.
PASTA_SAIDA = Path("pdf2image/paginas_convertidas")  # Define a pasta onde as imagens resultantes serao salvas.
CAMINHO_POPPLER = r"C:\poppler\Library\bin"  # Define um caminho de exemplo para os binarios do Poppler no Windows.


def converter_pdf() -> list:
    # Converte um PDF em uma lista de imagens Pillow.
    paginas = convert_from_path(  # Chama a funcao principal da biblioteca.
        CAMINHO_PDF,  # Informa qual arquivo PDF deve ser aberto.
        dpi=300,  # Define uma resolucao boa para leitura e OCR.
        poppler_path=CAMINHO_POPPLER,  # Informa onde o Poppler foi instalado no Windows.
    )  # Fecha a chamada da funcao principal.
    return paginas  # Devolve a lista de imagens para a funcao chamadora.


def salvar_paginas(paginas: list) -> None:
    # Recebe as paginas convertidas e salva cada uma como PNG.
    PASTA_SAIDA.mkdir(parents=True, exist_ok=True)  # Cria a pasta de saida caso ela ainda nao exista.

    for indice, pagina in enumerate(paginas, start=1):  # Percorre cada pagina com um contador iniciando em 1.
        caminho_saida = PASTA_SAIDA / f"pagina_{indice}.png"  # Monta o nome final do arquivo de imagem.
        pagina.save(caminho_saida, "PNG")  # Salva a pagina atual no formato PNG.
        print(f"Pagina {indice} salva em {caminho_saida}")  # Informa no console onde a imagem foi gravada.


def main() -> None:
    # Executa o fluxo principal do script.
    paginas = converter_pdf()  # Converte o PDF em imagens e guarda o resultado em memoria.
    salvar_paginas(paginas)  # Salva no disco todas as paginas convertidas.


if __name__ == "__main__":  # Garante que o codigo abaixo so rode quando este arquivo for executado diretamente.
    main()  # Inicia o fluxo completo de conversao e salvamento.
