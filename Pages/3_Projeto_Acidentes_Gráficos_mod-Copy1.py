# importando bibliotecas
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import folium as fl
import streamlit as st
from PIL import Image

st.set_page_config(page_title='car crashes with death victim on map', page_icon='🚘☠️', layout='wide')

# Funções 

def graph_chart(df1):
    df1_aux = df1.loc[:,['dia_semana','uf']].groupby('uf').count().reset_index()
    df1_aux.columns =['Unidade_Federativa', 'Quantidade_Acidentes']

    fig = px.bar(df1_aux,
                 x='Unidade_Federativa', y='Quantidade_Acidentes',
                 color='Unidade_Federativa', title='Quantidade de Acidentes por Estado')
    return fig


def graph_chart2(df1):
    df_aux = (df.loc[:, ['uf', 'mortos']]
              .groupby('uf')
              .agg(Vítimas_Fatais=('mortos','sum'))
              .reset_index())
    fig = px.bar(df_aux, x='uf', y='Vítimas_Fatais', color='uf', title='Vítimas Fatais por Unidade Federativa')
    return fig


def data_frame_acidents(df1):
    df_aux = (df1.loc[:, ['municipio', 'uf', 'mortos']]
              .groupby('municipio')
              .agg(Quantidade_Acidentes=('uf', 'count'), Vítimas_Fatais=('mortos', 'sum'))
              .sort_values(by='Quantidade_Acidentes', ascending=False)
              .head(10)
              .reset_index())
    df_aux.index = df_aux.index +1
    data_frame = st.dataframe(df_aux, width= 500, height= 500)
    return data_frame


def data_frame_ten(df1):
    df_aux = (df1.loc[:, ['municipio', 'uf', 'mortos']]
              .groupby('municipio')
              .agg(Quantidade_Acidentes=('uf', 'count'), Vítimas_Fatais=('mortos', 'sum'))
              .sort_values(by='Quantidade_Acidentes', ascending=True)
              .head(10)
              .reset_index())
    df_aux.index = df_aux.index +1
    data_frame = st.dataframe(df_aux, width= 500, height= 500)
    return data_frame


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
    return df1 # convertendo para str


df = pd.read_csv('../dashboard/accidents_2017_to_2023_portugues.csv', on_bad_lines='skip')
df1 = df.copy()
df1= clean_data(df1)

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


# Gráficos
tab1, tab2, tab3 = st.tabs(['Gráficos e tabelas', '', ''])

with tab1:

    with st.container():
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('### Acidentes de trânsito por estado entre 2017-2021')
            fig= graph_chart(df1)
            st.plotly_chart(fig, use_container_width=True)
          

        with col2:
            st.markdown('### Vítimas fatais nos 10 estados com trânsito mais violento')
            fig = graph_chart2(df1)
            st.plotly_chart(fig, use_container_width=True)

         
    with st.container():
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('### Vítimas fatais nos 10 municípios com trânsito mais violento')
            data_frame_acidents(df1)

            

        with col2:
            st.markdown('### Vítimas fatais nos 10 municípios com trânsito menos violento')
            data_frame_ten(df1)

        

        