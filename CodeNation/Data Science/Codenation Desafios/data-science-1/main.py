#!/usr/bin/env python
# coding: utf-8

# # Desafio 3
# 
# Neste desafio, iremos praticar nossos conhecimentos sobre distribuições de probabilidade. Para isso,
# dividiremos este desafio em duas partes:
#     
# 1. A primeira parte contará com 3 questões sobre um *data set* artificial com dados de uma amostra normal e
#     uma binomial.
# 2. A segunda parte será sobre a análise da distribuição de uma variável do _data set_ [Pulsar Star](https://archive.ics.uci.edu/ml/datasets/HTRU2), contendo 2 questões.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Setup_ geral

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sct
import seaborn as sns
from statsmodels.distributions.empirical_distribution import ECDF


# In[4]:


# %matplotlib inline

from IPython.core.pylabtools import figsize


figsize(12, 8)

sns.set()


# ## Parte 1

# ### _Setup_ da parte 1

# In[5]:


np.random.seed(42)
    
dataframe = pd.DataFrame({"normal": sct.norm.rvs(20, 4, size=10000),
                     "binomial": sct.binom.rvs(100, 0.2, size=10000)})


# ## Inicie sua análise a partir da parte 1 a partir daqui

# ## Questão 1
# 
# Qual a diferença entre os quartis (Q1, Q2 e Q3) das variáveis `normal` e `binomial` de `dataframe`? Responda como uma tupla de três elementos arredondados para três casas decimais.
# 
# Em outra palavras, sejam `q1_norm`, `q2_norm` e `q3_norm` os quantis da variável `normal` e `q1_binom`, `q2_binom` e `q3_binom` os quantis da variável `binom`, qual a diferença `(q1_norm - q1 binom, q2_norm - q2_binom, q3_norm - q3_binom)`?

# In[26]:


def q1():
#     Calcula o quartil (Q1) da normal e subtrai do quartil da binomial 
    q1_norm_bin = np.percentile(dataframe['normal'], 25) - np.percentile(dataframe['binomial'], 25)
#     Calcula o quartil (Q2) da normal e subtrai do quartil da binomial 
    q2_norm_bin = np.percentile(dataframe['normal'], 50) - np.percentile(dataframe['binomial'], 50)
#     Calcula o quartil (Q3) da normal e subtrai do quartil da binomial 
    q3_norm_bin = np.percentile(dataframe['normal'], 75) - np.percentile(dataframe['binomial'], 75)
    return (round(q1_norm_bin, 3),round(q2_norm_bin, 3),round(q3_norm_bin, 3))


# In[27]:


q1()


# Para refletir:
# 
# * Você esperava valores dessa magnitude?
# 
# * Você é capaz de explicar como distribuições aparentemente tão diferentes (discreta e contínua, por exemplo) conseguem dar esses valores?

# ## Questão 2
# 
# Considere o intervalo $[\bar{x} - s, \bar{x} + s]$, onde $\bar{x}$ é a média amostral e $s$ é o desvio padrão. Qual a probabilidade nesse intervalo, calculada pela função de distribuição acumulada empírica (CDF empírica) da variável `normal`? Responda como uma único escalar arredondado para três casas decimais.

# In[15]:


def q2():
#     Calcula a média e o desvio padrão da variável normal
    mean_norm = dataframe['normal'].mean()
    std_norm = dataframe['normal'].std()
#     Ajuste de ECDF na normal
    ecdf_normal = ECDF(dataframe['normal'])
#     ECDF para media + desvio padrão
    ecdf_max = ecdf_normal(mean_norm + std_norm)
#     ECDF para media - desvio padrão
    ecdf_min = ecdf_normal(mean_norm - std_norm)
#     Calcula a probabilidade no intervalo subtraindo ecdf_max - ecdf_min
    prob_norm = round(ecdf_max - ecdf_min, 3)
    return prob_norm


# Para refletir:
# 
# * Esse valor se aproxima do esperado teórico?
# * Experimente também para os intervalos $[\bar{x} - 2s, \bar{x} + 2s]$ e $[\bar{x} - 3s, \bar{x} + 3s]$.

# ## Questão 3
# 
# Qual é a diferença entre as médias e as variâncias das variáveis `binomial` e `normal`? Responda como uma tupla de dois elementos arredondados para três casas decimais.
# 
# Em outras palavras, sejam `m_binom` e `v_binom` a média e a variância da variável `binomial`, e `m_norm` e `v_norm` a média e a variância da variável `normal`. Quais as diferenças `(m_binom - m_norm, v_binom - v_norm)`?

# In[24]:


def q3():
#     Calcula e subtrai a média binomial da média normal
    mean_norm_bin = round(np.mean(dataframe['binomial']) - np.mean(dataframe['normal']), 3)
#     Calcula e subtrai a variância binomial da variância normal
    var_norm_bin = round(np.var(dataframe['binomial']) - np.var(dataframe['normal']), 3)
    return (mean_norm_bin, var_norm_bin)


