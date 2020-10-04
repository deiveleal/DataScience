#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 16:21:10 2020

@author: deive
"""

#Importa a biblioteca pandas
import pandas as pd

#Importa o dataset
df = pd.read_csv('/home/deive/Git Files/Estudos_em_analise_de_dados/titanic/train.csv')

#Mostra as 5 primeiras linhas do dataset, se quantidade não for especificada entre os parenteses
df.head() 

#Mostra as 10 primeiras linhas do dataset, quantidade foi especificada dentro dos parenteses
df.head(10)

#Mostra as 5 últimas linhas do dataset, se quantidade não for especificada entre os parenteses
df.tail()

#Mostra as 10 últimas linhas do dataset, quantidade foi especificada dentro do parenteses
df.tail(10)

#Importa o dataset, mas especificando colunas
df_some_datas = pd.read_csv('/home/deive/Git Files/Estudos_em_analise_de_dados/titanic/train.csv', usecols=["PassengerId","Survived", "Pclass"])
df_some_datas.head()

#Apresenta um resumo de valores numéricos no dataset. Calcula média, desvio padrão, valor mínimo, máximo, etc.
df.describe()

#Apresenta informações do dataset incluindo o índice dtype, coluna dtype, valores não nulos e uso de memória
df.info() 

#Ordenar uma coluna por preço ou alfabeticamente, a coluna usada na ordenação é indicada entre parenteses, ordena do menor para o maior
df.sort_values("Fare").head(7)

#Para inverter a ordenação o ascending recebe false no código
df.sort_values("Fare",ascending = False).head(7)

#O dataset pode ser salvo nele mesmo, recebendo o valor ordenado dele
df = df.sort_values("Fare", ascending = False)
df.head(7)

#Também pode ser salvo utilizando o argumento inplace, este recebendo o valor True
df.sort_values("Fare", ascending = False, inplace = True)
df.head(7)

#Ordenando coluna alfabeticamente, deixando por último os valores nulos 
#(o argumento na_position recebe a posição que eles aparecerão)
df.sort_values("Cabin", ascending = True, na_position = 'last')

#Há duas formas de selecionar uma coluna:
#dataset.coluna
#dataset["coluna"]

#Adicionando o método value_counts() a coluna selecionada obtemos a contagem de itens diferentes na coluna
df["Sex"].value_counts()

#Utilizando o método nunique() podemos contar valores ocorridos em um dataset ou em uma coluna específica, 
#sem especificar uma coluna, todas elas mostram seus valores únicos
df.nunique()

#Especificando uma coluna junto com o método nunique()
df["Embarked"].nunique()

#Para visualizar mais de uma coluna, adicionamos entre colchetes
df[["Embarked","Sex"]].nunique()

#Para mudar o tipo de dado de uma coluna usa-se o método .astype()
df.Embarked = df.Embarked.astype("category")
df['Embarked'].dtype

#Para visualizar dados sobre uma condição usa-se o duplo sinal de igual (==) seguido do valor de comparação
#Os dois códigos abaixo tem o mesmo resultado
df.Embarked == "C"
df['Embarked'] == "C"

#Caso se queira ver todos os dados com a condição, ao invés de True or False, o código vem entre colchetes
#Os dois códigos abaixo tem o mesmo resultado
df[df.Embarked == "C"].head() # O método .head() ao final é apenas para mostrar os 5 resultados
df[df["Embarked"] == "C"].head() # O método .head() ao final é apenas para mostrar os 5 resultados

#Filtrando com duas ou mais condições
#Símbolos de condição: maior(>), menor(<), igual(==),diferente(!=)
#Operadores: and ou &, or ou |
df[(df["Fare"] < 100) & (df["Sex"] == "female")].head(7)
#Outro código, mesmo resultado
df_fare_mask = df["Fare"] < 100
df_sex_mask = df["Sex"] == "female" 
df[df_fare_mask & df_sex_mask].head(7)

#Para encontrar os valores nulos pode ser usado o método .isnull()
null_mask = df["Cabin"].isnull()
df[null_mask]
#Outro código, mesmo resultado
df[df["Cabin"].isnull()]

#Usando o método .isnull() para verificar todo o dataset junto ao método .sum() para somar os resultados de cada coluna
df.isnull().sum()

#Para excluir uma coluna usa-se o método .drop() com os detalhes da coluna. 
#O argumento axis aponta que é uma coluna (1) ou linha (0), 
df.drop(labels = ['Cabin'], axis = 1).head()

#Excluindo mais de uma coluna
df.drop(labels = ["Cabin", "Name"], axis=1).head()

#Preenchendo valores faltantes no dataset com o método .fillna()
#Neste caso os valores faltantes da coluna especificada são preenchidos com 0 e o próprio dataset é atualizado
df['columnname'].fillna(0, inplace = True)

#Se quiser preencher os valores faltantes com a média da coluna é usado o seguinte código
df['Age'] = df['Age'].fillna((df['Age'].median()))
df.head(7)
