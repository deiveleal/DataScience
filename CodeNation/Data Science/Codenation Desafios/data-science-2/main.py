#!/usr/bin/env python
# coding: utf-8

# # Desafio 4
# 
# Neste desafio, vamos praticar um pouco sobre testes de hipóteses. Utilizaremos o _data set_ [2016 Olympics in Rio de Janeiro](https://www.kaggle.com/rio2016/olympic-games/), que contém dados sobre os atletas das Olimpíadas de 2016 no Rio de Janeiro.
# 
# Esse _data set_ conta com informações gerais sobre 11538 atletas como nome, nacionalidade, altura, peso e esporte praticado. Estaremos especialmente interessados nas variáveis numéricas altura (`height`) e peso (`weight`). As análises feitas aqui são parte de uma Análise Exploratória de Dados (EDA).
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Setup_ geral

# In[106]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sct
import seaborn as sns
import statsmodels.api as sm


# In[107]:


#%matplotlib inline

from IPython.core.pylabtools import figsize


figsize(12, 8)

sns.set()


# In[108]:


athletes = pd.read_csv("athletes.csv")


# In[109]:


def get_sample(df, col_name, n=100, seed=42):
    """Get a sample from a column of a dataframe.
    
    It drops any numpy.nan entries before sampling. The sampling
    is performed without replacement.
    
    Example of numpydoc for those who haven't seen yet.
    
    Parameters
    ----------
    df : pandas.DataFrame
        Source dataframe.
    col_name : str
        Name of the column to be sampled.
    n : int
        Sample size. Default is 100.
    seed : int
        Random seed. Default is 42.
    
    Returns
    -------
    pandas.Series
        Sample of size n from dataframe's column.
    """
    np.random.seed(seed)
    
    random_idx = np.random.choice(df[col_name].dropna().index, size=n, replace=False)
    
    return df.loc[random_idx, col_name]


# ## Inicia sua análise a partir daqui

# In[110]:


athletes.head(7)


# In[111]:


athletes.describe()


# In[112]:


sample_athlet_height = get_sample(athletes, 'height', 3000)


# In[113]:


sample_athlet_weight = get_sample(athletes, 'weight', 3000)


# In[128]:


bra = athletes[athletes['nationality'] == 'BRA']
print(bra)


# In[129]:


bra.isna().sum()


# In[130]:


can = athletes[athletes['nationality'] == 'CAN']
print(can)


# In[131]:


can.isna().sum()


# In[132]:


usa = athletes[athletes['nationality'] == 'USA']
print(usa)


# In[133]:


usa.isna().sum()


# In[76]:


sns.distplot(sample_athlet_height)


# In[77]:


sct.shapiro(sample_athlet_height)


# In[78]:


sct.jarque_bera(sample_athlet_height)


# In[79]:


sct.normaltest(sample_athlet_weight)


# In[80]:


sample_athlet_weight_log = np.log(sample_athlet_weight)
sct.normaltest(sample_athlet_weight_log)


# In[123]:


sct.ttest_ind(can['height'],usa['height'], equal_var=False)[1].round(8)


# ## Questão 1
# 
# Considerando uma amostra de tamanho 3000 da coluna `height` obtida com a função `get_sample()`, execute o teste de normalidade de Shapiro-Wilk com a função `scipy.stats.shapiro()`. Podemos afirmar que as alturas são normalmente distribuídas com base nesse teste (ao nível de significância de 5%)? Responda com um boolean (`True` ou `False`).

# In[20]:


def q1():
    shapiro_p = sct.shapiro(sample_athlet_height)[1]
    if shapiro_p > 0.05:
        boolean_resp = True
    else:
        boolean_resp = False
    return boolean_resp


# In[65]:


sns.distplot(sample_athlet_height, bins=25)


# In[68]:


sm.qqplot(sample_athlet_height, fit = True, line = "45")


# __Para refletir__:
# 
# * Plote o histograma dessa variável (com, por exemplo, `bins=25`). A forma do gráfico e o resultado do teste são condizentes? Por que?
# * Plote o qq-plot para essa variável e a analise.
# * Existe algum nível de significância razoável que nos dê outro resultado no teste? (Não faça isso na prática. Isso é chamado _p-value hacking_, e não é legal).

# ## Questão 2
# 
# Repita o mesmo procedimento acima, mas agora utilizando o teste de normalidade de Jarque-Bera através da função `scipy.stats.jarque_bera()`. Agora podemos afirmar que as alturas são normalmente distribuídas (ao nível de significância de 5%)? Responda com um boolean (`True` ou `False`).

