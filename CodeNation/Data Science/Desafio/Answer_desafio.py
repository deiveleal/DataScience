# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 08:57:06 2020

@author: Deive
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

#Importa os datasets e retira a primeira coluna do train
dt_frame_enem_2016_train = pd.read_csv('/media/deive/Arquivos/Git Files/DesafiosCodeNation/datascience/testfiles/train_menos_variáveis.csv')
dt_frame_enem_2016_train = dt_frame_enem_2016_train.drop(['Unnamed: 0'], axis = 1)
dt_frame_enem_2016_test = pd.read_csv('/media/deive/Arquivos/Git Files/DesafiosCodeNation/datascience/testfiles/test.csv')



#Verifica o número de nulos no dataframe
dt_frame_enem_2016_train.isnull().sum()

#Limpa o casos nulos de todas as notas
dt_frame_enem_2016_train = dt_frame_enem_2016_train.dropna(subset=['NU_NOTA_MT','NU_NOTA_CN','NU_NOTA_CH',
                                                                   'NU_NOTA_LC'])
dt_frame_enem_2016_test = dt_frame_enem_2016_test.dropna(subset=['NU_NOTA_CN','NU_NOTA_CH','NU_NOTA_LC'])

#Verifica o número de nulos no dataframe
dt_frame_enem_2016_train.isnull().sum()
dt_frame_enem_2016_test.isnull().sum()

#Retira todos os alunos que tiraram zero como nota em alguma das provas
dt_frame_enem_2016_train = dt_frame_enem_2016_train.loc[dt_frame_enem_2016_train['NU_NOTA_CN']!=0]
dt_frame_enem_2016_train = dt_frame_enem_2016_train.loc[dt_frame_enem_2016_train['NU_NOTA_CH']!=0]
dt_frame_enem_2016_train = dt_frame_enem_2016_train.loc[dt_frame_enem_2016_train['NU_NOTA_LC']!=0]
dt_frame_enem_2016_train = dt_frame_enem_2016_train.loc[dt_frame_enem_2016_train['NU_NOTA_MT']!=0]
dt_frame_enem_2016_train = dt_frame_enem_2016_train.loc[dt_frame_enem_2016_train['NU_NOTA_COMP1']!=0]
dt_frame_enem_2016_train = dt_frame_enem_2016_train.loc[dt_frame_enem_2016_train['NU_NOTA_COMP2']!=0]
dt_frame_enem_2016_train = dt_frame_enem_2016_train.loc[dt_frame_enem_2016_train['NU_NOTA_COMP3']!=0]
dt_frame_enem_2016_train = dt_frame_enem_2016_train.loc[dt_frame_enem_2016_train['NU_NOTA_COMP4']!=0]
dt_frame_enem_2016_train = dt_frame_enem_2016_train.loc[dt_frame_enem_2016_train['NU_NOTA_COMP5']!=0]
dt_frame_enem_2016_train = dt_frame_enem_2016_train.loc[dt_frame_enem_2016_train['NU_NOTA_REDACAO']!=0]
#Finalizada a limpeza dos dados

#Criação de gráficos para verificar a distribuição
x_cn_dist_train = dt_frame_enem_2016_train['NU_NOTA_CN']
x_cn_dist_test = dt_frame_enem_2016_test['NU_NOTA_CN']
sns.distplot(x_cn_dist_train)
sns.distplot(x_cn_dist_test,color='red')
plt.legend(labels=['TRAIN','TEST'],ncol=2, loc='upper left');

#Definição do nome das variáveis que serão utilizadas
variaveis_train = ['NU_NOTA_CN','NU_NOTA_CH','NU_NOTA_LC','NU_NOTA_COMP1','NU_NOTA_COMP2','NU_NOTA_COMP3',
                   'NU_NOTA_COMP4','NU_NOTA_COMP5','NU_NOTA_REDACAO']
variaveis_test = ['NU_NOTA_CN','NU_NOTA_CH','NU_NOTA_LC','NU_NOTA_COMP1','NU_NOTA_COMP2','NU_NOTA_COMP3',
                   'NU_NOTA_COMP4','NU_NOTA_COMP5','NU_NOTA_REDACAO']

#Criando as features que serão usadas na criação do modelo
y_enem_mt_train = dt_frame_enem_2016_train['NU_NOTA_MT']
x_enem_train = dt_frame_enem_2016_train[variaveis_train]
x_enem_test = dt_frame_enem_2016_test[variaveis_test]

#Criação do modelo e treinamento
modelo_mt = LinearRegression()
modelo_mt.fit(x_enem_train,y_enem_mt_train)
modelo_mt.intercept_
modelo_mt.coef_
modelo_mt.score(x_enem_train, y_enem_mt_train)

#Previsão das notas de matemática
previsao_mt = modelo_mt.predict(x_enem_test)

#Atualização do dataframe com a nota de matemática
dt_frame_enem_2016_test['NU_NOTA_MT'] = previsao_mt

#Criação do dataframe de resposta com o número de inscrição e nota de matemática
answer = dt_frame_enem_2016_test.loc[:,['NU_INSCRICAO','NU_NOTA_MT']]

#Exportação do dataframe como arquivo csv
answer_csv = answer.to_csv('answer.csv')











































