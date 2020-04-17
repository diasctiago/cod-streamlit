import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    st.title('AceleraDev Data Science')
    st.subheader('Semana 2 - Pré-processamento de Dados em Python')
    file  = st.file_uploader('Escolha a base de dados que deseja analisar (.csv)', type = 'csv')
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
            st.dataframe({'Dtype': df.dtypes, 'Non-Null Count': df.count()})
        if select_analise == 'describe':
            st.dataframe(df.describe())

        st.markdown('**Gráficos**')
        if st.checkbox("Correlação com Seaborn"):
            st.markdown('Podemos observar as relações estre as colunas e a intensidade de cada relacionamento')
            sns.heatmap(df.corr(),annot=True)
            st.pyplot()
            
        if st.checkbox("Colunas com Nulos"):
            st.markdown('Podemos observar quais as colunas possuem valores nulos e sua quantidade')
            plt.barh(list(df.columns), df.isna().sum().values)
            st.pyplot()
            
        if st.checkbox("Histograma com Pyplot"):
            st.markdown('Podemos observar o histograma de cada coluna do dataset de acordo com a seleção abaixo')
            option = st.selectbox('Selecione a coluna',list(df.columns))
            plt.hist(sorted(df[option].values))
            st.pyplot()
            
        if st.checkbox("Scatter com Pyplot"):
            st.markdown('Podemos observar dispersão entre duas colunas de acordo com a seleção abaixo')
            selecao1 = st.selectbox('Selecione a primeira coluna',list(df.columns))
            selecao2 = st.selectbox('Selecione a segunda coluna',list(df.columns))
            plt.scatter(df[selecao1],df[selecao2])
            st.pyplot()
            
        st.markdown('**Estatísticas**')
        if st.checkbox("Gerar dados Estatísticos"):
            st.markdown('Podemos observar alguns dados estatísticos de acordo com a seleção abaixo')
            medida = st.selectbox('Selecione a coluna',list(df.select_dtypes(include='number').columns))
            media = df[medida].mean()
            mediana = df[medida].median()
            moda = df[medida].mode().max()
            st.table({'Média': [media], 'Mediana': [mediana], 'Moda': [moda]})
        
if __name__ == '__main__':
    main()
