# streamlit/02_widgets_interativos.py

"""
Aula 2: Widgets Interativos

Widgets são os elementos que permitem que seus usuários interajam com a aplicação.
Eles podem ser botões, caixas de texto, sliders, e muito mais.

O valor de um widget é retornado pela função que o cria. O Streamlit
re-executa o script de cima para baixo sempre que um usuário interage com um widget.

Para executar este arquivo:
streamlit run 02_widgets_interativos.py
"""

import streamlit as st

st.title("Aula 2: Widgets Interativos")

st.write("Widgets permitem que os usuários enviem informações para sua aplicação.")

# --- Botão (st.button) ---
st.header("Botão")
st.write("O `st.button` retorna `True` quando é clicado.")

# O código dentro do `if` só será executado quando o botão for pressionado.
if st.button("Clique em mim"):
    st.write("Obrigado por clicar! 🎉")
else:
    st.write("O botão ainda não foi clicado.")

# --- Caixa de Seleção (st.checkbox) ---
st.header("Caixa de Seleção")
st.write("Use `st.checkbox` para opções de 'sim' ou 'não'.")

mostrar_mensagem = st.checkbox("Marque esta caixa para ver uma mensagem")

if mostrar_mensagem:
    st.success("Você marcou a caixa! Aqui está sua mensagem secreta.")

# --- Rádio (st.radio) ---
st.header("Botões de Rádio")
st.write("`st.radio` é usado para selecionar uma opção entre várias.")

opcao_radio = st.radio(
    "Qual é a sua linguagem de programação favorita?",
    ("Python", "JavaScript", "Java", "Outra")
)

st.write(f"Você selecionou: **{opcao_radio}**")
if opcao_radio == "Python":
    st.write("Ótima escolha! 🐍")

# --- Caixa de Seleção Múltipla (st.selectbox) ---
st.header("Caixa de Seleção (Selectbox)")
st.write("`st.selectbox` é um menu suspenso para escolher uma única opção.")

opcao_selectbox = st.selectbox(
    "Qual framework você está aprendendo?",
    ["Streamlit", "Django", "Flask", "FastAPI"]
)

st.write(f"Você está aprendendo: **{opcao_selectbox}**")

# --- Slider (st.slider) ---
st.header("Slider")
st.write("`st.slider` permite selecionar um número em um intervalo.")

idade = st.slider("Qual é a sua idade?", min_value=0, max_value=130, value=25, step=1)
st.write(f"Sua idade é: **{idade}** anos.")

# --- Entrada de Texto (st.text_input) ---
st.header("Entrada de Texto")
st.write("`st.text_input` é um campo para o usuário digitar um texto.")

nome = st.text_input("Digite o seu nome", placeholder="Seu nome aqui...")

if nome:
    st.write(f"Olá, **{nome}**! Bem-vindo(a).")

st.write("Fim da Aula 2. Brinque com os widgets e veja como a página se atualiza!")
