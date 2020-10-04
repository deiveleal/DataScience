#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[3]:


black_friday.columns


# In[4]:


df = black_friday


# In[5]:


df.head(3)


# In[6]:


df.info()


# In[7]:


df[['Product_Category_1','Product_Category_2','Product_Category_3']].head(7)


# In[8]:


aux = pd.DataFrame({'colunas' : df.columns, 'tipos' : df.dtypes, 'missing': df.isna().sum()})


# In[9]:


aux.head()


# In[10]:


aux['missing_percentual'] = aux['missing'] / df.shape[0]


# In[11]:


aux


# In[12]:


df.shape


# In[13]:


df.Product_ID.nunique()


# In[14]:


df.dtypes


# In[15]:


df.dtypes.value_counts()


# In[16]:


df.Age.value_counts()


# In[17]:


q2 = df[df.Age == '26-35']


# In[18]:


q2.User_ID.nunique()


# In[19]:


q2.shape[0]


# In[20]:


q2.User_ID.value_counts()


# In[21]:


q2.groupby('Gender')['User_ID'].nunique()


# In[22]:


mean = df.Purchase.mean()


# In[23]:


std = df.Purchase.std()


# In[24]:


df.Purchase_norm = (df.Purchase - mean) / std


# In[25]:


df.Purchase_norm


# In[26]:


pd.cut(df.Purchase_norm, labels = ('Menor que 1', 'Maior que 1'), bins = (-1000, 1,1000))


# In[27]:


#10
df[df.isna()]


# In[28]:


df.isna().sum()


# In[29]:


df[['Product_Category_2','Product_Category_3']].isna()


# In[30]:


df['Product_Category_2'].isna().equals(df['Product_Category_3'].isna())


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[31]:


def q1():
    obs_col = black_friday.shape
    return obs_col


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[34]:


def q2():
    mulheres = black_friday[black_friday['Gender'] == 'F']
    mulheres_26_35 = mulheres[mulheres['Age'] == '26-35']
    mulheres_26_35 = mulheres_26_35['User_ID'].nunique()
    return mulheres_26_35


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[36]:


def q3():
    return black_friday.User_ID.nunique()


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[66]:


def q4():
    return black_friday.dtypes.nunique()


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[78]:


def q5():
    porc_reg = black_friday[black_friday.isna().any(axis=1)].shape[0] / black_friday.shape[0]
    return porc_reg


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[245]:


def q6():
    return black_friday.isnull().sum().max()


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[249]:


def q7():
    commom_value = black_friday.Product_Category_3.value_counts()
    return commom_value[]


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[311]:


def q8():
    purch_orig_min = black_friday_norm = black_friday['Purchase'] - black_friday['Purchase'].min()
    purch_max_min = black_friday['Purchase'].max() - black_friday['Purchase'].min()
    black_friday_purch_norm = purch_orig_min / purch_max_min
    nova_media = np.mean(black_friday_purch_norm)
    return nova_media


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[361]:


def q9():
    black_friday_purch_padron = (black_friday.Purchase - black_friday.Purchase.mean()) / black_friday.Purchase.std()
    ocorr = black_friday_purch_padron[black_friday_purch_padron >= -1]
    ocorr = ocorr[ocorr <= 1]
    return ocorr.shape[0]


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[443]:


def q10():
    black_friday_prod_2_null = black_friday[black_friday['Product_Category_2'].isna()]
    boole = black_friday_prod_2_null['Product_Category_2'].equals(black_friday_prod_2_null['Product_Category_3'])
    return boole


# In[444]:


q10()

