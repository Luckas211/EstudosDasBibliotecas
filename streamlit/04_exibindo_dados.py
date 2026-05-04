# streamlit/04_exibindo_dados.py

"""
Aula 4: Exibindo Dados com Pandas e Gráficos

Uma das principais utilidades do Streamlit é visualizar dados.
Ele tem integração nativa com a biblioteca Pandas para exibir tabelas (DataFrames)
e também possui comandos simples para criar gráficos interativos.

Para esta aula, você precisará ter o Pandas e o NumPy instalados:
pip install pandas numpy

Para executar este arquivo:
streamlit run 04_exibindo_dados.py
"""

import streamlit as st
import pandas as pd
import numpy as np

st.title("Aula 4: Exibindo Dados")

# --- Criando um DataFrame de Exemplo ---
# Em uma aplicação real, você carregaria seus dados de um arquivo (CSV, Excel)
# ou de um banco de dados. Aqui, vamos criar dados de exemplo.
st.header("Criando Dados de Exemplo com Pandas")

# np.random.randn(20, 3) cria uma matriz 20x3 com números aleatórios.
# pd.DataFrame cria a tabela com os dados e nomes de colunas.
dados = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Coluna A', 'Coluna B', 'Coluna C']
)

st.write("Abaixo estão os dados que vamos usar nesta aula:")
# st.write() renderiza um DataFrame como uma tabela interativa.
st.write(dados)


# --- Exibindo DataFrames ---
st.header("Formas de Exibir DataFrames")

st.subheader("1. `st.dataframe()`")
st.write("Permite rolar e ordenar a tabela. Ideal para tabelas grandes.")
st.dataframe(dados)

st.subheader("2. `st.table()`")
st.write("Renderiza uma tabela estática. Ideal para tabelas pequenas.")
# Vamos mostrar apenas as 5 primeiras linhas para não ocupar muito espaço.
st.table(dados.head())


# --- Gráficos Nativos do Streamlit ---
st.header("Criando Gráficos Simples")
st.write("O Streamlit oferece funções fáceis para gráficos comuns.")

# Para os gráficos, vamos criar um novo DataFrame com um índice de tempo.
dados_grafico = pd.DataFrame(
    np.random.randn(20, 2),
    columns=['Preço', 'Volume']
)

st.subheader("Gráfico de Linha (`st.line_chart`)")
st.write("Ideal para visualizar dados ao longo do tempo.")
st.line_chart(dados_grafico)

st.subheader("Gráfico de Barras (`st.bar_chart`)")
st.write("Ótimo para comparar categorias.")
# Vamos usar os dados originais e pegar as 5 primeiras linhas.
st.bar_chart(dados.head())

st.subheader("Gráfico de Área (`st.area_chart`)")
st.write("Similar ao gráfico de linha, mas com a área preenchida.")
st.area_chart(dados_grafico)


# --- Mapas ---
st.header("Exibindo Dados em um Mapa")
st.write("`st.map()` plota pontos em um mapa se você tiver colunas de latitude e longitude.")

# Criando dados de exemplo com coordenadas de algumas cidades do Brasil.
dados_mapa = pd.DataFrame({
    'cidade': ['São Paulo', 'Rio de Janeiro', 'Salvador'],
    'lat': [-23.5505, -22.9068, -12.9777],
    'lon': [-46.6333, -43.1729, -38.5016]
})

st.write("Localização de algumas cidades:")
st.map(dados_mapa)

st.write("Fim da Aula 4. Tente carregar seus próprios dados de um arquivo CSV!")