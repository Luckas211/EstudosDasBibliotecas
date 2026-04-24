from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parent


def lines(text: str) -> list[str]:
    cleaned = dedent(text).strip("\n")
    return [line + "\n" for line in cleaned.splitlines()]


def md(text: str) -> dict:
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": lines(text),
    }


def code(text: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": lines(text),
    }


def notebook(title: str, cells: list[dict]) -> dict:
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.12",
            },
            "title": title,
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dedent(content).strip("\n") + "\n", encoding="utf-8")


def write_notebook(path: Path, title: str, cells: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(notebook(title, cells), ensure_ascii=True, indent=2) + "\n",
        encoding="utf-8",
    )


def build_root_files() -> None:
    write_text(
        ROOT / "README.md",
        """
        # Manual das bibliotecas em Python

        Este diretorio foi organizado como uma trilha de estudos didatica para iniciantes.
        A proposta e que cada biblioteca funcione como um pequeno curso, com aulas progressivas, explicacoes em portugues simples e exemplos comentados linha por linha.

        ## Como a trilha esta organizada

        - Cada biblioteca ganhou sua propria pasta.
        - Dentro de cada pasta existe um `README.md` com a visao geral do modulo.
        - As aulas seguem o padrao `Aula01`, `Aula02`, `Aula03` e assim por diante.
        - O que puder ser estudado passo a passo foi criado em `.ipynb`.
        - O que fizer mais sentido como script executavel foi criado em `.py`.

        ## Bibliotecas estudadas

        - `os`
        - `re`
        - `pytesseract`
        - `pdf2image`

        ## Ordem sugerida

        1. `os`
        2. `re`
        3. `pdf2image`
        4. `pytesseract`

        ## Intencao pedagogica

        Os materiais foram escritos pensando em alguem leigo.
        Por isso, cada modulo tenta responder sempre estas perguntas:

        - o que esta funcao faz
        - o que este objeto representa
        - quais parametros ela recebe
        - o que ela devolve
        - quando usar
        - como variar o mesmo conceito em exemplos diferentes

        ## Antes de executar os notebooks

        Para `os` e `re`, basta ter Python instalado.

        Para `pdf2image` e `pytesseract`, alem das bibliotecas Python, voce tambem precisa instalar ferramentas externas:

        - `pdf2image` depende do Poppler no Windows
        - `pytesseract` depende do Tesseract OCR instalado no sistema

        ## Arquivo de apoio

        O arquivo `requirements-estudos.txt` reune as dependencias Python mais importantes para esta pasta de estudos.

        ## Forma recomendada de estudo

        1. Leia o `README.md` da biblioteca.
        2. Estude uma aula por vez.
        3. Execute cada bloco.
        4. Leia os comentarios de todas as linhas.
        5. Modifique os exemplos.
        6. Tente repetir sem copiar.
        7. Anote duvidas e compare uma aula com a outra.
        """,
    )

    write_text(
        ROOT / "requirements-estudos.txt",
        """
        # Pacotes uteis para executar os estudos em notebook
        jupyter

        # Imagens e OCR
        pillow
        pdf2image
        pytesseract
        """,
    )


