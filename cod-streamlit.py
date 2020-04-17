import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    st.title('AceleraDev Data Science')
    st.subheader('Semana 2 - Pré-processamento de Dados em Python')
    file  = st.file_uploader('Escolha a base de dados que deseja analisar (.csv)', type = 'csv')
    #file  = 'black_friday.csv'
    if file is not None:
        st.subheader('Exploração de Dados')
        df = pd.read_csv(file)

        st.markdown('**Dimensão do Data Frame**')
        st.write('Nº de obserações:', df.shape[0], ' Nº de colunas:', df.shape[1])

        st.markdown('**Dados**')
        select_analise = st.radio('Escolha uma analise abaixo :', ('head', 'info', 'describe'))
        if select_analise == 'head':
            st.dataframe(df.head())
        if select_analise == 'info':
            st.dataframe({'Dtype': df.dtypes, 'Non-Null Count' :df.count()})
        if select_analise == 'describe':
            st.dataframe(df.describe())

        st.markdown('**Gráficos**')
        if st.checkbox("Correlação com Seaborn"):
            sns.heatmap(df.corr(),annot=True)
            st.pyplot()
            
        if st.checkbox("Colunas com Nulos"):
            plt.barh(list(df.columns), df.isna().sum().values)
            st.pyplot()
            
        if st.checkbox("Histograma com Pyplot"):
            option = st.selectbox('Selecione a coluna',list(df.columns))
            plt.hist(sorted(df[option].values))
            st.pyplot()
            
        
if __name__ == '__main__':
	main()
