# streamlit/03_layout_e_organizacao.py

"""
Aula 3: Layout e Organização

À medida que suas aplicações crescem, é importante organizar os elementos
de forma clara e intuitiva. O Streamlit oferece várias ferramentas para isso.

Nesta aula, vamos aprender a usar:
- Barra Lateral (Sidebar)
- Colunas
- Expansor (Expander)

Para executar este arquivo:
streamlit run 03_layout_e_organizacao.py
"""

import streamlit as st

st.set_page_config(layout="wide") # Usa a largura total da página

st.title("Aula 3: Layout e Organização")

# --- Barra Lateral (Sidebar) ---
# Para adicionar um elemento à barra lateral, basta usar `st.sidebar.`
# antes de qualquer comando do Streamlit (ex: st.sidebar.write, st.sidebar.button).

st.sidebar.header("Barra Lateral")
st.sidebar.write("A barra lateral é ideal para colocar filtros e configurações.")

# Vamos adicionar alguns widgets da aula anterior na barra lateral.
opcao_sidebar = st.sidebar.selectbox(
    "Escolha uma opção na sidebar:",
    ["Opção A", "Opção B", "Opção C"]
)

st.sidebar.write(f"Você escolheu a **{opcao_sidebar}** na barra lateral.")

# O conteúdo principal da página continua sendo criado com `st.`
st.header("Conteúdo Principal")
st.write("Qualquer comando sem `st.sidebar` aparece na área principal da página.")
st.info(f"A opção selecionada na barra lateral foi: **{opcao_sidebar}**")


# --- Colunas (st.columns) ---
st.header("Organizando com Colunas")
st.write("`st.columns()` permite dividir a tela em colunas verticais.")

# Cria duas colunas. `col1` e `col2` são objetos onde você pode colocar conteúdo.
col1, col2 = st.columns(2)

# Adicionando conteúdo à primeira coluna
with col1:
    st.subheader("Coluna 1")
    st.write("Este conteúdo está na primeira coluna.")
    if st.checkbox("Mostrar imagem na Coluna 1"):
        # O Streamlit pode exibir imagens diretamente de uma URL.
        st.image("https://static.streamlit.io/examples/cat.jpg", caption="Gato na Coluna 1")

# Adicionando conteúdo à segunda coluna
with col2:
    st.subheader("Coluna 2")
    st.write("Este conteúdo está na segunda coluna.")
    if st.checkbox("Mostrar outra imagem na Coluna 2"):
        st.image("https://static.streamlit.io/examples/dog.jpg", caption="Cachorro na Coluna 2")

# Você pode ajustar a proporção das colunas
st.write("Você também pode definir a largura relativa das colunas.")
col_a, col_b, col_c = st.columns([3, 1, 1]) # A primeira coluna será 3x mais larga que as outras

col_a.success("Coluna A (largura 3)")
col_b.warning("Coluna B (largura 1)")
col_c.error("Coluna C (largura 1)")


# --- Expansor (st.expander) ---
st.header("Conteúdo Expansível")
st.write("`st.expander` é útil para ocultar conteúdo que não precisa estar sempre visível.")

with st.expander("Clique aqui para ver os detalhes"):
    st.write("""
    Este é um conteúdo detalhado que fica oculto por padrão.
    É ótimo para seções de "Ajuda", "Informações Adicionais" ou
    qualquer conteúdo que possa poluir a interface principal.
    """)
    st.code("st.expander('Título')")

st.write("Fim da Aula 3. Experimente combinar a barra lateral, colunas e expansores!")