def build_os_course() -> None:
    folder = ROOT / "os"

    write_text(
        folder / "README.md",
        """
        # Modulo: os

        O modulo `os` ajuda o Python a conversar com o sistema operacional.
        Ele e usado para descobrir onde estamos, listar arquivos, criar pastas, manipular caminhos e automatizar tarefas simples do dia a dia.

        ## O que voce vai aprender

        - descobrir a pasta atual com `os.getcwd()`
        - listar itens com `os.listdir()`
        - montar caminhos com `os.path.join()`
        - testar caminhos com `exists`, `isfile` e `isdir`
        - criar, renomear e remover itens
        - entender melhor caminhos, nomes e extensoes
        - percorrer subpastas com `os.walk()`
        - ler variaveis de ambiente com `os.environ` e `os.getenv()`

        ## Ordem sugerida

        1. `Aula01 - Introducao ao modulo os.ipynb`
        2. `Aula02 - Navegando por pastas e arquivos.ipynb`
        3. `Aula03 - Criando, renomeando e removendo.ipynb`
        4. `Aula04 - Projeto guiado - Organizador de arquivos.ipynb`
        5. `Aula05 - Trabalhando melhor com caminhos.ipynb`
        6. `Aula06 - Percorrendo subpastas com os.walk.ipynb`
        7. `Aula07 - Variaveis de ambiente e informacoes do sistema.ipynb`
        """,
    )

    write_notebook(
        folder / "Aula01 - Introducao ao modulo os.ipynb",
        "Aula01 - Introducao ao modulo os",
        [
            md(
                """
                # Aula01 - Introducao ao modulo os

                Nesta aula voce vai conhecer o papel do modulo `os`.

                O modulo `os` serve para:

                - descobrir em qual pasta o programa esta
                - listar arquivos e subpastas
                - montar caminhos de forma correta
                - acessar informacoes do sistema operacional

                Vamos comecar pelas funcoes mais usadas por iniciantes.
                """
            ),
            md(
                """
                ## Funcao: `os.getcwd()`

                `getcwd` significa **get current working directory**.

                Em portugues:
                ela devolve o caminho da pasta atual onde o Python esta executando.

                Quando isso e util:

                - quando um arquivo "nao esta sendo encontrado"
                - quando voce quer montar caminhos relativos
                - quando quer confirmar em que pasta seu notebook esta rodando
                """
            ),
            code(
                """
                import os  # Importa o modulo os, que possui funcoes ligadas ao sistema operacional.

                pasta_atual = os.getcwd()  # Chama a funcao getcwd para descobrir a pasta atual do processo Python.

                print(pasta_atual)  # Exibe o caminho encontrado para voce visualizar o diretorio atual.
                """
            ),
            md(
                """
                ## Funcao: `os.listdir()`

                `listdir` significa **list directory**.

                Ela lista os nomes dos itens dentro de uma pasta.

                Parametros:

                - sem parametro: lista a pasta atual
                - com um caminho: lista a pasta informada

                Retorno:

                - uma lista de strings
                """
            ),
            code(
                """
                import os  # Importa novamente o modulo os para manter o exemplo independente.

                itens_da_pasta_atual = os.listdir()  # Lista todos os itens da pasta atual porque nenhum caminho foi informado.

                print(itens_da_pasta_atual)  # Mostra no console a lista retornada pela funcao.
                print(type(itens_da_pasta_atual))  # Mostra o tipo do objeto para reforcar que o retorno e uma lista.
                """
            ),
            md(
                """
                ## Funcao: `os.path.join()`

                `join` serve para juntar partes de um caminho.

                Isso e importante porque:

                - Windows e Linux usam separadores diferentes
                - escrever barras "na mao" pode gerar erro
                - `join` deixa o codigo mais legivel e mais seguro
                """
            ),
            code(
                """
                import os  # Importa o modulo os para usar o submodulo path.

                nome_da_pasta = "os"  # Guarda o nome de uma pasta em uma variavel.
                nome_do_arquivo = "README.md"  # Guarda o nome de um arquivo em outra variavel.

                caminho_completo = os.path.join(nome_da_pasta, nome_do_arquivo)  # Junta as duas partes usando o separador correto do sistema.

                print(caminho_completo)  # Exibe o caminho final montado pela funcao join.
                """
            ),
            md(
                """
                ## Resumo da aula

                Hoje voce viu:

                - `os.getcwd()`
                - `os.listdir()`
                - `os.path.join()`

                ## Exercicio sugerido

                1. Descubra sua pasta atual.
                2. Liste os itens dela.
                3. Monte o caminho para um arquivo real usando `os.path.join()`.
                """
            ),
        ],
    )

    write_notebook(
        folder / "Aula02 - Navegando por pastas e arquivos.ipynb",
        "Aula02 - Navegando por pastas e arquivos",
        [
            md(
                """
                # Aula02 - Navegando por pastas e arquivos

                Agora vamos aprender a fazer perguntas sobre um caminho.

                Perguntas comuns:

                - este caminho existe?
                - ele aponta para arquivo?
                - ele aponta para pasta?
                - como percorrer varios itens de uma vez?
                """
            ),
            md(
                """
                ## Funcoes importantes desta aula

                - `os.path.exists(caminho)`
                - `os.path.isfile(caminho)`
                - `os.path.isdir(caminho)`
                - `os.listdir(caminho)`
                """
            ),
            code(
                """
                import os  # Importa o modulo os para trabalhar com caminhos.

                pasta_do_modulo = "os"  # Define o nome da pasta que queremos analisar.

                existe = os.path.exists(pasta_do_modulo)  # Verifica se o caminho informado existe.
                e_arquivo = os.path.isfile(pasta_do_modulo)  # Verifica se o caminho aponta para um arquivo.
                e_pasta = os.path.isdir(pasta_do_modulo)  # Verifica se o caminho aponta para uma pasta.

                print(existe)  # Mostra True ou False para a existencia do caminho.
                print(e_arquivo)  # Mostra True apenas se o caminho for um arquivo.
                print(e_pasta)  # Mostra True apenas se o caminho for uma pasta.
                """
            ),
            md(
                """
                ## Percorrendo uma lista de nomes

                Quando `os.listdir()` devolve uma lista, podemos percorrer a lista com `for`.
                Isso e muito usado em automacoes simples.
                """
            ),
            code(
                """
                import os  # Importa o modulo os para listar o conteudo da pasta.

                caminho_base = "os"  # Define a pasta que sera percorrida.
                itens_encontrados = os.listdir(caminho_base)  # Lista os itens existentes dentro da pasta informada.

                for item in itens_encontrados:  # Percorre cada nome retornado pela lista.
                    caminho_do_item = os.path.join(caminho_base, item)  # Monta o caminho completo do item atual.
                    print("Nome:", item)  # Mostra o nome simples do item atual.
                    print("Caminho completo:", caminho_do_item)  # Mostra o caminho completo do item atual.
                    print("E arquivo?", os.path.isfile(caminho_do_item))  # Diz se o item atual e um arquivo.
                    print("E pasta?", os.path.isdir(caminho_do_item))  # Diz se o item atual e uma pasta.
                    print("-" * 40)  # Cria uma separacao visual entre um item e outro.
                """
            ),
            md(
                """
                ## Boa pratica

                Antes de abrir, mover, renomear ou apagar algo, verifique:

                - se o caminho existe
                - se ele e arquivo ou pasta
                - se voce esta na pasta correta
                """
            ),
        ],
    )

    write_notebook(
        folder / "Aula03 - Criando, renomeando e removendo.ipynb",
        "Aula03 - Criando, renomeando e removendo",
        [
            md(
                """
                # Aula03 - Criando, renomeando e removendo

                Agora vamos sair da parte de consulta e entrar na parte de alteracao.

                Funcoes estudadas:

                - `os.mkdir()`
                - `os.makedirs()`
                - `os.rename()`
                - `os.remove()`
                - `os.rmdir()`

                Cuidado:
                remocao apaga de verdade.
                """
            ),
            code(
                """
                import os  # Importa o modulo os para criar itens no sistema de arquivos.

                pasta_principal = "os/exemplo_pratico"  # Define a pasta principal do nosso exemplo controlado.
                subpasta = os.path.join(pasta_principal, "textos")  # Monta o caminho da subpasta que sera criada.

                if not os.path.exists(subpasta):  # Verifica se a subpasta ainda nao existe para evitar erro de criacao duplicada.
                    os.makedirs(subpasta)  # Cria a subpasta e qualquer pasta intermediaria que ainda falte.

                print("Estrutura criada com sucesso.")  # Informa que a criacao terminou.
                """
            ),
            md(
                """
                ## O que cada funcao representa

                - `os.mkdir("pasta")`: cria uma pasta unica
                - `os.makedirs("a/b/c")`: cria uma cadeia de pastas
                - `os.rename(origem, destino)`: renomeia ou move
                - `os.remove(arquivo)`: apaga um arquivo
                - `os.rmdir(pasta_vazia)`: apaga uma pasta vazia
                """
            ),
            code(
                """
                import os  # Importa o modulo os para continuar o exemplo.

                pasta_base = "os/exemplo_pratico"  # Define a pasta principal onde ocorreu a criacao.
                nome_antigo = os.path.join(pasta_base, "textos")  # Monta o caminho antigo da subpasta.
                nome_novo = os.path.join(pasta_base, "documentos_texto")  # Monta o novo caminho desejado.

                if os.path.exists(nome_antigo) and not os.path.exists(nome_novo):  # Confere se a pasta antiga existe e se a nova ainda nao existe.
                    os.rename(nome_antigo, nome_novo)  # Renomeia a subpasta.

                print("Renomeacao concluida.")  # Exibe uma mensagem simples para indicar o fim da etapa.
                """
            ),
            code(
                """
                import os  # Importa o modulo os para limpar o exemplo.

                pasta_base = "os/exemplo_pratico"  # Define novamente a pasta principal do exemplo.
                pasta_final = os.path.join(pasta_base, "documentos_texto")  # Monta o caminho da subpasta ja renomeada.

                if os.path.exists(pasta_final) and os.path.isdir(pasta_final):  # Confirma que a subpasta existe e e uma pasta.
                    os.rmdir(pasta_final)  # Remove a subpasta porque ela esta vazia.

                if os.path.exists(pasta_base) and os.path.isdir(pasta_base):  # Confirma que a pasta principal ainda existe.
                    os.rmdir(pasta_base)  # Remove a pasta principal depois de remover a subpasta.

                print("Limpeza concluida com seguranca.")  # Informa que os itens de teste foram removidos.
                """
            ),
            md(
                """
                ## Resumo importante

                Voce acabou de ver um ciclo muito comum em automacao:

                1. criar
                2. renomear
                3. remover

                Sempre teste primeiro em pastas de exemplo, nunca em arquivos importantes.
                """
            ),
        ],
    )

    write_notebook(
        folder / "Aula04 - Projeto guiado - Organizador de arquivos.ipynb",
        "Aula04 - Projeto guiado - Organizador de arquivos",
        [
            md(
                """
                # Aula04 - Projeto guiado - Organizador de arquivos

                Nesta aula vamos juntar varias funcoes do modulo `os` em um mini projeto.

                Objetivo:
                mover arquivos para pastas diferentes de acordo com a extensao.
                """
            ),
            md(
                """
                ## Ideia do projeto

                O projeto usa:

                - `os.listdir()` para percorrer a pasta
                - `os.path.join()` para montar caminhos
                - `os.path.splitext()` para separar nome e extensao
                - `os.makedirs()` para criar pastas de destino
                - `os.rename()` para mover arquivos

                Tambem aparecem ideias importantes para iniciantes:

                - dicionario
                - laco `for`
                - `if`
                - `continue`
                """
            ),
            md(
                """
                ## Conceitos importantes antes do codigo

                - `os.path.splitext("relatorio.pdf")` devolve uma tupla como `("relatorio", ".pdf")`
                - `mapa_de_destinos.get(extensao)` procura uma chave no dicionario
                - `continue` pula para a proxima repeticao do laco
                - `f"texto {variavel}"` e uma f-string, usada para montar textos dinamicos
                """
            ),
            code(
                """
                import os  # Importa o modulo os para lidar com caminhos e movimentacao simples.

                pasta_origem = "os"  # Define a pasta que sera analisada pelo organizador.
                mapa_de_destinos = {  # Cria um dicionario que relaciona extensoes com nomes de pastas.
                    ".md": "textos",  # Diz que arquivos Markdown devem ir para a pasta textos.
                    ".ipynb": "notebooks",  # Diz que notebooks devem ir para a pasta notebooks.
                    ".py": "scripts",  # Diz que scripts Python devem ir para a pasta scripts.
                }  # Fecha o dicionario de mapeamento.

                for nome_item in os.listdir(pasta_origem):  # Percorre cada item encontrado dentro da pasta de origem.
                    caminho_item = os.path.join(pasta_origem, nome_item)  # Monta o caminho completo do item atual.

                    if not os.path.isfile(caminho_item):  # Ignora pastas para evitar mover diretorios por engano.
                        continue  # Vai direto para o proximo item do laco.

                    nome_sem_extensao, extensao = os.path.splitext(nome_item)  # Separa o nome do arquivo de sua extensao.
                    pasta_destino = mapa_de_destinos.get(extensao)  # Procura no dicionario qual pasta corresponde a extensao encontrada.

                    if pasta_destino is None:  # Verifica se a extensao atual nao foi mapeada no dicionario.
                        print(f"Ignorando {nome_item} porque a extensao nao foi mapeada.")  # Informa que o arquivo foi ignorado.
                        continue  # Pula para o proximo item sem tentar mover o arquivo atual.

                    caminho_pasta_destino = os.path.join(pasta_origem, pasta_destino)  # Monta o caminho da pasta de destino.
                    os.makedirs(caminho_pasta_destino, exist_ok=True)  # Cria a pasta de destino caso ela ainda nao exista.

                    novo_caminho = os.path.join(caminho_pasta_destino, nome_item)  # Monta o caminho final do arquivo.
                    os.rename(caminho_item, novo_caminho)  # Move o arquivo atual para a pasta de destino.

                    print(f"Arquivo {nome_item} movido para {pasta_destino}.")  # Resume a acao feita para o usuario.
                """
            ),
            md(
                """
                ## Desafio

                Adapte o codigo para:

                - criar uma pasta `outros` para extensoes desconhecidas
                - ignorar arquivos temporarios
                - organizar outra pasta de testes
                """
            ),
        ],
    )

    write_notebook(
        folder / "Aula05 - Trabalhando melhor com caminhos.ipynb",
        "Aula05 - Trabalhando melhor com caminhos",
        [
            md(
                """
                # Aula05 - Trabalhando melhor com caminhos

                Nesta aula vamos estudar funcoes muito uteis do submodulo `os.path`.

                Elas ajudam a:

                - transformar caminho relativo em absoluto
                - separar nome de extensao
                - descobrir pasta pai
                - pegar apenas o nome final
                - normalizar um caminho
                """
            ),
            md(
                """
                ## Funcoes estudadas

                - `os.path.abspath()`
                - `os.path.basename()`
                - `os.path.dirname()`
                - `os.path.splitext()`
                - `os.path.relpath()`
                - `os.path.normpath()`
                """
            ),
            code(
                """
                import os  # Importa o modulo os para usar as funcoes do submodulo path.

                caminho_relativo = os.path.join("os", "README.md")  # Monta um caminho relativo simples para o exemplo.
                caminho_absoluto = os.path.abspath(caminho_relativo)  # Converte o caminho relativo em caminho absoluto.
                nome_final = os.path.basename(caminho_absoluto)  # Extrai apenas o nome final do caminho.
                pasta_pai = os.path.dirname(caminho_absoluto)  # Extrai a pasta pai do caminho informado.
                nome_sem_extensao, extensao = os.path.splitext(nome_final)  # Separa o nome do arquivo de sua extensao.

                print(caminho_relativo)  # Mostra o caminho relativo original.
                print(caminho_absoluto)  # Mostra o caminho absoluto correspondente.
                print(nome_final)  # Mostra apenas o nome do arquivo.
                print(pasta_pai)  # Mostra a pasta onde o arquivo esta localizado.
                print(nome_sem_extensao)  # Mostra o nome do arquivo sem extensao.
                print(extensao)  # Mostra apenas a extensao do arquivo.
                """
            ),
            code(
                """
                import os  # Importa o modulo os para demonstrar caminhos relativos e normalizacao.

                caminho_mal_montado = "os/../os//README.md"  # Cria um exemplo de caminho com redundancias.
                caminho_normalizado = os.path.normpath(caminho_mal_montado)  # Remove partes redundantes e organiza o caminho.
                caminho_relativo = os.path.relpath("os/README.md", start=".")  # Calcula um caminho relativo a partir da pasta atual.

                print(caminho_mal_montado)  # Mostra o caminho antes da normalizacao.
                print(caminho_normalizado)  # Mostra o caminho depois da normalizacao.
                print(caminho_relativo)  # Mostra o caminho relativo calculado.
                """
            ),
            md(
                """
                ## O que cada retorno representa

                - caminho absoluto: caminho completo desde a raiz do sistema
                - basename: ultimo trecho do caminho
                - dirname: caminho da pasta pai
                - splitext: tupla com nome e extensao
                """
            ),
        ],
    )

    write_notebook(
        folder / "Aula06 - Percorrendo subpastas com os.walk.ipynb",
        "Aula06 - Percorrendo subpastas com os.walk",
        [
            md(
                """
                # Aula06 - Percorrendo subpastas com os.walk

                `os.walk()` e muito usado quando voce quer atravessar uma arvore de pastas.

                Ele visita:

                - a pasta atual
                - as subpastas
                - as subpastas das subpastas
                - e assim por diante
                """
            ),
            md(
                """
                ## O que `os.walk()` devolve

                A cada repeticao, `os.walk()` devolve uma tupla com tres partes:

                - `raiz`: a pasta atual sendo visitada
                - `pastas`: a lista de subpastas dentro dessa raiz
                - `arquivos`: a lista de arquivos dentro dessa raiz
                """
            ),
            code(
                """
                import os  # Importa o modulo os para usar a funcao walk.

                pasta_inicial = "os"  # Define a pasta que sera percorrida recursivamente.

                for raiz, pastas, arquivos in os.walk(pasta_inicial):  # Percorre todas as pastas e subpastas a partir do ponto inicial.
                    print("Raiz atual:", raiz)  # Mostra qual pasta esta sendo visitada neste momento.
                    print("Subpastas:", pastas)  # Mostra a lista de subpastas encontradas dentro da raiz atual.
                    print("Arquivos:", arquivos)  # Mostra a lista de arquivos encontrados dentro da raiz atual.
                    print("-" * 50)  # Cria uma divisao visual entre uma iteracao e outra.
                """
            ),
            code(
                """
                import os  # Importa o modulo os para um segundo exemplo com filtro.

                pasta_inicial = "os"  # Define a mesma pasta inicial do exemplo anterior.

                for raiz, pastas, arquivos in os.walk(pasta_inicial):  # Percorre novamente a estrutura de pastas.
                    for arquivo in arquivos:  # Percorre cada arquivo encontrado na raiz atual.
                        if arquivo.endswith(".ipynb"):  # Verifica se o arquivo atual termina com a extensao .ipynb.
                            caminho_completo = os.path.join(raiz, arquivo)  # Monta o caminho completo do notebook encontrado.
                            print(caminho_completo)  # Exibe o caminho completo do notebook atual.
                """
            ),
            md(
                """
                ## Quando usar `os.walk()`

                - para montar inventarios de arquivos
                - para encontrar arquivos por extensao
                - para preparar migracoes simples
                - para gerar relatorios sobre uma pasta inteira
                """
            ),
        ],
    )

    write_notebook(
        folder / "Aula07 - Variaveis de ambiente e informacoes do sistema.ipynb",
        "Aula07 - Variaveis de ambiente e informacoes do sistema",
        [
            md(
                """
                # Aula07 - Variaveis de ambiente e informacoes do sistema

                O modulo `os` tambem fornece acesso a variaveis de ambiente e algumas informacoes basicas do sistema.

                Variavel de ambiente e um valor configurado fora do Python, normalmente pelo sistema operacional.
                """
            ),
            md(
                """
                ## Objetos e funcoes estudadas

                - `os.environ`
                - `os.getenv()`
                - `os.name`
                - `os.cpu_count()`
                """
            ),
            code(
                """
                import os  # Importa o modulo os para acessar variaveis de ambiente e dados do sistema.

                home = os.getenv("USERPROFILE")  # Tenta ler a variavel USERPROFILE, comum no Windows.
                sistema = os.name  # Consulta o identificador simples do sistema operacional.
                total_cpus = os.cpu_count()  # Descobre quantos nucleos logicos de CPU o Python consegue enxergar.

                print(home)  # Mostra o valor da variavel de ambiente lida.
                print(sistema)  # Mostra o nome resumido do sistema, como nt no Windows.
                print(total_cpus)  # Mostra a quantidade de CPUs logicas disponiveis.
                """
            ),
            code(
                """
                import os  # Importa o modulo os para acessar o mapeamento completo de variaveis.

                variaveis = os.environ  # Guarda em uma variavel o objeto que representa o conjunto de variaveis de ambiente.

                print(type(variaveis))  # Mostra o tipo do objeto para voce perceber que ele funciona como um dicionario.
                print("PATH" in variaveis)  # Verifica se a chave PATH existe entre as variaveis de ambiente.

                if "PATH" in variaveis:  # Confirma se a variavel PATH realmente existe antes de acessa-la.
                    print(variaveis["PATH"])  # Mostra o valor completo da variavel PATH.
                """
            ),
            md(
                """
                ## Diferenca entre `os.environ` e `os.getenv()`

                - `os.environ` funciona como um dicionario completo
                - `os.getenv("NOME")` pega apenas uma chave especifica

                Para iniciantes, `os.getenv()` costuma ser mais simples quando voce quer ler apenas uma variavel.
                """
            ),
        ],
    )