# Para refletir:
# 
# * Você esperava valore dessa magnitude?
# * Qual o efeito de aumentar ou diminuir $n$ (atualmente 100) na distribuição da variável `binomial`?

# ## Parte 2

# ### _Setup_ da parte 2

# In[31]:


stars = pd.read_csv("pulsar_stars.csv")

stars.rename({old_name: new_name
              for (old_name, new_name)
              in zip(stars.columns,
                     ["mean_profile", "sd_profile", "kurt_profile", "skew_profile", "mean_curve", "sd_curve", "kurt_curve", "skew_curve", "target"])
             },
             axis=1, inplace=True)

stars.loc[:, "target"] = stars.target.astype(bool)


# ## Inicie sua análise da parte 2 a partir daqui

# In[32]:


# Sua análise da parte 2 começa aqui.
stars.head(7)


# ## Questão 4
# 
# Considerando a variável `mean_profile` de `stars`:
# 
# 1. Filtre apenas os valores de `mean_profile` onde `target == 0` (ou seja, onde a estrela não é um pulsar).
# 2. Padronize a variável `mean_profile` filtrada anteriormente para ter média 0 e variância 1.
# 
# Chamaremos a variável resultante de `false_pulsar_mean_profile_standardized`.
# 
# Encontre os quantis teóricos para uma distribuição normal de média 0 e variância 1 para 0.80, 0.90 e 0.95 através da função `norm.ppf()` disponível em `scipy.stats`.
# 
# Quais as probabilidade associadas a esses quantis utilizando a CDF empírica da variável `false_pulsar_mean_profile_standardized`? Responda como uma tupla de três elementos arredondados para três casas decimais.

# In[52]:


def q4():
#     Filtrando os valores de mean_profile para target == 0 e colocando em modo ascendente
    mean_profile = stars['mean_profile'][stars.target == 0]
    mean_profile = sorted(mean_profile)
#     Padronizando mean_profile e criando variável false_pulsar_mean_profile_standardized
    mean_mean_profile = np.mean(mean_profile)
    std_mean_profile = np.std(mean_profile)
    false_pulsar_mean_profile_standardized = (mean_profile - mean_mean_profile) / std_mean_profile
#     Define os quantis de false_pulsar_mean_profile_standardized
    quantil_mean_profile = np.percentile(false_pulsar_mean_profile_standardized, 0.80),np.percentile(false_pulsar_mean_profile_standardized, 0.90),np.percentile(false_pulsar_mean_profile_standardized, 0.95)
#     Mostra os quantis teóricos
    quantis_teoricos = sct.norm.ppf(0.80), sct.norm.ppf(0.90), sct.norm.ppf(0.95)
#     Define a probabilidade nos quantis de false_pulsar_mean_profile_standardized
    ecdf_pulsar = ECDF(false_pulsar_mean_profile_standardized)
    standard_prob_mean = ecdf_pulsar(quantis_teoricos)
    standard_prob_mean = tuple(standard_prob_mean.round(3))

    return standard_prob_mean


# In[53]:


q4()


# Para refletir:
# 
# * Os valores encontrados fazem sentido?
# * O que isso pode dizer sobre a distribuição da variável `false_pulsar_mean_profile_standardized`?

# ## Questão 5
# 
# Qual a diferença entre os quantis Q1, Q2 e Q3 de `false_pulsar_mean_profile_standardized` e os mesmos quantis teóricos de uma distribuição normal de média 0 e variância 1? Responda como uma tupla de três elementos arredondados para três casas decimais.

# In[77]:


def q5():
#     Definindo os quantis teóricos
    quantis_teoricos = sct.norm.ppf(0.25), sct.norm.ppf(0.50), sct.norm.ppf(0.75)
#     Definindo os quantis de false_pulsar_mean_profile_standardized
    mean_profile = stars['mean_profile'][stars.target == False]
    mean_profile = sorted(mean_profile)
    mean_mean_profile = np.mean(mean_profile)
    std_mean_profile = np.std(mean_profile)
    false_pulsar_mean_profile_standardized = (mean_profile - mean_mean_profile) / std_mean_profile
    quantis_false_pulsar = np.percentile(false_pulsar_mean_profile_standardized, 25), np.percentile(false_pulsar_mean_profile_standardized, 50), np.percentile(false_pulsar_mean_profile_standardized, 75)
#     Determina diferença entre os quantis
    diferenca_quantis = round(quantis_false_pulsar[0] - quantis_teoricos[0], 3), round(quantis_false_pulsar[1] - quantis_teoricos[1], 3), round(quantis_false_pulsar[2] - quantis_teoricos[2], 3)
    return diferenca_quantis


# In[78]:


q5()


# Para refletir:
# 
# * Os valores encontrados fazem sentido?
# * O que isso pode dizer sobre a distribuição da variável `false_pulsar_mean_profile_standardized`?
# * Curiosidade: alguns testes de hipóteses sobre normalidade dos dados utilizam essa mesma abordagem.

# In[ ]:




