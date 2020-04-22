import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    st.image('codenationTD.png',format='PNG')
    st.title('AceleraDev Data Science 2020')
    st.subheader('Análise Exploratória de Dados em Python')
    file  = st.file_uploader('Escolha o dataset que deseja analisar (.csv)', type = 'csv')
    if file is not None:
        df = pd.read_csv(file)

        st.markdown('**Dimensão do Dataset**')
        st.write('Nº de obserações:', df.shape[0], ' Nº de colunas:', df.shape[1])

        st.markdown('**Resumo dos Dados**')
        select_analise = st.radio('Escolha uma análise abaixo :', ('head', 'info', 'describe'))
        if select_analise == 'head':
            st.dataframe(df.head())
        if select_analise == 'info':
            st.dataframe({'Dtype': df.dtypes, 'Non-Null Count': df.count()})
        if select_analise == 'describe':
            st.dataframe(df.describe())

        st.markdown('**Análise Gráfica**')
        if st.checkbox("Correlação com Seaborn"):
            st.markdown('Podemos observar as relações enqtre as colunas e a intensidade de cada relacionamento')
            sns.heatmap(df.corr(),annot=True)
            st.pyplot()
        if st.checkbox("Covariância com Seaborn"):
            st.markdown('Podemos observar as inter-dependência estre as colunas e como se comportam conjuntamente em relação às suas médias')
            sns.heatmap(df.cov(),annot=True)
            st.pyplot()            
        if st.checkbox("Colunas com Nulos"):
            st.markdown('Podemos observar quais as colunas possuem valores nulos e a quantidade')
            plt.barh(list(df.columns), df.isna().sum().values)
            st.pyplot()
        if st.checkbox("Histograma com Pyplot"):
            st.markdown('Podemos observar o histograma de cada coluna do dataset de acordo com a seleção abaixo')
            option = st.selectbox('Selecione uma coluna',list(df.columns))
            plt.hist(sorted(df[option].values))
            st.pyplot()
        if st.checkbox("Scatter com Pyplot"):
            st.markdown('Podemos observar dispersão entre duas colunas de acordo com a seleção abaixo')
            selecao1 = st.selectbox('Selecione a primeira coluna',list(df.columns))
            selecao2 = st.selectbox('Selecione a segunda coluna',list(df.columns))
            plt.scatter(df[selecao1],df[selecao2])
            st.pyplot()
            
        st.markdown('**Análise Estatística**')
        if st.checkbox("Gerar dados Estatísticos"):
            st.markdown('Podemos observar alguns indicadores estatísticos de acordo com a seleção abaixo')
            medida = st.selectbox('Selecione uma coluna',list(df.select_dtypes(include='number').columns))
            media = df[medida].mean()
            mediana = df[medida].median()
            moda = df[medida].mode().max()
            variancia = df[medida].var()
            desvio_p = df[medida].std()
            desvio_a = df[medida].mad()
            simetria = df[medida].skew()
            curtose = df[medida].kurtosis()
            st.dataframe({'Valor': {'1 - Média': media, '2 - Mediana': mediana, '3 - Moda': moda, '4 - Variância': variancia, '5 - Desvio Padrão': desvio_p, '6 - Desvio Absoluto': desvio_a, '7 - Simetria': simetria, '8 - Curtose': curtose}})
            #st.dataframe({'Média': [media], 'Mediana': [mediana], 'Moda': [moda], 'Desvio Padrão': [desvio]})
        
if __name__ == '__main__':
    main()