def build_re_course() -> None:
    folder = ROOT / "re"

    write_text(
        folder / "README.md",
        """
        # Modulo: re

        O modulo `re` serve para trabalhar com expressoes regulares.
        Expressoes regulares ajudam a localizar, validar, extrair, limpar e transformar textos com base em padroes.

        ## O que voce vai aprender

        - como funciona `re.search()`
        - o que e um objeto `Match`
        - o que significa usar `r"..."` em um padrao
        - diferenca entre `search`, `match`, `fullmatch`, `findall` e `finditer`
        - simbolos como `\\d`, `\\w`, `\\s`, `.`, `^` e `$`
        - conjuntos com colchetes `[]`
        - quantificadores como `+`, `*`, `?`, `{n}` e `{n,m}`
        - grupos, alternancia, flags e substituicoes
        - projetos de extracao e validacao de dados

        ## Ordem sugerida

        1. `Aula01 - Introducao a expressoes regulares.ipynb`
        2. `Aula02 - search, match e findall.ipynb`
        3. `Aula03 - Metacaracteres fundamentais.ipynb`
        4. `Aula04 - Projeto guiado - Extrator de dados.ipynb`
        5. `Aula05 - Colchetes, intervalos e negacoes.ipynb`
        6. `Aula06 - Grupos, flags e alternancia.ipynb`
        7. `Aula07 - Substituicoes, limpeza e split.ipynb`
        8. `Aula08 - Validando formatos comuns.ipynb`
        """,
    )

    write_notebook(
        folder / "Aula01 - Introducao a expressoes regulares.ipynb",
        "Aula01 - Introducao a expressoes regulares",
        [
            md(
                """
                # Aula01 - Introducao a expressoes regulares

                O modulo `re` permite procurar padroes dentro de textos.

                Pense assim:

                - busca comum: procura um texto exato
                - expressao regular: procura um formato

                Exemplo de formato:

                - um numero
                - duas letras maiusculas
                - uma data como `21/04/2026`
                - um email simples
                """
            ),
            md(
                """
                ## Funcao: `re.search(padrao, texto)`

                `search` procura a primeira parte do texto que combina com o padrao.

                Parametros:

                - `padrao`: a regra que voce quer procurar
                - `texto`: a string onde a busca sera feita

                Retorno:

                - objeto `Match` se encontrar
                - `None` se nao encontrar
                """
            ),
            code(
                """
                import re  # Importa o modulo re, que contem funcoes para expressoes regulares.

                texto = "O pedido 458 foi enviado."  # Cria uma string com um numero dentro.
                padrao = r"\\d+"  # Define um padrao que significa um ou mais digitos numericos.

                resultado = re.search(padrao, texto)  # Procura a primeira sequencia de digitos no texto.

                print(resultado)  # Mostra o objeto Match retornado pela busca.

                if resultado:  # Confirma que algo foi encontrado antes de acessar os dados do Match.
                    print(resultado.group())  # Mostra o trecho exato do texto que casou com o padrao.
                """
            ),
            md(
                """
                ## O que e o objeto `Match`

                O objeto `Match` representa uma correspondencia encontrada no texto.

                Com ele voce pode descobrir:

                - o texto que foi capturado
                - a posicao inicial
                - a posicao final
                - os grupos capturados
                """
            ),
            code(
                """
                import re  # Importa o modulo re para um segundo exemplo com o objeto Match.

                texto = "Codigo: AB123"  # Cria um texto simples com letras e numeros.
                padrao = r"AB\\d+"  # Define um padrao que espera AB seguido de um ou mais digitos.

                resultado = re.search(padrao, texto)  # Executa a busca do padrao no texto informado.

                if resultado:  # Confirma que a correspondencia existe.
                    print(resultado.group())  # Mostra o trecho que combinou com o padrao.
                    print(resultado.start())  # Mostra o indice onde a correspondencia comeca.
                    print(resultado.end())  # Mostra o indice onde a correspondencia termina.
                """
            ),
            md(
                """
                ## Por que usamos `r"..."` nos padroes

                O `r` antes da string significa **raw string**.

                Isso ajuda porque a barra invertida `\\` e muito usada nas expressoes regulares.

                Exemplo:

                - `r"\\d+"` e mais legivel
                - sem `r`, voce precisaria pensar com mais cuidado em escapes do proprio Python
                """
            ),
            code(
                """
                padrao_sem_raw = "\\\\d+"  # Cria uma string comum que precisa escapar a barra invertida do Python.
                padrao_com_raw = r"\\d+"  # Cria uma raw string, que fica mais legivel em regex.

                print(padrao_sem_raw)  # Mostra o conteudo real da string sem raw.
                print(padrao_com_raw)  # Mostra o conteudo real da raw string.
                """
            ),
        ],
    )

    write_notebook(
        folder / "Aula02 - search, match e findall.ipynb",
        "Aula02 - search, match e findall",
        [
            md(
                """
                # Aula02 - search, match e findall

                Agora vamos comparar funcoes importantes do modulo `re`.

                - `re.search()` procura em qualquer parte do texto
                - `re.match()` procura apenas no comeco do texto
                - `re.fullmatch()` exige que o texto inteiro siga o padrao
                - `re.findall()` devolve todas as ocorrencias
                - `re.finditer()` devolve varios objetos `Match`
                """
            ),
            code(
                """
                import re  # Importa o modulo re para comparar formas de busca.

                texto = "Produto 123 cadastrado"  # Cria um texto de exemplo.
                padrao = r"Produto"  # Define um padrao literal simples.

                print(re.search(padrao, texto))  # Procura o padrao em qualquer parte do texto.
                print(re.match(padrao, texto))  # Procura o padrao apenas no inicio do texto.
                print(re.fullmatch(padrao, texto))  # Exige que o texto inteiro seja exatamente igual ao padrao.
                """
            ),
            md(
                """
                ## Funcao: `re.findall()`

                `findall` e util quando voce quer todas as ocorrencias encontradas.

                Retorno:

                - uma lista com os trechos encontrados
                """
            ),
            code(
                """
                import re  # Importa o modulo re para localizar varias ocorrencias.

                texto = "Os numeros sao 10, 20 e 30."  # Cria um texto contendo tres numeros.
                padrao = r"\\d+"  # Define um padrao que encontra uma ou mais ocorrencias de digitos.

                numeros = re.findall(padrao, texto)  # Procura todos os blocos numericos dentro do texto.

                print(numeros)  # Mostra a lista com todos os numeros encontrados.
                print(type(numeros))  # Mostra o tipo do objeto retornado por findall.
                """
            ),
            md(
                """
                ## Funcao: `re.finditer()`

                `finditer` e parecida com `findall`, mas devolve objetos `Match`.
                Isso e importante quando voce quer saber posicoes.
                """
            ),
            code(
                """
                import re  # Importa o modulo re para percorrer correspondencias detalhadas.

                texto = "A sala 12 fica ao lado da sala 25."  # Cria um texto com mais de um numero.
                padrao = r"\\d+"  # Define um padrao que encontra blocos numericos.

                for correspondencia in re.finditer(padrao, texto):  # Percorre cada objeto Match encontrado.
                    print(correspondencia.group())  # Mostra o texto encontrado na correspondencia atual.
                    print(correspondencia.start())  # Mostra o indice inicial da correspondencia.
                    print(correspondencia.end())  # Mostra o indice final da correspondencia.
                    print("-" * 30)  # Separa visualmente uma correspondencia da outra.
                """
            ),
        ],
    )

    write_notebook(
        folder / "Aula03 - Metacaracteres fundamentais.ipynb",
        "Aula03 - Metacaracteres fundamentais",
        [
            md(
                """
                # Aula03 - Metacaracteres fundamentais

                Nesta aula vamos estudar simbolos muito importantes das expressoes regulares.

                Os principais para comecar sao:

                - `\\d`
                - `\\w`
                - `\\s`
                - `.`
                - `^`
                - `$`
                """
            ),
            md(
                """
                ## O que cada simbolo significa

                - `\\d`: um digito
                - `\\w`: caractere de palavra, como letra, numero ou `_`
                - `\\s`: espaco em branco, como espaco, tab ou quebra de linha
                - `.`: quase qualquer caractere
                - `^`: comeco da string ou linha
                - `$`: fim da string ou linha
                """
            ),
            code(
                """
                import re  # Importa o modulo re para testar os metacaracteres.

                texto = "Rua A, numero 25"  # Cria um texto com letras, espacos e numeros.

                print(re.findall(r"\\d", texto))  # Encontra cada digito separadamente.
                print(re.findall(r"\\w", texto))  # Encontra cada caractere de palavra separadamente.
                print(re.findall(r"\\s", texto))  # Encontra os espacos em branco presentes no texto.
                """
            ),
            md(
                """
                ## Entendendo `\\w`

                `\\w` significa **word character**.

                Em termos praticos, costuma representar:

                - letras
                - numeros
                - underscore `_`

                Importante:
                ele nao significa "uma palavra inteira".
                Ele significa "um caractere que pode fazer parte de uma palavra".
                """
            ),
            code(
                """
                import re  # Importa o modulo re para mostrar a diferenca entre um caractere e varios caracteres.

                texto = "abc_123"  # Cria um texto com letras, underscore e numeros.

                print(re.findall(r"\\w", texto))  # Encontra um caractere de palavra por vez.
                print(re.findall(r"\\w+", texto))  # Encontra uma sequencia de um ou mais caracteres de palavra.
                """
            ),
            md(
                """
                ## Entendendo `\\s`

                `\\s` representa espaco em branco.

                Isso inclui:

                - espaco comum
                - tabulacao
                - quebra de linha
                """
            ),
            code(
                """
                import re  # Importa o modulo re para testar o simbolo de espaco em branco.

                texto = "Linha 1\\nLinha 2\\tFim"  # Cria uma string com quebra de linha e tabulacao.

                print(re.findall(r"\\s", texto))  # Encontra todos os caracteres de espaco em branco.
                print(re.sub(r"\\s+", " ", texto))  # Troca sequencias de espacos em branco por um unico espaco.
                """
            ),
            md(
                """
                ## Entendendo `.` , `^` e `$`

                - `.` representa quase qualquer caractere
                - `^` verifica o inicio
                - `$` verifica o fim

                Observacao:
                o ponto `.` nao representa literalmente um ponto final.
                Se voce quiser um ponto literal, use `\\.`.
                """
            ),
            code(
                """
                import re  # Importa o modulo re para testar ponto e ancoras.

                print(re.search(r"^Pedido", "Pedido 10"))  # Verifica se a string comeca com a palavra Pedido.
                print(re.search(r"10$", "Pedido 10"))  # Verifica se a string termina com 10.
                print(re.findall(r"a.", "casa"))  # Encontra a letra a seguida de qualquer caractere.
                print(re.findall(r"\\.", "www.site.com"))  # Encontra apenas os pontos literais.
                """
            ),
        ],
    )

    write_notebook(
        folder / "Aula04 - Projeto guiado - Extrator de dados.ipynb",
        "Aula04 - Projeto guiado - Extrator de dados",
        [
            md(
                """
                # Aula04 - Projeto guiado - Extrator de dados

                Vamos criar um extrator simples de informacoes contidas em um texto maior.

                Objetivo:
                encontrar emails, telefones e datas dentro de um bloco de texto.
                """
            ),
            md(
                """
                ## O texto do projeto

                Neste projeto, vamos aplicar `re.findall()` em um bloco maior de texto.

                A ideia e treinar tres tipos de extracao:

                - email
                - telefone
                - data
                """
            ),
            md(
                """
                ## Lendo o padrao de email simbolo por simbolo

                O padrao usado sera:

                `r"[\\w.-]+@[\\w.-]+\\.\\w+"`

                Explicacao:

                - `[]`: cria um conjunto de caracteres permitidos
                - `\\w`: permite letra, numero e underscore
                - `.` dentro de `[]`: aqui representa o ponto literal
                - `-` dentro de `[]`: aqui representa o hifen literal
                - `[\\w.-]`: significa "aceite letras, numeros, underscore, ponto ou hifen"
                - `+`: uma ou mais repeticoes do conjunto anterior
                - `@`: exige o simbolo arroba
                - `\\.`: exige um ponto literal fora dos colchetes
                - `\\w+`: exige uma extensao simples com uma ou mais letras ou numeros
                """
            ),
            md(
                """
                ## Lendo o padrao de telefone simbolo por simbolo

                O padrao usado sera:

                `r"\\(\\d{2}\\)\\s?\\d{4,5}-\\d{4}"`

                Explicacao:

                - `\\(`: abre parenteses literal
                - `\\d{2}`: dois digitos para o DDD
                - `\\)`: fecha parenteses literal
                - `\\s?`: zero ou um espaco em branco
                - `\\d{4,5}`: quatro ou cinco digitos para o numero principal
                - `-`: hifen literal
                - `\\d{4}`: quatro digitos finais
                """
            ),
            md(
                """
                ## Lendo o padrao de data

                O padrao usado sera:

                `r"\\d{2}/\\d{2}/\\d{4}"`

                Explicacao:

                - `\\d{2}`: dois digitos
                - `/`: barra literal
                - `\\d{2}`: dois digitos para o mes
                - `/`: barra literal
                - `\\d{4}`: quatro digitos para o ano
                """
            ),
            code(
                """
                import re  # Importa o modulo re para localizar padroes no texto do projeto.

                texto = (  # Cria uma string multilinha usando parenteses para facilitar a leitura.
                    "Contato comercial: maria.silva@email.com\\n"  # Adiciona uma linha com email comercial.
                    "Telefone: (11) 99888-7766\\n"  # Adiciona uma linha com telefone no formato brasileiro.
                    "Data da proposta: 21/04/2026\\n"  # Adiciona uma linha com data no formato dia/mes/ano.
                    "Contato tecnico: suporte@empresa.com.br\\n"  # Adiciona outra linha com email tecnico.
                )  # Fecha a construcao da string de entrada.

                padrao_email = r"[\\w.-]+@[\\w.-]+\\.\\w+"  # Define um padrao simples para localizar emails.
                padrao_telefone = r"\\(\\d{2}\\)\\s?\\d{4,5}-\\d{4}"  # Define um padrao simples para localizar telefones brasileiros.
                padrao_data = r"\\d{2}/\\d{2}/\\d{4}"  # Define um padrao simples para localizar datas no formato dia/mes/ano.

                emails = re.findall(padrao_email, texto)  # Procura todos os emails presentes no texto.
                telefones = re.findall(padrao_telefone, texto)  # Procura todos os telefones presentes no texto.
                datas = re.findall(padrao_data, texto)  # Procura todas as datas presentes no texto.

                print("Emails encontrados:", emails)  # Mostra a lista de emails localizados.
                print("Telefones encontrados:", telefones)  # Mostra a lista de telefones localizados.
                print("Datas encontradas:", datas)  # Mostra a lista de datas localizadas.
                """
            ),
            code(
                """
                import re  # Importa o modulo re para mostrar as correspondencias com mais detalhes.

                texto = (  # Cria novamente a string principal do projeto.
                    "Contato comercial: maria.silva@email.com\\n"  # Adiciona a primeira linha de exemplo.
                    "Telefone: (11) 99888-7766\\n"  # Adiciona a segunda linha de exemplo.
                    "Data da proposta: 21/04/2026\\n"  # Adiciona a terceira linha de exemplo.
                    "Contato tecnico: suporte@empresa.com.br\\n"  # Adiciona a quarta linha de exemplo.
                )  # Fecha a string de entrada.

                padrao_email = r"[\\w.-]+@[\\w.-]+\\.\\w+"  # Define novamente o padrao de email.

                for correspondencia in re.finditer(padrao_email, texto):  # Percorre cada email encontrado como objeto Match.
                    print(correspondencia.group())  # Mostra o email encontrado.
                    print(correspondencia.start())  # Mostra o indice inicial do email no texto.
                    print(correspondencia.end())  # Mostra o indice final do email no texto.
                    print("-" * 30)  # Separa visualmente um email do outro.
                """
            ),
            md(
                """
                ## Como este projeto pode crescer

                Voce pode adaptar este extrator para:

                - ler curriculos
                - validar cadastros
                - extrair dados de contratos
                - preparar textos para processamento posterior
                """
            ),
        ],
    )

    write_notebook(
        folder / "Aula05 - Colchetes, intervalos e negacoes.ipynb",
        "Aula05 - Colchetes, intervalos e negacoes",
        [
            md(
                """
                # Aula05 - Colchetes, intervalos e negacoes

                Nesta aula vamos aprofundar o uso dos colchetes `[]`.

                Os colchetes criam um conjunto de caracteres permitidos.
                Eles aparecem muito em validacoes e extracoes.
                """
            ),
            md(
                """
                ## Ideias principais

                - `[abc]` aceita `a`, `b` ou `c`
                - `[0-9]` aceita qualquer digito de 0 a 9
                - `[A-Z]` aceita letras maiusculas
                - `[^0-9]` aceita qualquer caractere que nao seja digito

                O acento circunflexo `^` dentro dos colchetes significa negacao.
                Fora dos colchetes ele significa inicio da string ou linha.
                """
            ),
            code(
                """
                import re  # Importa o modulo re para praticar conjuntos de caracteres.

                texto = "Casa 25, Bloco B"  # Cria um texto com letras, numero e espacos.

                print(re.findall(r"[A-Z]", texto))  # Encontra letras maiusculas.
                print(re.findall(r"[a-z]", texto))  # Encontra letras minusculas.
                print(re.findall(r"[0-9]", texto))  # Encontra digitos.
                print(re.findall(r"[CB]", texto))  # Encontra apenas C ou B.
                """
            ),
            code(
                """
                import re  # Importa o modulo re para praticar negacao dentro dos colchetes.

                texto = "Sala 305"  # Cria um texto curto com letras, espaco e numeros.

                print(re.findall(r"[^0-9]", texto))  # Encontra tudo o que nao e digito.
                print(re.findall(r"[^A-Z]", texto))  # Encontra tudo o que nao e letra maiuscula.
                """
            ),
            md(
                """
                ## Sobre `-` e `.` dentro de `[]`

                - o hifen `-` pode indicar intervalo, como em `[0-9]`
                - o hifen tambem pode ser literal, dependendo da posicao
                - o ponto `.` dentro de `[]` costuma ser apenas ponto literal

                Exemplo:

                - `[\\w.-]` aceita caractere de palavra, ponto ou hifen
                """
            ),
            code(
                """
                import re  # Importa o modulo re para um ultimo exemplo de colchetes.

                texto = "arquivo-teste_v2.txt"  # Cria um nome de arquivo para o exemplo.

                print(re.findall(r"[\\w.-]+", texto))  # Encontra uma sequencia composta por letras, numeros, underscore, ponto e hifen.
                """
            ),
        ],
    )

    write_notebook(
        folder / "Aula06 - Grupos, flags e alternancia.ipynb",
        "Aula06 - Grupos, flags e alternancia",
        [
            md(
                """
                # Aula06 - Grupos, flags e alternancia

                Nesta aula vamos estudar recursos que deixam as expressoes regulares mais organizadas e mais poderosas.

                Vamos estudar:

                - grupos com parenteses
                - grupos nomeados
                - alternancia com `|`
                - flags como `IGNORECASE` e `MULTILINE`
                """
            ),
            code(
                """
                import re  # Importa o modulo re para trabalhar com grupos.

                texto = "Data: 21/04/2026"  # Cria um texto simples com uma data.
                padrao = r"(\\d{2})/(\\d{2})/(\\d{4})"  # Cria tres grupos: dia, mes e ano.

                resultado = re.search(padrao, texto)  # Procura uma data no texto.

                if resultado:  # Confirma que a data foi encontrada.
                    print(resultado.group(0))  # Mostra o texto inteiro que combinou com o padrao.
                    print(resultado.group(1))  # Mostra apenas o primeiro grupo, que e o dia.
                    print(resultado.group(2))  # Mostra apenas o segundo grupo, que e o mes.
                    print(resultado.group(3))  # Mostra apenas o terceiro grupo, que e o ano.
                """
            ),
            code(
                """
                import re  # Importa o modulo re para demonstrar grupos nomeados.

                texto = "Data: 21/04/2026"  # Cria novamente um texto com data.
                padrao = r"(?P<dia>\\d{2})/(?P<mes>\\d{2})/(?P<ano>\\d{4})"  # Define grupos com nomes explicitos.

                resultado = re.search(padrao, texto)  # Procura a data seguindo o novo padrao nomeado.

                if resultado:  # Confirma que a data foi encontrada.
                    print(resultado.group("dia"))  # Mostra o grupo chamado dia.
                    print(resultado.group("mes"))  # Mostra o grupo chamado mes.
                    print(resultado.group("ano"))  # Mostra o grupo chamado ano.
                """
            ),
            md(
                """
                ## Alternancia com `|`

                O simbolo `|` significa "ou".

                Exemplo:

                - `casa|apartamento` encontra `casa` ou `apartamento`
                """
            ),
            code(
                """
                import re  # Importa o modulo re para demonstrar alternancia e flags.

                texto = "Casa, apartamento, CASA"  # Cria um texto com palavras repetidas em diferentes formas.

                print(re.findall(r"casa|apartamento", texto))  # Procura exatamente casa minusculo ou apartamento minusculo.
                print(re.findall(r"casa|apartamento", texto, flags=re.IGNORECASE))  # Repete a busca ignorando diferenca entre maiusculas e minusculas.
                """
            ),
            code(
                """
                import re  # Importa o modulo re para demonstrar a flag MULTILINE.

                texto = "item: arroz\\nvalor: 10\\nitem: feijao"  # Cria uma string com varias linhas.

                encontrados = re.findall(r"^item: .+$", texto, flags=re.MULTILINE)  # Procura linhas inteiras que comecem com item:.

                print(encontrados)  # Mostra as linhas encontradas.
                """
            ),
        ],
    )

    write_notebook(
        folder / "Aula07 - Substituicoes, limpeza e split.ipynb",
        "Aula07 - Substituicoes, limpeza e split",
        [
            md(
                """
                # Aula07 - Substituicoes, limpeza e split

                Nesta aula vamos estudar tres usos muito praticos do modulo `re`:

                - substituir com `re.sub()`
                - limpar textos
                - dividir textos com `re.split()`
                """
            ),
            md(
                """
                ## Funcao: `re.sub(padrao, novo_valor, texto)`

                `sub` significa substituicao.

                Parametros:

                - `padrao`: o que voce quer localizar
                - `novo_valor`: o valor que vai entrar no lugar
                - `texto`: a string original
                """
            ),
            code(
                """
                import re  # Importa o modulo re para substituir trechos do texto.

                texto = "CPF: 123.456.789-00"  # Cria um texto com varios digitos.
                padrao = r"\\d"  # Define um padrao que encontra um digito por vez.

                texto_mascarado = re.sub(padrao, "*", texto)  # Troca todos os digitos por asteriscos.

                print(texto_mascarado)  # Mostra o resultado depois da substituicao.
                """
            ),
            md(
                """
                ## Limpando excesso de espaco com `\\s+`

                `\\s+` significa:

                - `\\s`: espaco em branco
                - `+`: uma ou mais repeticoes

                Entao `\\s+` encontra blocos de um ou mais espacos em branco.
                """
            ),
            code(
                """
                import re  # Importa o modulo re para limpar espacos em branco.

                texto = "Python   e\\n\\tuma linguagem   poderosa."  # Cria um texto com espacos, quebra de linha e tabulacao.
                texto_limpo = re.sub(r"\\s+", " ", texto).strip()  # Troca blocos de espacos em branco por um unico espaco e remove sobra nas pontas.

                print(texto_limpo)  # Mostra o texto final limpo.
                """
            ),
            md(
                """
                ## Funcao: `re.split()`

                `split` divide um texto com base em um padrao.
                """
            ),
            code(
                """
                import re  # Importa o modulo re para dividir uma string em partes.

                texto = "python, java; javascript | go"  # Cria um texto com separadores diferentes.
                partes = re.split(r"[,;|]\\s*", texto)  # Divide o texto sempre que encontrar virgula, ponto e virgula ou barra vertical seguidos de espacos opcionais.

                print(partes)  # Mostra a lista resultante da divisao.
                """
            ),
        ],
    )

    write_notebook(
        folder / "Aula08 - Validando formatos comuns.ipynb",
        "Aula08 - Validando formatos comuns",
        [
            md(
                """
                # Aula08 - Validando formatos comuns

                Nesta aula vamos usar `re.fullmatch()` para validar formatos inteiros.

                Importante:
                aqui vamos validar apenas o formato, nao a regra matematica completa de documentos como CPF.
                """
            ),
            code(
                """
                import re  # Importa o modulo re para validar formatos completos.

                padrao_cep = r"\\d{5}-\\d{3}"  # Define o formato simples de CEP brasileiro.
                padrao_placa = r"[A-Z]{3}-?\\d{4}"  # Define um formato simples de placa antiga com hifen opcional.
                padrao_email = r"[\\w.-]+@[\\w.-]+\\.\\w+"  # Define um formato simples de email.

                print(bool(re.fullmatch(padrao_cep, "12345-678")))  # Valida um CEP correto.
                print(bool(re.fullmatch(padrao_cep, "1234-678")))  # Valida um CEP incorreto.
                print(bool(re.fullmatch(padrao_placa, "ABC-1234")))  # Valida uma placa no formato antigo.
                print(bool(re.fullmatch(padrao_email, "nome@email.com")))  # Valida um email simples.
                """
            ),
            code(
                """
                import re  # Importa o modulo re para validar varios valores de uma vez.

                valores = [  # Cria uma lista com varios textos para teste.
                    "12345-678",  # Adiciona um CEP valido.
                    "11111-111",  # Adiciona outro CEP valido.
                    "12-345678",  # Adiciona um CEP invalido.
                ]  # Fecha a lista de valores.

                padrao_cep = r"\\d{5}-\\d{3}"  # Define novamente o padrao simples de CEP.

                for valor in valores:  # Percorre cada valor da lista.
                    valido = bool(re.fullmatch(padrao_cep, valor))  # Verifica se o valor inteiro segue o padrao do CEP.
                    print(valor, valido)  # Mostra o valor testado e o resultado da validacao.
                """
            ),
            md(
                """
                ## Fechamento do modulo `re`

                A partir daqui voce ja tem base para:

                - extrair dados
                - limpar textos
                - validar formatos simples
                - montar padroes mais completos aos poucos
                """
            ),
        ],
    )


