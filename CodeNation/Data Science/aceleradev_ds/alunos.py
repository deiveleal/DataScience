import streamlit as st
import pandas as pd

#def main():
#    st.title('Hello World')
#    st.markdown('Teste de Botao')
#    botao = st.button('Botao')
#    if botao:
#        st.markdown('Clicado')
#    
#    st.markdown('Teste de Checkbox')
#    check = st.checkbox('Checkbox')
#    if check:
#        st.markdown('Clicado no Checkbox')
#
#    st.markdown('Radio')
#    radio = st.radio('Escolha as opções',('Opt 1', 'Opt 2'))
#    if radio == 'Opt 1':
#        st.markdown('Opção 1')
#    if radio == 'Opt 2':
#        st.markdown('Opção 2')
#    
#    st.markdown('Caixa de seleção (SelectBox)')
#    select = st.selectbox('Escolha a opção', ('Opt 1', 'Opt 2'))
#    if select == 'Opt 1':
#        st.markdown('Opção 1')
#    if select == 'Opt 2':
#        st.markdown('Opção 2')
#
#    st.markdown('Seleção múltipla')
#    mult = st.multiselect('Escolha as opções', ('Opt 1','Opt 2'))
#    if mult == 'Opt 1':
#        st.markdown('Opção 1')
#    if mult == 'Opt 2':
#        st.markdown('Opção 2')
#
#    st.markdown('File Uploader')
#    file = st.file_uploader('Choose you file', type='csv')
#    if file is not None:
#        st.markdown('Upload Completado com Sucesso')

def main():
    st.title('AceleraDev Data Science - Semana II')
    st.image('logo.png')
    file = st.file_uploader('Upload do arquivo', type = 'csv')
    if file is not None:
        slider = st.slider('Valores', 1, 100)
        df = pd.read_csv('IRIS.csv')
        st.dataframe(df.head(slider))

        st.markdown('Outra visualização')
        st.table(df.head(slider))

        st.markdown('Colunas')
        st.write(df.columns)

    
dic_frame = {'col':[1,2,3,4,5],'lin':[11,22,33,44,55]}
df = pd.DataFrame(data=dic_frame)
print(df_col)
df_col = df.columns



if __name__ == '__main__':
    main()