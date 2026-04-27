import streamlit as st
import re

class App():
    def __init__(self, titulo):
        self.titulo = titulo

        self.padrao_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        self.padrao_telefone = r"\(\d{2}\) \d{5}-\d{4}"
        self.padrao_cpf = r"\d{3}\.\d{3}\.\d{3}-\d{2}"
        self.padrao_cep = r"\d{5}-\d{3}"

    def home(self):
        st.set_page_config(page_title=self.titulo, layout="wide")

        st.title(self.titulo)
        st.subheader("Bem-vindo ao Coletor de Dados")
        st.divider()

    def menu_lateral(self):
        st.sidebar.subheader("👨‍💻 Informações")
        st.sidebar.caption("Projeto de estudo focado em Regex e extração de dados")

        st.sidebar.divider()

        st.sidebar.markdown("🔗 **Links:**")
        st.sidebar.markdown("📧 Email: Lucas_rj211@hotmail.com")
        st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/lucas-silva-41290532a/)")
        st.sidebar.markdown("[GitHub](https://github.com/luckas211)")

    def abas(self):
        aba1, aba2 = st.tabs(["🔍 Coletor", "📘 Sobre o estudo"])

        with aba1:
            self.usuario()

        with aba2:
            self.sobre_estudo()

    def usuario(self):
        st.write("Insira um texto para coletar os dados:")
        texto = st.text_area("Digite o texto aqui", height=200)

        if st.button("Coletar Dados"):
            self.coletar_dados(texto)

    def coletar_dados(self, texto):
        emails = re.findall(self.padrao_email, texto)
        telefones = re.findall(self.padrao_telefone, texto)
        cpfs = re.findall(self.padrao_cpf, texto)
        ceps = re.findall(self.padrao_cep, texto)

        st.subheader("Resultados")

        st.write("E-mails encontrados:", emails)
        st.write("Telefones encontrados:", telefones)
        st.write("CPF's encontrados:", cpfs)
        st.write("CEP's encontrados:", ceps)

        st.divider()

        if any([emails, telefones, cpfs, ceps]):
            st.success("Coleta finalizada com sucesso!")
        else:
            st.warning("Nenhum dado encontrado.")

    def sobre_estudo(self):
        st.subheader("📌 Contexto do Estudo")

        st.write("""
Recentemente, tive a necessidade de aplicar automação em um processo interno na empresa onde atuo. 
O fluxo envolvia a leitura de documentos em formato PDF, extração de informações e organização desses dados.

Durante esse processo, identifiquei um gargalo: a coleta manual de dados estava tornando o processo lento, repetitivo e sujeito a erros.

🔍 **Solução aplicada**
- Regex (re)
- pytesseract
- pdf2image
- os

💡 **Aprendizado**
O uso de Regex permitiu identificar padrões dentro de grandes volumes de texto não estruturado, automatizando tarefas manuais.

🚀 **Resultado**
Redução de tempo, aumento de precisão e melhoria no fluxo de trabalho.

📈 **Evolução**
Este projeto foi criado para consolidar esse aprendizado de forma visual e interativa.
""")

if __name__ == "__main__":
    app = App("Coletor de Dados")
    app.home()
    app.menu_lateral()
    app.abas()