def build_pytesseract_course() -> None:
    folder = ROOT / "pytesseract"

    write_text(
        folder / "README.md",
        """
        # Modulo: pytesseract

        `pytesseract` e uma biblioteca Python usada para OCR.
        OCR significa reconhecimento optico de caracteres.

        Em outras palavras:
        a biblioteca ajuda a transformar imagem em texto.

        ## Antes de estudar este modulo

        Voce precisa:

        - instalar `pytesseract`
        - instalar `Pillow`
        - instalar o programa Tesseract OCR no sistema

        No Windows, normalmente tambem e preciso informar o caminho do executavel `tesseract.exe`.

        ## O que voce vai aprender

        - leitura basica com `image_to_string`
        - uso de `lang` e `config`
        - pre-processamento de imagem
        - retorno detalhado com `image_to_boxes` e `image_to_data`
        - orientacao e saidas avancadas
        - OCR em lote com script Python

        ## Ordem sugerida

        1. `Aula01 - Instalacao e primeira leitura.ipynb`
        2. `Aula02 - Idiomas, configuracao e limpeza basica.ipynb`
        3. `Aula03 - Caixas, coordenadas e dados detalhados.ipynb`
        4. `Aula04 - Script de OCR em lote.py`
        5. `Aula05 - Pre-processamento para melhorar OCR.ipynb`
        6. `Aula06 - Orientacao e saidas avancadas.ipynb`
        """,
    )

    write_notebook(
        folder / "Aula01 - Instalacao e primeira leitura.ipynb",
        "Aula01 - Instalacao e primeira leitura",
        [
            md(
                """
                # Aula01 - Instalacao e primeira leitura

                Nesta aula voce vai entender o fluxo mais basico do OCR com `pytesseract`.

                Fluxo mental:

                1. ter uma imagem
                2. enviar a imagem para o OCR
                3. receber um texto de volta

                Observacao:
                este notebook pressupoe que o Tesseract OCR ja esteja instalado no sistema.
                """
            ),
            md(
                """
                ## Objetos importantes desta aula

                - `Image`: objeto de imagem da biblioteca Pillow
                - `ImageDraw`: objeto que desenha sobre a imagem
                - `pytesseract.image_to_string()`: funcao principal para extrair texto
                """
            ),
            code(
                """
                from PIL import Image, ImageDraw  # Importa classes da biblioteca Pillow para criar e desenhar uma imagem.
                import pytesseract  # Importa a biblioteca pytesseract, responsavel por conversar com o OCR Tesseract.

                imagem = Image.new("RGB", (500, 140), "white")  # Cria uma imagem nova com fundo branco, largura 500 e altura 140.
                desenho = ImageDraw.Draw(imagem)  # Cria um objeto de desenho para escrever dentro da imagem.

                desenho.text((20, 50), "Pedido 458 aprovado", fill="black")  # Escreve um texto simples na imagem para o OCR ler.

                imagem  # Exibe a imagem dentro do notebook para voce conferir visualmente o conteudo.
                """
            ),
            md(
                """
                ## Funcao: `pytesseract.image_to_string(imagem)`

                Esta e a funcao principal da biblioteca.

                Parametros comuns:

                - `imagem`: objeto Pillow ou caminho de imagem
                - `lang`: idioma esperado
                - `config`: configuracoes extras enviadas ao Tesseract

                Retorno:

                - uma string com o texto reconhecido
                """
            ),
            code(
                """
                from PIL import Image, ImageDraw  # Importa novamente as classes para manter o exemplo independente.
                import pytesseract  # Importa novamente a biblioteca de OCR para o segundo bloco.

                imagem = Image.new("RGB", (500, 140), "white")  # Cria uma nova imagem branca para o exemplo de leitura.
                desenho = ImageDraw.Draw(imagem)  # Cria o objeto que permite desenhar texto na imagem.
                desenho.text((20, 50), "Pedido 458 aprovado", fill="black")  # Escreve o texto que sera lido pelo OCR.

                texto_extraido = pytesseract.image_to_string(imagem)  # Envia a imagem ao OCR e recebe o texto reconhecido.

                print(texto_extraido)  # Mostra no console o texto que o OCR conseguiu ler.
                print(type(texto_extraido))  # Mostra o tipo do retorno para reforcar que a funcao devolve string.
                """
            ),
            md(
                """
                ## Erros comuns nesta etapa

                - Tesseract nao instalado
                - caminho do executavel nao configurado
                - imagem com pouco contraste
                - texto pequeno ou borrado
                """
            ),
        ],
    )

    write_notebook(
        folder / "Aula02 - Idiomas, configuracao e limpeza basica.ipynb",
        "Aula02 - Idiomas, configuracao e limpeza basica",
        [
            md(
                """
                # Aula02 - Idiomas, configuracao e limpeza basica

                Agora vamos melhorar a leitura do OCR.

                Nesta aula voce vai ver:

                - como apontar o caminho do executavel no Windows
                - como informar o idioma
                - como usar o parametro `config`
                - como converter a imagem para tons de cinza
                """
            ),
            code(
                """
                from PIL import Image, ImageDraw  # Importa classes para criar e editar a imagem de exemplo.
                import pytesseract  # Importa a biblioteca principal do OCR.

                pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"  # Define o caminho do executavel do Tesseract no Windows.

                imagem = Image.new("RGB", (500, 140), "white")  # Cria uma imagem branca para o teste.
                desenho = ImageDraw.Draw(imagem)  # Cria o objeto responsavel por desenhar no canvas da imagem.
                desenho.text((20, 50), "Nota fiscal numero 123", fill="black")  # Escreve um texto simples com letras pretas.

                imagem_cinza = imagem.convert("L")  # Converte a imagem para tons de cinza para simplificar a leitura do OCR.

                texto = pytesseract.image_to_string(imagem_cinza, lang="por")  # Extrai o texto pedindo ao OCR para priorizar o idioma portugues.

                print(texto)  # Mostra o resultado final da leitura.
                """
            ),
            md(
                """
                ## Sobre o parametro `config`

                O parametro `config` envia instrucoes extras ao motor OCR.

                Dois exemplos muito comentados:

                - `--psm`: page segmentation mode
                - `--oem`: OCR engine mode

                Para iniciantes, `--psm 6` costuma ser um bom primeiro teste quando a imagem tem um bloco simples de texto.
                """
            ),
            code(
                """
                from PIL import Image, ImageDraw  # Importa as classes para recriar a imagem neste bloco independente.
                import pytesseract  # Importa a biblioteca de OCR para usar o parametro config.

                imagem = Image.new("RGB", (500, 140), "white")  # Cria a imagem branca que recebera o texto do exemplo.
                desenho = ImageDraw.Draw(imagem)  # Cria o objeto de desenho vinculado a imagem.
                desenho.text((20, 50), "Relatorio mensal", fill="black")  # Insere um texto curto para o OCR reconhecer.

                configuracao = "--psm 6"  # Guarda uma configuracao que ajuda quando o texto esta em um bloco unico.
                texto = pytesseract.image_to_string(imagem, lang="por", config=configuracao)  # Executa o OCR usando idioma e configuracao personalizada.

                print(texto)  # Exibe o texto retornado pelo OCR.
                """
            ),
            code(
                """
                import pytesseract  # Importa a biblioteca pytesseract para consultar os idiomas disponiveis.

                idiomas = pytesseract.get_languages(config="")  # Pede ao Tesseract a lista de idiomas instalados.

                print(idiomas)  # Mostra a lista de idiomas disponiveis no ambiente.
                """
            ),
        ],
    )

    write_notebook(
        folder / "Aula03 - Caixas, coordenadas e dados detalhados.ipynb",
        "Aula03 - Caixas, coordenadas e dados detalhados",
        [
            md(
                """
                # Aula03 - Caixas, coordenadas e dados detalhados

                O OCR nao precisa devolver apenas texto puro.
                Ele tambem pode devolver informacoes detalhadas sobre onde cada caractere ou palavra foi encontrada.

                Funcoes estudadas:

                - `pytesseract.image_to_boxes()`
                - `pytesseract.image_to_data()`
                """
            ),
            md(
                """
                ## O que esses retornos representam

                - `image_to_boxes()`: devolve coordenadas por caractere
                - `image_to_data()`: devolve uma estrutura mais rica com texto, confianca e posicoes
                """
            ),
            code(
                """
                from PIL import Image, ImageDraw  # Importa classes para gerar uma imagem de teste.
                import pytesseract  # Importa a biblioteca de OCR.

                imagem = Image.new("RGB", (600, 180), "white")  # Cria uma imagem maior para comportar mais texto.
                desenho = ImageDraw.Draw(imagem)  # Cria o objeto usado para desenhar dentro da imagem.
                desenho.text((20, 40), "Cliente: Ana", fill="black")  # Escreve a primeira linha do texto de teste.
                desenho.text((20, 90), "Pedido: 458", fill="black")  # Escreve a segunda linha do texto de teste.

                caixas = pytesseract.image_to_boxes(imagem, lang="por")  # Pede ao OCR as coordenadas aproximadas de cada caractere.

                print(caixas)  # Mostra o texto bruto com as caixas retornadas pelo Tesseract.
                """
            ),
            md(
                """
                ## Funcao: `image_to_data`

                Esta funcao e muito util quando voce quer um retorno estruturado.

                Ela pode devolver:

                - palavra encontrada
                - confianca
                - coordenadas
                - largura e altura do bloco

                Ao usar `Output.DICT`, o retorno vira um dicionario de listas.
                """
            ),
            code(
                """
                from PIL import Image, ImageDraw  # Importa novamente as classes para um bloco independente.
                import pytesseract  # Importa novamente a biblioteca de OCR.
                from pytesseract import Output  # Importa Output para pedir o retorno em formato de dicionario.

                imagem = Image.new("RGB", (600, 180), "white")  # Cria outra imagem em branco para o exemplo estruturado.
                desenho = ImageDraw.Draw(imagem)  # Cria o objeto de desenho associado a imagem.
                desenho.text((20, 40), "Cliente: Ana", fill="black")  # Escreve a primeira linha que sera lida.
                desenho.text((20, 90), "Pedido: 458", fill="black")  # Escreve a segunda linha que sera lida.

                dados = pytesseract.image_to_data(imagem, lang="por", output_type=Output.DICT)  # Executa o OCR e pede um dicionario como retorno.

                print(dados.keys())  # Mostra as chaves disponiveis no dicionario retornado.
                print(dados["text"])  # Mostra a lista dos textos reconhecidos em cada bloco.
                print(dados["conf"])  # Mostra a lista das confiancas estimadas pelo OCR.
                """
            ),
            md(
                """
                ## Aplicacoes praticas

                - localizar campos em documentos
                - filtrar apenas trechos com boa confianca
                - desenhar caixas em volta das palavras
                - montar processamentos de documentos mais inteligentes
                """
            ),
        ],
    )

    write_text(
        folder / "Aula04 - Script de OCR em lote.py",
        """
        from pathlib import Path  # Importa Path para trabalhar com caminhos de forma mais moderna e legivel.
        from PIL import Image  # Importa Image para abrir as imagens que serao lidas pelo OCR.
        import pytesseract  # Importa pytesseract para extrair o texto das imagens.


        PASTA_IMAGENS = Path("pytesseract/imagens_entrada")  # Define a pasta onde o usuario deve colocar as imagens para processar.
        PASTA_SAIDA = Path("pytesseract/textos_saida")  # Define a pasta onde os arquivos de texto gerados serao salvos.
        EXTENSOES_VALIDAS = {".png", ".jpg", ".jpeg"}  # Define as extensoes de imagem aceitas pelo script.


        def configurar_ambiente() -> None:
            # Ajusta o caminho do Tesseract e cria as pastas minimas do fluxo.
            pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"  # Informa explicitamente onde esta o executavel do Tesseract.
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
        """,
    )

    write_notebook(
        folder / "Aula05 - Pre-processamento para melhorar OCR.ipynb",
        "Aula05 - Pre-processamento para melhorar OCR",
        [
            md(
                """
                # Aula05 - Pre-processamento para melhorar OCR

                Uma parte muito importante do OCR e preparar melhor a imagem antes da leitura.

                Nesta aula vamos ver:

                - aumento de tamanho
                - conversao para tons de cinza
                - binarizacao simples
                """
            ),
            md(
                """
                ## Ideia principal

                Quanto mais limpa e contrastada a imagem estiver, maiores costumam ser as chances de o OCR acertar.
                """
            ),
            code(
                """
                from PIL import Image, ImageDraw  # Importa classes para criar e desenhar a imagem de exemplo.
                import pytesseract  # Importa a biblioteca de OCR.

                imagem = Image.new("RGB", (400, 100), "white")  # Cria uma imagem base com fundo branco.
                desenho = ImageDraw.Draw(imagem)  # Cria o objeto de desenho ligado a imagem.
                desenho.text((10, 35), "Documento 321", fill="gray")  # Escreve um texto em cinza para simular um caso menos nitido.

                imagem_ampliada = imagem.resize((imagem.width * 2, imagem.height * 2))  # Aumenta o tamanho da imagem para facilitar a leitura do OCR.
                imagem_cinza = imagem_ampliada.convert("L")  # Converte a imagem ampliada para tons de cinza.
                imagem_binarizada = imagem_cinza.point(lambda pixel: 255 if pixel > 180 else 0)  # Transforma pixels claros em branco e pixels escuros em preto.

                texto = pytesseract.image_to_string(imagem_binarizada, lang="por")  # Executa OCR na imagem depois do pre-processamento.

                print(texto)  # Mostra o texto reconhecido apos a limpeza basica.
                """
            ),
            md(
                """
                ## O que cada etapa faz

                - `resize`: aumenta a imagem
                - `convert("L")`: transforma em tons de cinza
                - `point(...)`: aplica uma regra de limiar para deixar a imagem mais contrastada
                """
            ),
        ],
    )

    write_notebook(
        folder / "Aula06 - Orientacao e saidas avancadas.ipynb",
        "Aula06 - Orientacao e saidas avancadas",
        [
            md(
                """
                # Aula06 - Orientacao e saidas avancadas

                O `pytesseract` tambem oferece funcoes alem de `image_to_string()`.

                Nesta aula vamos ver:

                - `image_to_osd()` para orientacao
                - `image_to_pdf_or_hocr()` para gerar saidas reutilizaveis
                """
            ),
            code(
                """
                from pathlib import Path  # Importa Path para salvar arquivos gerados.
                from PIL import Image, ImageDraw  # Importa classes para criar uma imagem de exemplo.
                import pytesseract  # Importa a biblioteca de OCR.

                imagem = Image.new("RGB", (500, 150), "white")  # Cria uma imagem de exemplo para as funcoes avancadas.
                desenho = ImageDraw.Draw(imagem)  # Cria o objeto de desenho associado a imagem.
                desenho.text((20, 60), "Relatorio anual", fill="black")  # Escreve um texto simples na imagem.

                orientacao = pytesseract.image_to_osd(imagem)  # Pede informacoes de orientacao e script detectado.

                print(orientacao)  # Mostra o texto bruto retornado pela analise de orientacao.
                """
            ),
            code(
                """
                from pathlib import Path  # Importa Path para salvar o arquivo PDF gerado.
                from PIL import Image, ImageDraw  # Importa novamente as classes para um exemplo independente.
                import pytesseract  # Importa novamente a biblioteca de OCR.

                imagem = Image.new("RGB", (500, 150), "white")  # Cria outra imagem branca para o exemplo de saida PDF.
                desenho = ImageDraw.Draw(imagem)  # Cria o objeto de desenho da imagem.
                desenho.text((20, 60), "Relatorio anual", fill="black")  # Escreve o texto que sera transformado em PDF pesquisavel.

                pdf_bytes = pytesseract.image_to_pdf_or_hocr(imagem, extension="pdf")  # Gera um PDF em formato de bytes a partir da imagem.
                caminho_saida = Path("pytesseract/saida_exemplo.pdf")  # Define o caminho do arquivo de saida.

                caminho_saida.write_bytes(pdf_bytes)  # Salva no disco o PDF gerado pelo OCR.
                print(caminho_saida)  # Mostra onde o arquivo foi salvo.
                """
            ),
            md(
                """
                ## O que o retorno representa

                - `image_to_osd()` devolve um texto com dados de orientacao
                - `image_to_pdf_or_hocr()` devolve bytes

                Bytes significam dados brutos que ainda precisam ser salvos em um arquivo para virar PDF ou hOCR utilizavel.
                """
            ),
        ],
    )


