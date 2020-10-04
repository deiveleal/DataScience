# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 21:06:37 2020

@author: Deive
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def graph_bar(x_values, y_values, label):
    '''
    Criação de gráfico de barras
    '''
    plt.figure(figsize=(10,8))
    sns.barplot(x_values, y_values, label=x_values)
    plt.legend(x_values, loc='best')
    plt.xticks(fontsize=14, rotation=75)
    plt.yticks(fontsize=14)
    plt.title(label, fontsize=20)
    return graph_bar

def graph_hist(x_values, label):
    '''
    Criação de histogramabarras
    '''
    plt.figure(figsize=(10,8))
    sns.distplot(x_values)
    plt.xticks(fontsize=14, rotation=75)
    plt.title(label, fontsize=20)
    return graph_hist

def graph_pie(x_values, label):
    '''
    Criação de gráfico de pizza
    '''
    plt.figure(figsize=(10,8))
    plt.pie(x_values, labels=x_values.index, autopct='%1.1f%%')
    plt.title(label, fontsize=20)
    return graph_pie

def graph_lin_point(x_values, y_values, label):
    '''
    Criação de gráfico de linhas e pontos
    '''
    plt.figure(figsize=(10,8))
    plt.scatter(x_values, y_values)
    plt.plot(x_values, y_values)
    plt.xticks(fontsize=14, rotation=75)
    plt.title(label, fontsize=20)
    return graph_lin_point


def main():
    st.sidebar.title('População em Situação de Rua - Censo Pop Rua')
    st.sidebar.image('CentroPopI.png', width=200)

    file = st.file_uploader('Clique para Inserir ou Solte aqui o Arquivo', encoding='utf-8', type='csv')

    if file is None:
        st.markdown('Aguardando Upload de Arquivo...')
    if file is not None:
        st.markdown('Arquivo Carregado com Sucesso')

        #Le o dataset e o transforma em dataframe
        df = pd.read_csv(file)
        st.sidebar.header('Escolha o tipo de análise')
        data_explorer = st.sidebar.checkbox('Exploração dos dados')
        if data_explorer:
            #Início da análise dos dados
            st.header('Análise dos Dados do Arquivo')
            

            #Apresenta o número de linhas e o de colunas
            st.subheader('Número de Linhas/Observações')
            st.markdown(df.shape[0])
            st.subheader('Número de Colunas')
            st.markdown(df.shape[1])
            
            #Visualização de Dados por linhas
            st.subheader('Visualização de Dados por Linha')
            number_lines = st.slider('Escolha o número de linhas para visualização',min_value=0,max_value=25)
            if number_lines != 0:
                st.dataframe(df.head(number_lines))

            #Tipos de informações do dataframe
            st.subheader('Escolha a Informação que Deseja Visualizar')
            radio_data = st.radio('', ( 'Nomes das Colunas', 'Descrição do DataSet', 'Valores Nulos por Coluna no DataSet', 'Porcentagem de Valores Nulos por Coluna no DataSet'))
            if radio_data == 'Nomes das Colunas':
                st.markdown(df.columns)
            if radio_data == 'Descrição do DataSet':
                st.write(df.describe())
            if radio_data == 'Valores Nulos por Coluna no DataSet':
                st.table(df.isna().sum(),)
            if radio_data == 'Porcentagem de Valores Nulos por Coluna no DataSet':
                st.table((df.isna().sum() / df.shape[0]) * 100)

        graph_explorer = st.sidebar.checkbox('Visualização de Gráficos')
        if graph_explorer:
            #Exploração de dados via gráficos
            st.header('Análise de Dados a Partir de Gráficos')
            select_graph = st.selectbox('Escolha o Tipo de Gráfico', ['Barras', 'Histograma', 'Pizza', 'Pontos e Linhas'])
            select_columns = st.selectbox('Escolha o Dado de Interesse', df.columns)
            
            #Gráfico de Barras
            if select_graph == 'Barras':
                x_values = df[select_columns].value_counts().index
                y_values = df[select_columns].value_counts()
                label_bar = select_columns
                graph_bar(x_values, y_values, label_bar)
                st.pyplot()
            
            #Histograma
            if select_graph == 'Histograma':
                x_values = df[select_columns].value_counts()
                label_hist = select_columns
                graph_hist(x_values, label_hist)
                st.pyplot()
            
            #Pizza
            if select_graph == 'Pizza':
                x_values = df[select_columns].value_counts()
                label_pie = select_columns
                graph_pie(x_values, label_pie)
                st.pyplot()
            
            #Pontos e Linhas
            if select_graph == 'Pontos e Linhas':
                x_values = df[select_columns].value_counts()
                y_values = df[select_columns].value_counts()
                label_hist = select_columns
                graph_lin_point(x_values, y_values, label_hist)
                st.pyplot()

if __name__ == '__main__':
    main()


