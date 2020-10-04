import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as sm

dtfram_enem_2016 = pd.read_csv('D:/Git Files/DesafiosCodeNation/datascience/testfiles/train_menos_variáveis.csv')
dtfram_enem_2016 = dtfram_enem_2016.drop(['Unnamed: 0'], axis = 1)

dtfram_enem_2016.isnull().sum()

dtfram_enem_2016 = dtfram_enem_2016.dropna(subset=['NU_NOTA_LC'])
dtfram_enem_2016 = dtfram_enem_2016.dropna(subset=['NU_NOTA_CH'])
dtfram_enem_2016 = dtfram_enem_2016.dropna(subset=['NU_NOTA_CN'])
dtfram_enem_2016 = dtfram_enem_2016.dropna(subset=['NU_NOTA_MT'])
dtfram_enem_2016 = dtfram_enem_2016.fillna(dtfram_enem_2016['NU_NOTA_LC'].mean)

dtfram_enem_2016_notalc = dtfram_enem_2016.loc[dtfram_enem_2016['NU_NOTA_LC']!=0]
dtfram_enem_2016_notalc = dtfram_enem_2016_notalc.loc[dtfram_enem_2016_notalc['NU_NOTA_CH']!=0]
dtfram_enem_2016_notalc = dtfram_enem_2016_notalc.loc[dtfram_enem_2016_notalc['NU_NOTA_CN']!=0]
dtfram_enem_2016_notalc = dtfram_enem_2016_notalc.loc[dtfram_enem_2016_notalc['NU_NOTA_MT']!=0]

x_nota_lc = dtfram_enem_2016_notalc.loc[ : ,'NU_NOTA_LC'].values
y_nota_ch = dtfram_enem_2016_notalc.loc[ : ,'NU_NOTA_CH'].values
y_nota_cn = dtfram_enem_2016_notalc.loc[ : ,'NU_NOTA_CN'].values
y_nota_mt = dtfram_enem_2016_notalc.loc[ : ,'NU_NOTA_MT'].values

correlacao_notalc_notach = np.corrcoef(x_nota_lc,y_nota_ch)
correlacao_notalc_notacn = np.corrcoef(x_nota_lc,y_nota_cn) 
correlacao_notalc_notamt = np.corrcoef(x_nota_lc,y_nota_mt)

plt.scatter(x_nota_lc,y_nota_ch)
plt.scatter(x_nota_lc,y_nota_cn)
plt.scatter(x_nota_lc,y_nota_mt)

x_nota_lc = x_nota_lc.reshape(-1, 1)

modelo_lc = LinearRegression()
modelo_lc.fit(x_nota_lc, y_nota_ch)
modelo_lc.intercept_
modelo_lc.coef_

modelo_lc.score(x_nota_lc,y_nota_ch)
previsoes = modelo_lc.predict(x_nota_lc)
modelo_lc_ajustado = sm.ols(formula = 'NU_NOTA_LC ~ NU_NOTA_CH + NU_NOTA_CN + NU_NOTA_MT', data = dtfram_enem_2016_notalc)
modelo_lc_treinado = modelo_lc_ajustado.fit()
modelo_lc_treinado.summary()

plt.scatter(x_nota_lc, y_nota_ch)
plt.plot(x_nota_lc, previsoes, color ='r')



