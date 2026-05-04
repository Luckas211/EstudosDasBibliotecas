import streamlit as st
import sqlite3
import re


class BancoDeDados:
    def __init__(self, nome_banco="usuarios.db"):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()


    def criar_tabela(self):
        try:
            self.cursor.execute(""" CREATE TABLE IF NOT EXISTS usuarios (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL,
                                telefone TEXT NOT NULL,
                                data_nascimento TEXT NOT NULL,
                                email TEXT NOT NULL
                                )
    """)
            self.conexao.commit()
        except sqlite3.Error as e:
            st.error(f"Erro ao criar tabela: {e}")


    def inserir_dados(self, nome,telefone,data_nascimento, email):
        try:
            self.cursor.execute("INSERT INTO usuarios (nome,telefone,data_nascimento,email) VALUES (?,?,?,?)", (nome,telefone,data_nascimento, email))
            self.conexao.commit()
        except sqlite3.Error as e:
            st.error(f"Erro ao inserir dados: {e}")
    
    def listar_dados(self):
        try:
            self.cursor.execute("SELECT * FROM usuarios")
            return self.cursor.fetchall()

        except sqlite3.Error as e:
            st.error(f"Erro ao listar dados: {e}")

    def atualizar_dados(self, id,nome,telefone,data_nascimento, email):
        try:
            self.cursor.execute("UPDATE usuarios SET nome=?, telefone=?, data_nascimento=?, email=? WHERE id=?", (nome,telefone,data_nascimento,email,id))
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


    def validar_email(self, email):
        padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(padrao_email, email)


    def validar_data(self, data):
        padrao_data = r'^\d{2}/\d{2}/\d{4}$'
        return re.match(padrao_data, data)


    def validar_telefone(self, telefone):
        padrao_tel = r'^\d{10,11}$'  # Ex: 11999999999
        return re.match(padrao_tel, telefone)
    
    
    def pagina_inicial(self):
        titulo = st.title("Cadastro de Usuários", text_alignment="center")
        opcoes_menu = ["Formulário de Cadastro", "Listar Usuários", "Atualizar Usuário", "Excluir Usuário"]
        navegacao = st.tabs(opcoes_menu)

        with navegacao[0]:
            self.formulario()

        with navegacao[1]:
            self.listar_usuarios()
        
        with navegacao[2]:
            self.atualizar_usuarios()
            
        with navegacao[3]:
            self.excluir_usuarios()
            
        


    def menu_lateral(self):
        st.sidebar.title("📌 Sistema CRUD")

        st.sidebar.markdown("---")

        # 👤 Autor
        st.sidebar.subheader("👤 Desenvolvedor")
        st.sidebar.write("Lucas da Conceição Silva")
        st.sidebar.markdown("---")






        # 📖 Sobre
        st.sidebar.subheader("📖 Sobre o projeto")
        st.sidebar.write(
            "Projeto de estudo para praticar CRUD com Python, SQLite e Streamlit, "
            "com foco em manipulação de dados e validação de entradas."
        )

        st.sidebar.markdown("---")

        # 🔍 Regex (parte nova 🔥)
        st.sidebar.subheader("🔍 Validações com Regex")

        st.sidebar.write("📧 Email:")
        st.sidebar.code(r'^[\w\.-]+@[\w\.-]+\.\w+$')

        st.sidebar.write("📞 Telefone:")
        st.sidebar.code(r'^\d{10,11}$')

        st.sidebar.write("📅 Data de nascimento:")
        st.sidebar.code(r'^\d{2}/\d{2}/\d{4}$')

        st.sidebar.markdown("---")

        # 🧠 Explicação simples
        st.sidebar.subheader("🧠 Como funciona")
        st.sidebar.write(
            "Regex (expressões regulares) são padrões usados para validar textos. "
            "Neste projeto, são utilizadas para garantir que os dados inseridos "
            "sigam formatos corretos antes de serem salvos no banco."
        )

        st.sidebar.markdown("---")


        st.sidebar.markdown("---")
        st.sidebar.subheader("📬 Contato")

        st.sidebar.write("📧 Email: lucas_rj211@hotmail.com")

        st.sidebar.caption("Projeto educacional 🚀")
        
        




    def formulario(self):
        st.subheader("Cadastro de usuário")

        with st.form("form"):
            nome = st.text_input("Nome")
            telefone = st.text_input("Telefone (somente números)")
            email = st.text_input("Email")
            data = st.text_input("Data de nascimento (dd/mm/aaaa)")

            btn = st.form_submit_button("Cadastrar")

        if btn:
            if nome and telefone and email and data:

                if not self.validar_email(email):
                    st.error("Email inválido")
                    return

                if not self.validar_data(data):
                    st.error("Data inválida. Use dd/mm/aaaa")
                    return

                if not self.validar_telefone(telefone):
                    st.error("Telefone inválido")
                    return

                self.banco.inserir_dados(nome, telefone, email, data)
                st.success("Cadastrado com sucesso!")

            else:
                st.error("Preencha todos os campos")


    def listar_usuarios(self):
        st.subheader("Lista de usuários")
        usuarios = self.banco.listar_dados()

        if usuarios != None:
            tabela = []
            for usuario in usuarios:
                tabela.append({
                    "ID": usuario[0],
                    "Nome": usuario[1],
                    "telefone": usuario[2],
                    "Data de nascimento": usuario[3],
                    "Email": usuario[4]
                })
            st.table(tabela)
            st.success(f"Temos um total de {len(usuarios)} usuários cadastrados.")
        else:
            st.info("Nenhum usuário cadastrado")
                
                
    def atualizar_usuarios(self):
        st.subheader("Atualizar usuário")
        usuarios = self.banco.listar_dados()

        if usuarios:
            opcoes_usuario = {}
            for usuario in usuarios:
                chave = f"ID: {usuario[0]} - {usuario[1]}"
                valor = usuario[0]
                
                opcoes_usuario[chave] = valor

            usuario_selecionado = st.selectbox(
                "Selecione o usuário",
                list(opcoes_usuario.keys())
            )

            id_usuario = opcoes_usuario[usuario_selecionado]
            
            nome = st.text_input("Novo nome")
            telefone = st.text_input("Novo telefone")
            data = st.text_input("Nova data de nascimento (dd/mm/aaaa)")
            email = st.text_input("Novo email")

            if st.button("Atualizar"):
                if nome and telefone and email and data:

                    if not self.validar_email(email):
                        st.error("Email inválido")
                        return

                    if not self.validar_data(data):
                        st.error("Data inválida")
                        return

                    if not self.validar_telefone(telefone):
                        st.error("Telefone inválido")
                        return

                    self.banco.atualizar_dados(id_usuario, nome, telefone, data, email)
                    st.success("Atualizado com sucesso!")
                else:
                    st.error("Preencha todos os campos")
            
            
    def excluir_usuarios(self):
        st.subheader("Excluir usuário")
        usuarios = self.banco.listar_dados()

        if usuarios:
            opcoes_usuario = {}

            for usuario in usuarios:
                chave = f"{usuario[1]} (ID: {usuario[0]})"
                valor = usuario[0]
                opcoes_usuario[chave] = valor

            usuario_selecionado = st.selectbox(
                "Selecione o usuário para excluir",
                list(opcoes_usuario.keys())
            )

            id_usuario = opcoes_usuario[usuario_selecionado]

            st.warning("⚠️ Essa ação não pode ser desfeita!")

            if st.button("Excluir"):
                try:
                    self.banco.excluir_dados(id_usuario)
                    st.success("Usuário excluído com sucesso!")
                except Exception as e:
                    st.error(f"Erro ao excluir usuário: {e}")
        else:
            st.info("Nenhum usuário cadastrado.")
                

        




if __name__ == "__main__":
    app = App()
    app.pagina_inicial()
    app.menu_lateral()
    