def build_pdf2image_course() -> None:
    folder = ROOT / "pdf2image"

    write_text(
        folder / "README.md",
        """
        # Modulo: pdf2image

        `pdf2image` transforma paginas de um PDF em imagens.
        Isso e muito util quando voce quer:

        - visualizar paginas separadas
        - salvar cada pagina como PNG ou JPEG
        - preparar um PDF para OCR

        ## Antes de estudar este modulo

        Voce precisa:

        - instalar `pdf2image`
        - instalar `Pillow`
        - instalar Poppler no Windows

        ## O que voce vai aprender

        - uso basico de `convert_from_path`
        - parametros como `dpi`, `first_page`, `last_page` e `fmt`
        - salvamento das paginas
        - conversao a partir de bytes
        - uso de `output_folder`, `paths_only`, `thread_count` e `grayscale`
        - integracao com OCR

        ## Ordem sugerida

        1. `Aula01 - Instalacao e convert_from_path.ipynb`
        2. `Aula02 - DPI, paginas e formatos.ipynb`
        3. `Aula03 - Salvando paginas e preparando para OCR.ipynb`
        4. `Aula04 - Script para converter PDF em imagens.py`
        5. `Aula05 - convert_from_bytes e leitura em memoria.ipynb`
        6. `Aula06 - Parametros uteis e integracao com OCR.ipynb`
        """,
    )

    write_notebook(
        folder / "Aula01 - Instalacao e convert_from_path.ipynb",
        "Aula01 - Instalacao e convert_from_path",
        [
            md(
                """
                # Aula01 - Instalacao e convert_from_path

                A funcao mais famosa da biblioteca `pdf2image` e `convert_from_path`.

                O que ela faz:

                - recebe o caminho de um PDF
                - le as paginas do documento
                - devolve uma lista de imagens Pillow

                Isso quer dizer que cada pagina vira um objeto de imagem que pode ser exibido, salvo ou enviado para OCR.
                """
            ),
            md(
                """
                ## Funcao: `convert_from_path()`

                Parametros comuns:

                - `pdf_path`: caminho do arquivo PDF
                - `dpi`: qualidade da imagem gerada
                - `first_page`: pagina inicial
                - `last_page`: pagina final
                - `fmt`: formato da imagem em memoria
                - `poppler_path`: caminho da instalacao do Poppler no Windows
                """
            ),
            code(
                """
                from pdf2image import convert_from_path  # Importa a funcao principal que converte PDF em lista de imagens.

                caminho_pdf = "pdf2image/exemplo.pdf"  # Define o caminho do PDF que sera convertido.
                caminho_poppler = r"C:\\poppler\\Library\\bin"  # Define um exemplo de caminho onde o Poppler pode estar instalado no Windows.

                paginas = convert_from_path(  # Inicia a chamada da funcao que vai ler o PDF e criar imagens.
                    caminho_pdf,  # Envia o caminho do arquivo PDF que sera aberto.
                    dpi=200,  # Define uma resolucao intermediaria para gerar imagens com boa legibilidade.
                    poppler_path=caminho_poppler,  # Informa onde o pdf2image encontra os executaveis do Poppler no Windows.
                )  # Fecha a chamada da funcao principal.

                print(len(paginas))  # Mostra quantas paginas foram convertidas em imagens.
                print(type(paginas))  # Mostra o tipo do retorno para reforcar que a funcao devolve uma lista.
                """
            ),
            md(
                """
                ## O que o retorno representa

                O retorno de `convert_from_path` e uma lista.
                Cada item dessa lista e uma imagem Pillow.

                Isso permite:

                - exibir a pagina
                - salvar a pagina
                - editar a pagina
                - enviar a pagina para OCR
                """
            ),
        ],
    )

    write_notebook(
        folder / "Aula02 - DPI, paginas e formatos.ipynb",
        "Aula02 - DPI, paginas e formatos",
        [
            md(
                """
                # Aula02 - DPI, paginas e formatos

                Agora vamos entender parametros que influenciam fortemente no resultado.

                Os mais importantes para iniciantes costumam ser:

                - `dpi`
                - `first_page`
                - `last_page`
                - `fmt`
                """
            ),
            code(
                """
                from pdf2image import convert_from_path  # Importa a funcao usada para converter PDF em imagens.

                caminho_pdf = "pdf2image/exemplo.pdf"  # Define o PDF que sera usado no exemplo.
                caminho_poppler = r"C:\\poppler\\Library\\bin"  # Define o caminho do Poppler em um exemplo de instalacao no Windows.

                paginas = convert_from_path(  # Chama a funcao principal com mais parametros de controle.
                    caminho_pdf,  # Passa o caminho do PDF que sera lido.
                    dpi=300,  # Pede uma resolucao maior para melhorar a nitidez da pagina convertida.
                    first_page=1,  # Diz que a leitura deve comecar na pagina 1.
                    last_page=2,  # Diz que a leitura deve terminar na pagina 2.
                    fmt="png",  # Define que o formato interno desejado e PNG.
                    poppler_path=caminho_poppler,  # Informa o caminho do Poppler para a biblioteca funcionar no Windows.
                )  # Finaliza a chamada da funcao.

                print(len(paginas))  # Mostra quantas paginas entraram na conversao.
                """
            ),
            md(
                """
                ## Como pensar no `dpi`

                - `dpi` baixo: imagem mais leve, mas menos nitida
                - `dpi` medio: equilibrio razoavel
                - `dpi` alto: melhor leitura, mas arquivos maiores

                Para muitos casos de OCR, `200` ou `300` DPI sao bons pontos de partida.
                """
            ),
            code(
                """
                from pdf2image import convert_from_path  # Importa novamente a funcao para um exemplo independente.

                caminho_pdf = "pdf2image/exemplo.pdf"  # Define novamente o arquivo PDF de entrada.
                caminho_poppler = r"C:\\poppler\\Library\\bin"  # Define novamente o caminho do Poppler.

                paginas = convert_from_path(  # Inicia outra conversao com foco em apenas uma pagina.
                    caminho_pdf,  # Informa o PDF de origem.
                    first_page=1,  # Escolhe a primeira pagina como inicio da leitura.
                    last_page=1,  # Limita a conversao a apenas uma unica pagina.
                    dpi=250,  # Define uma resolucao suficiente para boa leitura.
                    poppler_path=caminho_poppler,  # Informa onde o Poppler esta instalado.
                )  # Fecha a chamada.

                primeira_pagina = paginas[0]  # Pega a primeira imagem da lista retornada.

                primeira_pagina  # Exibe a primeira pagina convertida dentro do notebook.
                """
            ),
        ],
    )

    write_notebook(
        folder / "Aula03 - Salvando paginas e preparando para OCR.ipynb",
        "Aula03 - Salvando paginas e preparando para OCR",
        [
            md(
                """
                # Aula03 - Salvando paginas e preparando para OCR

                Nesta aula voce vai pegar as imagens geradas pelo `pdf2image` e salva-las no disco.

                Esta etapa e muito importante quando:

                - voce quer guardar cada pagina separadamente
                - voce quer inspecionar visualmente as paginas
                - voce quer mandar as imagens para OCR depois
                """
            ),
            code(
                """
                from pathlib import Path  # Importa Path para criar e montar caminhos com mais clareza.
                from pdf2image import convert_from_path  # Importa a funcao que gera as imagens a partir do PDF.

                caminho_pdf = "pdf2image/exemplo.pdf"  # Define o arquivo PDF de entrada.
                caminho_poppler = r"C:\\poppler\\Library\\bin"  # Define o caminho do Poppler no Windows.
                pasta_saida = Path("pdf2image/paginas_convertidas")  # Define a pasta onde as imagens serao salvas.

                pasta_saida.mkdir(parents=True, exist_ok=True)  # Cria a pasta de saida caso ela ainda nao exista.

                paginas = convert_from_path(  # Converte o PDF em uma lista de imagens.
                    caminho_pdf,  # Informa qual PDF deve ser lido.
                    dpi=300,  # Usa boa resolucao para facilitar leitura humana e OCR.
                    poppler_path=caminho_poppler,  # Informa onde estao os binarios do Poppler.
                )  # Fecha a chamada da funcao.

                for indice, pagina in enumerate(paginas, start=1):  # Percorre cada imagem gerada junto com um numero de pagina.
                    caminho_imagem = pasta_saida / f"pagina_{indice}.png"  # Monta o nome do arquivo de saida da pagina atual.
                    pagina.save(caminho_imagem, "PNG")  # Salva a imagem atual no disco em formato PNG.
                    print(f"Pagina salva em: {caminho_imagem}")  # Mostra no console onde a pagina foi salva.
                """
            ),
            md(
                """
                ## Integracao com OCR

                Depois de salvar as paginas como imagens, voce pode:

                - abrir cada uma com Pillow
                - enviar para `pytesseract.image_to_string()`
                - extrair o texto de documentos escaneados
                """
            ),
        ],
    )

    write_text(
        folder / "Aula04 - Script para converter PDF em imagens.py",
        """
        from pathlib import Path  # Importa Path para montar caminhos de arquivos e pastas com clareza.
        from pdf2image import convert_from_path  # Importa a funcao que converte PDF em imagens Pillow.


        CAMINHO_PDF = Path("pdf2image/exemplo.pdf")  # Define o caminho do PDF que sera convertido.
        PASTA_SAIDA = Path("pdf2image/paginas_convertidas")  # Define a pasta onde as imagens resultantes serao salvas.
        CAMINHO_POPPLER = r"C:\\poppler\\Library\\bin"  # Define um caminho de exemplo para os binarios do Poppler no Windows.


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
        """,
    )

    write_notebook(
        folder / "Aula05 - convert_from_bytes e leitura em memoria.ipynb",
        "Aula05 - convert_from_bytes e leitura em memoria",
        [
            md(
                """
                # Aula05 - convert_from_bytes e leitura em memoria

                Alem de `convert_from_path()`, a biblioteca tambem oferece `convert_from_bytes()`.

                Esta funcao e util quando o PDF ja esta em memoria, por exemplo:

                - quando ele veio de uma API
                - quando foi baixado da internet
                - quando foi lido como bytes de um banco ou arquivo
                """
            ),
            code(
                """
                from pathlib import Path  # Importa Path para ler o arquivo PDF como bytes.
                from pdf2image import convert_from_bytes  # Importa a funcao que converte PDF em memoria para imagens.

                caminho_pdf = Path("pdf2image/exemplo.pdf")  # Define o caminho do PDF que sera lido como bytes.
                caminho_poppler = r"C:\\poppler\\Library\\bin"  # Define o caminho do Poppler no Windows.

                dados_pdf = caminho_pdf.read_bytes()  # Le o conteudo bruto do PDF e guarda em bytes.
                paginas = convert_from_bytes(dados_pdf, dpi=200, poppler_path=caminho_poppler)  # Converte os bytes do PDF em imagens Pillow.

                print(type(dados_pdf))  # Mostra o tipo do objeto que representa o PDF em memoria.
                print(len(paginas))  # Mostra quantas paginas foram convertidas.
                """
            ),
            md(
                """
                ## O que o objeto `bytes` representa

                `bytes` sao dados brutos em memoria.
                Eles nao sao ainda uma imagem pronta nem um texto pronto.

                `convert_from_bytes()` pega esses dados brutos e devolve uma lista de imagens Pillow.
                """
            ),
        ],
    )

    write_notebook(
        folder / "Aula06 - Parametros uteis e integracao com OCR.ipynb",
        "Aula06 - Parametros uteis e integracao com OCR",
        [
            md(
                """
                # Aula06 - Parametros uteis e integracao com OCR

                Nesta aula vamos ver alguns parametros uteis para fluxos mais reais.

                Exemplos:

                - `output_folder`
                - `paths_only`
                - `thread_count`
                - `grayscale`
                """
            ),
            code(
                """
                from pathlib import Path  # Importa Path para criar a pasta de saida.
                from pdf2image import convert_from_path  # Importa a funcao de conversao por caminho.

                caminho_pdf = "pdf2image/exemplo.pdf"  # Define o PDF de entrada.
                caminho_poppler = r"C:\\poppler\\Library\\bin"  # Define o caminho do Poppler no Windows.
                pasta_temporaria = Path("pdf2image/saida_temporaria")  # Define a pasta que recebera os arquivos temporarios.

                pasta_temporaria.mkdir(parents=True, exist_ok=True)  # Cria a pasta temporaria se ela ainda nao existir.

                caminhos = convert_from_path(  # Converte o PDF usando parametros mais voltados a fluxo real.
                    caminho_pdf,  # Informa o arquivo PDF de entrada.
                    dpi=300,  # Usa boa resolucao para preservar a legibilidade.
                    grayscale=True,  # Pede imagens em escala de cinza.
                    thread_count=2,  # Permite mais de uma thread de trabalho na conversao.
                    output_folder=str(pasta_temporaria),  # Define a pasta onde os arquivos temporarios serao gravados.
                    paths_only=True,  # Pede para a funcao devolver apenas os caminhos dos arquivos gerados.
                    poppler_path=caminho_poppler,  # Informa onde estao os binarios do Poppler.
                )  # Fecha a chamada da funcao.

                print(caminhos)  # Mostra a lista de caminhos gerados pela conversao.
                print(type(caminhos))  # Mostra o tipo do retorno.
                """
            ),
            md(
                """
                ## Como isso se conecta com OCR

                Uma estrategia comum e:

                1. converter o PDF em imagens
                2. salvar ou receber os caminhos dessas imagens
                3. enviar cada imagem para `pytesseract`

                Assim, `pdf2image` cuida da conversao do PDF e `pytesseract` cuida da leitura do texto.
                """
            ),
        ],
    )


def main() -> None:
    build_root_files()
    build_os_course()
    build_re_course()
    build_pytesseract_course()
    build_pdf2image_course()


if __name__ == "__main__":
    main()