# In[25]:


def q2():
    jarque_bera_p = sct.jarque_bera(sample_athlet_height)[1]
    if jarque_bera_p > 0.05:
        boolean_resp = True
    else:
        boolean_resp = False
    return boolean_resp


# __Para refletir__:
# 
# * Esse resultado faz sentido?

# ## Questão 3
# 
# Considerando agora uma amostra de tamanho 3000 da coluna `weight` obtida com a função `get_sample()`. Faça o teste de normalidade de D'Agostino-Pearson utilizando a função `scipy.stats.normaltest()`. Podemos afirmar que os pesos vêm de uma distribuição normal ao nível de significância de 5%? Responda com um boolean (`True` ou `False`).

# In[45]:


def q3():
    normal_test_p = sct.normaltest(sample_athlet_weight)[1]
    if normal_test_p > 0.05:
        boolean_resp = True
    else:
        boolean_resp = False
    return boolean_resp


# __Para refletir__:
# 
# * Plote o histograma dessa variável (com, por exemplo, `bins=25`). A forma do gráfico e o resultado do teste são condizentes? Por que?
# * Um _box plot_ também poderia ajudar a entender a resposta.

# ## Questão 4
# 
# Realize uma transformação logarítmica em na amostra de `weight` da questão 3 e repita o mesmo procedimento. Podemos afirmar a normalidade da variável transformada ao nível de significância de 5%? Responda com um boolean (`True` ou `False`).

# In[54]:


def q4():
    sample_athlet_weight_log = np.log(sample_athlet_weight)
    normal_test_p = sct.normaltest(sample_athlet_weight_log)[1]
    if normal_test_p > 0.05:
        boolean_resp = True
    else:
        boolean_resp = False
    return boolean_resp


# __Para refletir__:
# 
# * Plote o histograma dessa variável (com, por exemplo, `bins=25`). A forma do gráfico e o resultado do teste são condizentes? Por que?
# * Você esperava um resultado diferente agora?

# > __Para as questão 5 6 e 7 a seguir considere todos testes efetuados ao nível de significância de 5%__.

# ## Questão 5
# 
# Obtenha todos atletas brasileiros, norte-americanos e canadenses em `DataFrame`s chamados `bra`, `usa` e `can`,respectivamente. Realize um teste de hipóteses para comparação das médias das alturas (`height`) para amostras independentes e variâncias diferentes com a função `scipy.stats.ttest_ind()` entre `bra` e `usa`. Podemos afirmar que as médias são estatisticamente iguais? Responda com um boolean (`True` ou `False`).

# In[152]:


def q5():
    ttest_p = sct.ttest_ind(bra['height'],usa['height'], equal_var=False, nan_policy='omit')[1]
    print(sct.ttest_ind(bra['height'],usa['height'], equal_var=False, nan_policy='omit'))
    if ttest_p > 0.05:
        boolean_resp = True
    else:
        boolean_resp = False
    return boolean_resp
q5()


# ## Questão 6
# 
# Repita o procedimento da questão 5, mas agora entre as alturas de `bra` e `can`. Podemos afimar agora que as médias são estatisticamente iguais? Reponda com um boolean (`True` ou `False`).

# In[150]:


def q6():
    ttest_p = sct.ttest_ind(bra.height,can.height, nan_policy='omit')[1]
    print(sct.ttest_ind(bra.height,can.height, nan_policy='omit'))
    if ttest_p > 0.05:
        boolean_resp = True
    else:
        boolean_resp = False
    return boolean_resp
q6()


# ## Questão 7
# 
# Repita o procedimento da questão 6, mas agora entre as alturas de `usa` e `can`. Qual o valor do p-valor retornado? Responda como um único escalar arredondado para oito casas decimais.

# In[145]:


def q7():
    athletes = pd.read_csv("athletes.csv")
    usa = athletes[athletes['nationality'] == 'USA']
    can = athletes[athletes['nationality'] == 'CAN']
    stat, p_value = sct.ttest_ind(can.height,usa.height, equal_var=False, nan_policy='omit')
    print('stat: ' + str(stat))
    print('p_value: ' + str(p_value))
    return round(p_value,8)
q7()


# __Para refletir__:
# 
# * O resultado faz sentido?
# * Você consegue interpretar esse p-valor?
# * Você consegue chegar a esse valor de p-valor a partir da variável de estatística?

# In[ ]:




