import streamlit as st
import sqlite3


class BancoDeDados:
    def __init__(self, nome_banco="usuarios.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()


    def criar_tabela(self):
        try:
            self.cursor.execute(""" CREATE TABLE IF NOT EXISTS usuarios (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL,
                                idade INTEGER NOT NULL,
                                email TEXT NOT NULL
                                )
    """)
            self.conexao.commit()
        except sqlite3.Error as e:
            st.error(f"Erro ao criar tabela: {e}")


    def inserir_dados(self, nome,idade, email):
        try:
            self.cursor.execute("INSERT INTO usuarios (nome,idade,email) VALUES (?,?,?)", (nome,idade,email))
            self.conexao.commit()
        except sqlite3.Error as e:
            st.error(f"Erro ao inserir dados: {e}")
    
    def listar_dados(self):
        try:
            self.cursor.execute("SELECT * FROM usuarios")
            return self.cursor.fetchall()

        except sqlite3.Error as e:
            st.error(f"Erro ao listar dados: {e}")

    def atualizar_dados(self, id,nome,idade, email):
        try:
            self.cursor.execute("UPDATE usuarios SET nome=?, idade=?, email=? WHERE id=?", (nome,idade,email,id))
            self.conexao.commit()
        except sqlite3.Error as e:
            st.error(f"Erro ao atualizar dados: {e}")

    def excluir_dados(self, id):
        try:
            self.cursor.execute("DELETE FROM usuarios WHERE id=?", (id,))
            self.conexao.commit()
        except sqlite3.Error as e:
            st.error(f"Erro ao excluir dados: {e}")

    def fechar_conexao(self):
        self.conexao.close()






class App:
    def __init__(self):
        self.banco = BancoDeDados()
        self.banco.criar_tabela()


    def pagina_inicial(self):
        titulo = st.title("Cadastro de Usuários", text_alignment="center")
        menu_lateral = st.sidebar.subheader("Menu de navegação",text_alignment="center")
        opcoes_menu = ["Formulário de Cadastro", "Listar Usuários", "Atualizar Usuário", "Excluir Usuário"]
        navegacao = st.tabs(opcoes_menu)

        with navegacao[0]:
            self.formulario()

        with navegacao[1]:
            self.listar_usuarios()







    def formulario(self):
        st.subheader("Formulário de cadastro", text_alignment="center")
        with st.form("formulario_cadastro"):
            nome = st.text_input("nome")
            idade = st.number_input("idade", min_value=0,max_value=120, step=1)
            email = st.text_input("email")
            submit_button = st.form_submit_button("Cadastrar")

        if submit_button:
            try:
                if nome and email and idade:
                    self.banco.inserir_dados(nome,idade,email)
                    st.success("Usuário cadastrado com sucesso!")
                else:
                    st.error("Por favor, preencha todos os campos.")
            except Exception as e:
                st.error(f"Erro ao cadastrar usuário: {e}")


    def listar_usuarios(self):
        st.subheader("Lista de usuários")
        usuarios = self.banco.listar_dados()

        if usuarios:
            tabela = []
            for usuario in usuarios:
                tabela.append({
                    "ID": usuario[0],
                    "Nome": usuario[1],
                    "Idade": usuario[2],
                    "Email": usuario[3]
                })

            st.table(tabela)
        else:
            st.info("Nenhum usuário cadastrado.")
        




if __name__ == "__main__":
    app = App()
    app.pagina_inicial()
