# ==========================================================================
# DESAFIO FINAL: SISTEMA DE GERENCIAMENTO DE TAREFAS (TO-DO LIST) COM CRUD
# ==========================================================================

"""
OBJETIVO DO DESAFIO:
Sua missão é criar um programa de linha de comando (CLI) que permita ao 
usuário gerenciar suas tarefas diárias. Todos os dados devem ser salvos 
permanentemente utilizando o banco de dados SQLite.

REQUISITOS (O CRUD Completo):

1. CREATE (Criar Banco e Tabela):
   O programa deve criar automaticamente um banco chamado 'tarefas.db'.
   Crie uma tabela 'tarefas' com os campos:
   - id (INTEGER PRIMARY KEY AUTOINCREMENT)
   - titulo (TEXT NOT NULL)
   - descricao (TEXT)
   - status (TEXT DEFAULT 'pendente')

2. INSERT (Adicionar):
   Uma função para o usuário adicionar uma nova tarefa informando o título e descrição.

3. READ (Ler):
   Uma função que busca no banco e imprime todas as tarefas cadastradas,
   mostrando o ID, título e se está pendente ou concluída.

4. UPDATE (Atualizar):
   Uma função que recebe o ID de uma tarefa e altera o 'status' dela para 'concluída'.

5. DELETE (Deletar):
   Uma função que recebe o ID de uma tarefa e a remove completamente do banco.

DESAFIOS EXTRAS (Para ir além!):
- Tratar erros (Ex: E se o usuário digitar uma letra na hora de informar o ID?)
- Função extra de listagem: Mostrar apenas as tarefas que estão 'pendentes'.
"""

import sqlite3

NOME_BANCO = 'tarefas.db'

# 1. Função para conectar e criar a tabela (Executada ao iniciar o app)
def inicializar_banco():
    conn = sqlite3.connect(NOME_BANCO)  # Conecta ou cria o banco de dados
    cursor = conn.cursor()  # Cria um cursor para executar comandos SQL
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            status TEXT DEFAULT 'pendente'
        )
    """)  # Cria a tabela 'tarefas' se ela não existir
    conn.commit()  # Salva as alterações no banco
    conn.close()  # Fecha a conexão
    print("Banco de dados e tabela inicializados com sucesso!")  # Mensagem de sucesso

# 2. Função para adicionar tarefa (CREATE)
def adicionar_tarefa(titulo, descricao):
    conn = sqlite3.connect(NOME_BANCO)  # Conecta ao banco
    cursor = conn.cursor()  # Obtém o cursor
    cursor.execute("INSERT INTO tarefas (titulo, descricao) VALUES (?, ?)", (titulo, descricao))  # Insere a nova tarefa
    conn.commit()  # Confirma a transação
    conn.close()  # Fecha a conexão
    print(f"Tarefa '{titulo}' adicionada com sucesso!")  # Mensagem de confirmação

# 3. Função para listar tarefas (READ)
def listar_tarefas():
    conn = sqlite3.connect(NOME_BANCO)  # Conecta ao banco
    cursor = conn.cursor()  # Obtém o cursor
    cursor.execute("SELECT id, titulo, status FROM tarefas")  # Seleciona todas as tarefas
    tarefas = cursor.fetchall()  # Busca todos os resultados
    conn.close()  # Fecha a conexão

    if not tarefas:  # Verifica se há tarefas
        print("Nenhuma tarefa cadastrada.")  # Informa se não houver tarefas
        return  # Sai da função

    for tarefa in tarefas:  # Itera sobre cada tarefa
        id_tarefa, titulo, status = tarefa  # Desempacota os dados da tarefa
        print(f"ID: {id_tarefa}, Título: {titulo}, Status")
              

# 4. Função para marcar tarefa como concluída (UPDATE)
def concluir_tarefa(id_tarefa):
    pass

# 5. Função para deletar tarefa (DELETE)
def deletar_tarefa(id_tarefa):
    pass


# ================================================
# MENU INTERATIVO (Já estruturado para você focar no banco!)
# ================================================
def menu():
    inicializar_banco()
    
    while True:
        print("\n" + "="*30)
        print("   GERENCIADOR DE TAREFAS   ")
        print("="*30)
        print("1. Adicionar Nova Tarefa")
        print("2. Listar Todas as Tarefas")
        print("3. Concluir Tarefa")
        print("4. Deletar Tarefa")
        print("5. Sair do Programa")
        
        opcao = input("\nEscolha uma opção (1-5): ")
        
        if opcao == '1':
            titulo = input("Título da tarefa: ")
            descricao = input("Descrição detalhada: ")
            adicionar_tarefa(titulo, descricao)
            
        elif opcao == '2':
            print("\n--- Suas Tarefas ---")
            listar_tarefas()
            
        elif opcao == '3':
            try:
                id_t = int(input("Digite o ID da tarefa para concluir: "))
                concluir_tarefa(id_t)
            except ValueError:
                print("Por favor, digite um número válido para o ID.")
                
        elif opcao == '4':
            try:
                id_t = int(input("Digite o ID da tarefa para deletar: "))
                deletar_tarefa(id_t)
            except ValueError:
                print("Por favor, digite um número válido para o ID.")
                
        elif opcao == '5':
            print("Encerrando o gerenciador. Até mais!")
            break
            
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    # Descomente a linha abaixo quando quiser testar seu programa no terminal!
    # menu()
    pass
