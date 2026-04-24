from pathlib import Path  # Importa Path para trabalhar com caminhos de forma mais moderna e legivel.
from PIL import Image  # Importa Image para abrir as imagens que serao lidas pelo OCR.
import pytesseract  # Importa pytesseract para extrair o texto das imagens.


PASTA_IMAGENS = Path("pytesseract/imagens_entrada")  # Define a pasta onde o usuario deve colocar as imagens para processar.
PASTA_SAIDA = Path("pytesseract/textos_saida")  # Define a pasta onde os arquivos de texto gerados serao salvos.
EXTENSOES_VALIDAS = {".png", ".jpg", ".jpeg"}  # Define as extensoes de imagem aceitas pelo script.


def configurar_ambiente() -> None:
    # Ajusta o caminho do Tesseract e cria as pastas minimas do fluxo.
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Informa explicitamente onde esta o executavel do Tesseract.
    PASTA_IMAGENS.mkdir(parents=True, exist_ok=True)  # Cria a pasta de imagens se ela ainda nao existir.
    PASTA_SAIDA.mkdir(parents=True, exist_ok=True)  # Cria a pasta de textos se ela ainda nao existir.


def extrair_texto_da_imagem(caminho_imagem: Path) -> str:
    # Abre uma imagem, executa OCR e devolve o texto reconhecido.
    imagem = Image.open(caminho_imagem)  # Abre a imagem informada no disco.
    texto = pytesseract.image_to_string(imagem, lang="por")  # Extrai o texto da imagem usando o idioma portugues.
    return texto  # Devolve o texto para quem chamou a funcao.


def salvar_texto(caminho_imagem: Path, texto: str) -> None:
    # Salva em .txt o texto extraido da imagem atual.
    nome_saida = caminho_imagem.stem + ".txt"  # Pega o nome do arquivo sem extensao e troca a extensao para .txt.
    caminho_saida = PASTA_SAIDA / nome_saida  # Monta o caminho completo do arquivo de saida.
    caminho_saida.write_text(texto, encoding="utf-8")  # Grava o texto extraido em um arquivo de texto.


def processar_imagens() -> None:
    # Percorre a pasta de entrada e executa OCR em cada imagem valida.
    for caminho in PASTA_IMAGENS.iterdir():  # Visita cada item existente dentro da pasta de imagens.
        if caminho.suffix.lower() not in EXTENSOES_VALIDAS:  # Ignora arquivos cuja extensao nao esteja na lista permitida.
            continue  # Pula para o proximo item sem tentar processar um formato invalido.

        texto_extraido = extrair_texto_da_imagem(caminho)  # Executa OCR na imagem atual.
        salvar_texto(caminho, texto_extraido)  # Salva o texto extraido em um arquivo .txt correspondente.
        print(f"OCR concluido para: {caminho.name}")  # Mostra no console qual arquivo foi processado.


def main() -> None:
    # Executa o fluxo principal do script.
    configurar_ambiente()  # Prepara as pastas e o caminho do executavel antes do processamento.
    processar_imagens()  # Inicia o processamento em lote das imagens encontradas.


if __name__ == "__main__":  # Garante que o bloco abaixo so rode quando este arquivo for executado diretamente.
    main()  # Chama a funcao principal para iniciar o fluxo completo do script.
