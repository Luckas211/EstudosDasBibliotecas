# streamlit/05_estado_da_sessao.py

"""
Aula 5: Estado da Sessão (st.session_state)

Por padrão, o Streamlit re-executa seu script inteiro toda vez que um usuário
interage com um widget. Isso significa que as variáveis locais são perdidas
a cada interação.

O "Estado da Sessão" (`st.session_state`) é a solução para isso. Ele funciona
como um dicionário que persiste entre as re-execuções do script, permitindo
que você armazene informações durante a sessão de um usuário.

Para executar este arquivo:
streamlit run 05_estado_da_sessao.py
"""

import streamlit as st

st.title("Aula 5: Estado da Sessão")

st.write("""
O `st.session_state` é a memória da sua aplicação. Ele permite que você
armazene valores que não devem ser perdidos quando o usuário interage
com a página.
""")

# --- Exemplo 1: Contador Simples ---
st.header("Exemplo 1: Contador de Cliques")

# Inicialização: É crucial inicializar as chaves do session_state.
# Verificamos se a chave 'contador' já existe. Se não, a criamos com valor 0.
if 'contador' not in st.session_state:
    st.session_state.contador = 0

# Criamos um botão.
botao_clicado = st.button("Clique aqui para incrementar")

# Se o botão for clicado, incrementamos o valor no session_state.
if botao_clicado:
    st.session_state.contador += 1

# Exibimos o valor atual, que está armazenado no session_state.
st.write(f"O botão foi clicado **{st.session_state.contador}** vezes.")


# --- Exemplo 2: Login Simples ---
st.header("Exemplo 2: Simulando um Login")
st.write("""
Aqui, usaremos o session_state para lembrar se o usuário está "logado" ou não.
""")

# Inicializa o estado de login como False.
if 'logado' not in st.session_state:
    st.session_state.logado = False

# Se o usuário não estiver logado, mostramos os campos de login.
if not st.session_state.logado:
    st.subheader("Área de Login")
    usuario = st.text_input("Usuário", key="usuario_input")
    senha = st.text_input("Senha", type="password", key="senha_input")

    if st.button("Entrar"):
        # Lógica de autenticação simples
        if usuario == "admin" and senha == "1234":
            st.session_state.logado = True
            # st.rerun() força a re-execução imediata do script.
            # Isso é útil para atualizar a interface após uma mudança de estado.
            st.rerun()
        else:
            st.error("Usuário ou senha incorretos.")

# Se o usuário estiver logado, mostramos o conteúdo protegido.
if st.session_state.logado:
    st.success("Login realizado com sucesso! Bem-vindo(a), admin!")
    st.write("Você agora pode ver este conteúdo exclusivo.")

    if st.button("Sair"):
        st.session_state.logado = False
        st.rerun()

st.info("`st.session_state` é um dos conceitos mais importantes para criar aplicações complexas.")