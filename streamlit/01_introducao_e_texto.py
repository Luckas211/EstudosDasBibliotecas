# streamlit/01_introducao_e_texto.py

"""
Aula 1: Introdução ao Streamlit e Exibição de Texto

Bem-vindo à sua primeira aplicação com Streamlit!

O Streamlit transforma scripts de dados em aplicações web compartilháveis em minutos.
Tudo em Python puro. Sem necessidade de experiência com front-end.

Nesta aula, vamos aprender os comandos básicos para exibir informações na tela.

Para executar este arquivo:
1. Salve o código como `01_introducao_e_texto.py`.
2. Abra o terminal na pasta onde você salvou o arquivo.
3. Execute o comando: streamlit run 01_introducao_e_texto.py
"""

# Importa a biblioteca Streamlit e a apelida como 'st' para facilitar o uso.
import streamlit as st

# --- Títulos e Cabeçalhos ---

# st.title() é usado para o título principal da sua aplicação.
# Geralmente, você usará isso apenas uma vez no topo da página.
st.title("Minha Primeira Aplicação Streamlit")

# st.header() é usado para seções principais da sua página.
st.header("Aula 1: Comandos de Texto")

# st.subheader() é para subseções.
st.subheader("Introdução aos elementos de texto básicos")

# --- Texto Simples e Formatação ---

# st.write() é o comando "mágico" do Streamlit.
# Ele pode exibir quase tudo: texto, números, DataFrames do Pandas, gráficos, etc.
st.write("Olá, mundo! Bem-vindo ao Streamlit.")
st.write("Este é um texto simples exibido com `st.write()`.")

# st.text() é usado para exibir texto simples, sem formatação.
# É ideal para exibir texto de largura fixa ou código.
st.text("Este texto é exibido com st.text(), que não aplica formatação.")

# --- Markdown ---

# st.markdown() permite que você escreva em formato Markdown,
# o que é ótimo para formatar texto, criar listas, links e muito mais.
st.subheader("Usando Markdown")
st.markdown("""
O Markdown é uma forma leve de adicionar formatação a textos.

**Recursos do Markdown:**
- **Negrito** (`**Negrito**`)
- *Itálico* (`*Itálico*`)
- `Código` (`` `Código` ``)
- Listas:
  - Item 1
  - Item 2
- Links: Documentação Oficial do Streamlit
---
""")

# --- Elementos Especiais ---

# st.success(), st.info(), st.warning(), st.error() são caixas coloridas
# para destacar mensagens importantes.
st.subheader("Caixas de Mensagem")
st.success("Operação concluída com sucesso!")
st.info("Esta é uma mensagem informativa.")
st.warning("Atenção: esta ação pode ter consequências.")
st.error("Ocorreu um erro ao processar a solicitação.")

# st.code() é usado para exibir blocos de código com destaque de sintaxe.
st.subheader("Exibindo Blocos de Código")
st.code("""
# Exemplo de código em Python
def ola_streamlit():
    print("Olá, Streamlit!")
""", language="python")

st.write("Fim da Aula 1. Experimente alterar este arquivo e veja as mudanças na sua aplicação!")
