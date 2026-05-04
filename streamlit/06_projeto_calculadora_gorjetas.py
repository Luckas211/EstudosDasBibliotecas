# streamlit/06_projeto_calculadora_gorjetas.py

"""
Aula 6: Projeto Prático - Calculadora de Gorjetas

Vamos aplicar os conceitos aprendidos para criar uma aplicação funcional.
Esta calculadora permitirá ao usuário inserir o valor da conta, escolher a
porcentagem da gorjeta e o número de pessoas para dividir a conta.

Conceitos que vamos usar:
- `st.title`, `st.header`, `st.write`
- `st.number_input` para entrada de números
- `st.slider` para selecionar a porcentagem
- `st.columns` para organizar o layout
- Cálculos e exibição de resultados formatados

Para executar este arquivo:
streamlit run 06_projeto_calculadora_gorjetas.py
"""

import streamlit as st

# --- Configuração da Página e Título ---
st.set_page_config(layout="centered", page_title="Calculadora de Gorjetas")

st.title("Calculadora de Gorjetas 💸")

st.write("Uma aplicação simples para calcular a gorjeta e dividir a conta.")

# --- Layout com Colunas para Entradas ---
# Usaremos colunas para organizar melhor os campos de entrada.
col1, col2 = st.columns(2)

with col1:
    # st.number_input é ideal para entrada de valores numéricos.
    valor_conta = st.number_input(
        "Qual o valor total da conta?",
        min_value=0.0,       # Valor mínimo
        value=50.0,          # Valor padrão
        step=1.0,            # Incremento ao clicar nas setas
        format="%.2f"        # Formato de exibição (2 casas decimais)
    )

    num_pessoas = st.number_input(
        "Dividir a conta entre quantas pessoas?",
        min_value=1,
        value=1,
        step=1
    )

with col2:
    # st.slider é uma forma intuitiva de selecionar uma porcentagem.
    percentual_gorjeta = st.slider(
        "Qual a porcentagem da gorjeta?",
        min_value=0,
        max_value=100,
        value=15, # Valor padrão de 15%
        step=1
    )

# --- Cálculos ---
# Apenas realizamos os cálculos se o valor da conta for maior que zero.
if valor_conta > 0:
    valor_gorjeta = (valor_conta * percentual_gorjeta) / 100
    valor_total_com_gorjeta = valor_conta + valor_gorjeta
    valor_por_pessoa = valor_total_com_gorjeta / num_pessoas

    # --- Exibição dos Resultados ---
    st.header("Resultados")

    # Usamos st.metric para exibir valores de forma destacada.
    # Ele mostra um rótulo, o valor e, opcionalmente, uma variação.
    col_res1, col_res2, col_res3 = st.columns(3)

    with col_res1:
        st.metric(
            label="Valor da Gorjeta",
            value=f"R$ {valor_gorjeta:.2f}"
        )

    with col_res2:
        st.metric(
            label="Valor Total da Conta",
            value=f"R$ {valor_total_com_gorjeta:.2f}"
        )

    with col_res3:
        st.metric(
            label="Valor por Pessoa",
            value=f"R$ {valor_por_pessoa:.2f}"
        )

    # Adicionando um expansor com o resumo do cálculo
    with st.expander("Ver resumo do cálculo"):
        st.write(f"Valor da Conta: R$ {valor_conta:.2f}")
        st.write(f"Percentual da Gorjeta: {percentual_gorjeta}%")
        st.write(f"Número de Pessoas: {num_pessoas}")
        st.write("---")
        st.write(f"Cálculo do Total: R$ {valor_conta:.2f} + R$ {valor_gorjeta:.2f} = R$ {valor_total_com_gorjeta:.2f}")
        st.write(f"Cálculo por Pessoa: R$ {valor_total_com_gorjeta:.2f} / {num_pessoas} = R$ {valor_por_pessoa:.2f}")

else:
    st.info("Por favor, insira um valor para a conta para iniciar o cálculo.")

st.write("---")
st.success("Projeto finalizado! Agora você tem uma aplicação Streamlit completa.")
