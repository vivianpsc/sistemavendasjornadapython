# Passo a passo do projeto
# Passo 1: Criar a tela do sistema
# Passo 2: Criar o formulário de cadastro
# Passo 3: Salvar a venda na base de dados
# Passo 4: Mostrar a base de dados na tela
# Passo 5: Criar o dashboard com os gráficos

#Título 
# Seção Cadastrar Vendas
    #Campo data
    # Campo vendedor
    # Campo quantidade
    # Campo produto
    # Campo Valor

# Seção de Vendas
    # Tabela de vendas

# Seção Dashboard
    # Card/Métrica
    # Gráfico de Barra/ coluna -> Venda por Vendedor
    # Grafico de pizza -> Venda por produto

# Streamlit
# Pandas
# Plotly

import streamlit as  st
import pandas as pd
import plotly.express as px

#Carregar a base de Vendas
tabela_vendas = pd.read_csv("vendas.csv")

st.write("# Sistema de Vendas")

#Seção de cadastro de Vendas

st.sidebar.write("## Cadastrar de Vendas")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor",["Ana","Bruno","Carla"])
produto = st.sidebar.selectbox("Produto",["Notebook","Celular","Fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor" )
botao_cadastrar = st.sidebar.button("Cadastrar Vendas")

#logica de cadastro
if botao_cadastrar:
    nova_venda = [str(data), vendedor, produto,quantidade, valor]
    ultima_linha = len(tabela_vendas) #121 linhas 
    tabela_vendas.loc[ultima_linha] = nova_venda
    tabela_vendas.to_csv("vendas.csv",index=False)
    st.success("Venda cadastrada!")


#Seção de visualizar Vendas
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)



#Seção de cadastro de Vendas
st.write("## Dashboard")

# Card/Métrica
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento Total",f"R$ {faturamento}")

# Gráfico de Barra/ coluna -> Venda por Vendedor
grafico1 = px.bar(tabela_vendas ,x="vendedor", y="valor", color ="produto")
st.plotly_chart(grafico1)
   
# Grafico de pizza -> Venda por produto
grafico2 = px.pie(tabela_vendas, names ="produto", values = "valor",hole = 0.5)
st.plotly_chart(grafico2)