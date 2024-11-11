# importando bibliotecas
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import folium as fl
import streamlit as st
from PIL import Image


st.set_page_config(page_title='Car crashes on research', page_icon='🔎👩‍💻', layout='wide') # aumenta a layout
#---------------- FUNÇÕES

def acidents_cause(df1):
    
    """Essa função devolve um dataframe com as 10 maiores 
    causas de acidentes no Brasil
    """
    
    df_aux = (df1.loc[:,['causa_acidente','uf']]
              .groupby('causa_acidente')
              .count()
              .reset_index())
    df_aux.columns = ['Causa_Acidente','Quantidade_Acidentes']
    df_aux = (df_aux.sort_values('Quantidade_Acidentes',ascending=False)
              .head(10)
              .reset_index(drop=True))
    return df_aux
#-----------------
def min_acidents_of_cause(df1):
    
    df_aux = (df1.loc[:,['causa_acidente','uf']]
              .groupby('causa_acidente')
              .count()
              .reset_index())
    df_aux.columns = ['Causa_Acidente','Quantidade_Acidentes']
    df_aux = (df_aux.sort_values('Quantidade_Acidentes',ascending=True)
              .head(10)
              .reset_index(drop=True))
    return df_aux


# limpeza dos dados


def clean_data(df1):
    
    """Essa função faz a limpeza do dataframe,
    e converte algumas colunas object em outros valores
    usa-se a biblioteca pandas para conversão
    """
    
    df1['data_inversa'] = pd.to_datetime(df1['data_inversa'], format='%Y-%m-%d', errors='coerce') # data
    
    
    df1['horario'] = pd.to_datetime(df1['horario'], format='%H:%M:%S') # mudando para horário
    
    df1 = df1.astype({'feridos_leves':'int','feridos_graves':'int','ilesos':'int','ignorados':'int','feridos':'int','veiculos':'int'}) # trasnformando as colunas em int
    
    df1['uf'] = df1['uf'].astype('string') # convertendo para str
    return df1

#---------------------------------------------------------------#
df = pd.read_csv('../dashboard/accidents_2017_to_2023_portugues.csv', on_bad_lines='skip')
df1 = df.copy()
df1= clean_data(df1)



#---------------------------------------------------------------#



#---------------------------------------------------------------#
#                                                               #
#------------------------- sidebar -----------------------------#
#                                                               #
#---------------------------------------------------------------#


st.header('Acidentes de carro no Brasil entre 2017-2021')
#logo


# arquivo_image= r"repos/proggramacao_python/projeto2/img1_acidente.jpg"
image = Image.open('img1_acidente.jpg')
st.sidebar.image(image, width=120)

st.sidebar.markdown('# Brazil reviews')
st.sidebar.markdown( '##### *Car accidents in Brazil from 2017 to 2021*')
st.sidebar.markdown("""---""")



st.markdown('#')
st.sidebar.markdown('## As 10 maiores e menores causas de acidentes')







#---------------------------------------------------------------#
#                                                               #
#------------------------- Layout ------------------------------#
#                                                               #
#---------------------------------------------------------------#

tab1, tab2, tab3 = st.tabs(["As maiores e menores causas","--","--"])

with tab1:
    st.markdown('# As 10 maiores e menores causas de acidentes entre 2017-2021 no Brasil')
    st.markdown('### *Beyond the Crash: Understanding the Highest and Lowest Causes of Accidents in Brazil*')
# --------------- primeiro container, aqui apresentamos os dados das maiores causas dos acidentes
    with st.container():
        coluna = 1
        row1 = st.columns(2)
        row2 = st.columns(2)
        row3 = st.columns(2)
        row4 = st.columns(2)
        row5 = st.columns(2)

        i = 0
        x = 1
        df_aux = acidents_cause(df1)
        
        for col in row1+row2+row3+row4+row5:
            valor = df_aux.iloc[i, 1]
            nome = df_aux.iloc[i, 0]
            i+=1
            tile = col.container(height=200)
            tile.markdown(f'##### {nome}')
            tile.metric(label='mortes:', value=valor, delta=x)
            x+=1
        
        st.markdown("""---""")

        # segundo container menores causas

# --------------- primeiro container, aqui apresentamos os dados das menores causas dos acidentes
        with st.container():
            st.markdown('### *Beyond the Crash: Understanding the Highest and Lowest Causes of Accidents in Brazil*')
        coluna = 1
        row1 = st.columns(2)
        row2 = st.columns(2)
        row3 = st.columns(2)
        row4 = st.columns(2)
        row5 = st.columns(2)


        i = 0
        x = -1
        df_aux =min_acidents_of_cause(df1)
        
        for col in row1+row2+row3+row4+row5:
            valor = df_aux.iloc[i, 1]
            nome = df_aux.iloc[i, 0]
            i+=1
            tile = col.container(height=200)
            tile.markdown(f'##### {nome}')
            tile.metric(label='mortes:', value=valor, delta=x)
            x =x - 1

            
            
            
            
            
            
        
        
        


