# importando bibliotecas
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import folium as fl
import streamlit as st
from PIL import Image
from streamlit_folium import folium_static

st.set_page_config(page_title='Graph and tables explications', page_icon='📊', layout='wide')


# Funções

def map_graph(df1):
    cols = ['latitude','longitude','municipio','uf', 'mortos']
    df_aux =(df1.loc[:, cols]
             .groupby(['municipio','mortos'])
             .agg({'latitude': 'mean', 
                   'longitude': 'mean', 
                   'uf': 'first',
                   'mortos':'count'}).reset_index(drop=True))
    df_aux = df_aux.sort_values('mortos', ascending=False).head(10)
    
    map = fl.Map()
    
    for index, row in df_aux.iterrows():
      fl.Marker([row['latitude'], row['longitude']], popup=row[('uf')]).add_to(map)



    return map


def data_frame_uf(df1):
    df_aux = (df1.loc[:,['municipio', 'causa_acidente', 'uf']]
              .groupby(['municipio','causa_acidente'])
              .count()
              .reset_index())
    df_aux.columns = ['Municípios', 'Causa_Acidente', 'Quantidade_Acidentes']
    df_aux = (df_aux.sort_values(by='Quantidade_Acidentes',ascending=False)
              .head(10).reset_index(drop=True))
    data_frame = st.dataframe(df_aux)

    return data_frame

def data_frame_week(df1):
    df_aux = df1.loc[:, ['dia_semana','uf']].groupby('dia_semana').count().reset_index()
    df_aux.columns =['Dias_Semana', 'Quantidade_Acidentes']
    df_aux.sort_values(by='Quantidade_Acidentes', ascending=False).reset_index(drop=True)
    df_aux.index = df_aux.index +1
    data_frame = st.dataframe(df_aux)
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
    
    df1['uf'] = df1['uf'].astype('string')
    df1['mortos'] = df1['mortos'].astype('int')# convertendo para str
     # convertendo para str# convertendo para str

    return df1


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

tab1, tab2, tab3 = st.tabs(['Mapa e tabelas', '', ''])

with tab1:

    with st.container():
        figura =map_graph(df1)
        
        folium_static(figura, width=1024, height=600)
        st.markdown("""---""")

    with st.container():
        

        col1, col2 = st.columns(2)
    
        with col1:
            st.markdown('### As causas pedrominântes dos acidentes dos 10 municípios com trânsito mais violentos.')

            data_frame_uf(df1)

    

        with col2:
            st.markdown('### Dias da semana, quais os mais perigosos? Veja na tabela abaixo os dados de 2011-2021:')
            data_frame_week(df1)


    
