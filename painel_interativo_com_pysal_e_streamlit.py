# -*- coding: utf-8 -*-
"""Painel interativo com Pysal e Streamlit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tiIdNwbEt6mjXIyQ8WD5XeCIC6evNXE8

# **Painel interativo com PySal e Streamlit**
O objetivo deste projeto é criar um painel interativo com dados geoestatísticos da Península de Itapagipe, Salvador-BA. Área alvo de vários investimentos estatais com víeis turísticos. Afim de comparar dados dos censos 2000 e 2010.
"""

#Importando os dados
import geopandas as gpd
df = 'dados/Bairros_Itapagipe.geojson'

ssa = gpd.read_file(df)
# ssa.plot()

#Visualizando a tabela de atributos 
# ssa

#Renomeando as colunas 
columns = {
        'NM_BAIRROS' : 'nome',
        'Cod_bairro' : 'código',
        'Id' : 'id',
        'pop_t_2000' : 'população_total_2000',
        'pop_t_2010' : 'população_total_2010',
        'pop_h_2000' : 'homens_2000',
        'pop_h_2010' : 'homens_2010',
        'pop_m_2000' : 'mulheres_2000',
        'pop_m_2010' : 'mulheres_2010',
        '0_14_2000' : 'idade_0_a_14_2000',
        '0_14_2010' : 'idade_0_a_14_2010',
        '15_64_2000' : 'idade_15_a_64_2000',
        '15_64_2010' : 'idade_15_a_64_2010',
        '65+_2000' : 'idade_65+_2000',
        '65+_2010' : 'idade_65+_2010',
        'pt_na_2000' : 'população_não_alfabetizada_2000',
        'pt_na_2010' : 'população_não_alfabetizada_2010',
        'ren_m_2000' : 'renda_média_2000',
        'rem_m_2010' : 'renda_média_2010',
        'dom_p_2000' : 'domicílios_particulares_2000',
        'dom_p_2010' : 'domicílios_particulares_2010',
        'dom_s_2000' : 'domicílios_subnormais_2000',
        'dom_s_2010' : 'domicílios_subnormais_2010',
        'IDHM_2000' : 'idhm_2000',
        'IDHM_2010' : 'idhm_2010',
        'infra_2000' : 'infraestrutura_2000',
        'infra_2010' : 'infraestrutura_2010',
        'dens_2000' : 'densidade_demográfica_2000',
        'dens_2010' : 'densidade_demográfica_2010',
        'Y' : 'latitude',
        'X' : 'longitude'
}

# #Visualizando os dados
# import geopandas as gpd
data = gpd.read_file(df, index_col='Cod_bairro')
# data.head

#Visualizando a tabela de atributos renomeada 
data = data.rename(columns=columns)
# data.head()

#Transformando a tabela em lista
# data[list(columns.values())]

# #Visualizando os dados únicos 
# data.nome.unique().tolist()

#Convertendo os dados para SIRGAS 2000 - UTM 24S
bairros = gpd.read_file('dados/Bairros_Itapagipe.geojson')
bairros = bairros.to_crs(31984)

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# from streamlit_folium import folium_static
# import folium
# import seaborn as sns
# import geopandas as gpd
# import pandas as pd
# import plotly.express as px
# import libpysal as lps
# import mapclassify 
# import numpy as np
# import esda
# import contextily as cx
# import matplotlib.pyplot as plt
# from libpysal.weights.contiguity import Queen

# Commented out IPython magic to ensure Python compatibility.
# #Importando as bibliotecas 
# %%writefile app.py
import streamlit as st
from streamlit_folium import folium_static
import folium
import seaborn as sns
import geopandas as gpd
import pandas as pd
import plotly.express as px
import libpysal as lps
import mapclassify 
import numpy as np
import esda
import contextily as cx
import matplotlib.pyplot as plt
from libpysal.weights.contiguity import Queen

# Carregando os dados
polygons = gpd.read_file('dados/Bairros_Itapagipe.geojson')
points = gpd.read_file('dados/Bairros_Itapagipe_pt.geojson')

dados = pd.read_csv('dados/Tabela_bairros.csv', encoding='UTF-8')
dados_r = pd.read_csv('dados/Tabela_bairros_r.csv', encoding='UTF-8')

bairros = gpd.read_file('dados/Bairros_Itapagipe.geojson')
bairros_pt = gpd.read_file('dados/Bairros_Itapagipe_pt.geojson')
ssa_bairros = gpd.read_file('dados/SSA_Bairros.geojson')

#Layout
st.title('Península de Itapagipe')
st.sidebar.title('Península de Itapagipe')
paginas = ['Página Inicial','Dados', 'Metadados','Gráficos','Mapas','Mapas geoestatísticos','Informações']
pagina = st.sidebar.selectbox('Selecione a página', paginas)
st.sidebar.markdown('# Painel interativo')

st.sidebar.markdown(
    """
    O objetivo deste projeto é apresentar um painel interativo com dados geoestatísticos da Península de Itapagipe, Salvador-BA. 
    Afim de comparar dados dos censos 2000 e 2010.
    """
)

st.sidebar.markdown('# Produção')
st.sidebar.image('dados/UNEB-PROET.jpg', use_column_width = 'always')


if pagina == 'Página Inicial':
    st.markdown('# Página Inicial')
    st.image('dados/I5.jpg', width = 400, use_column_width = 'always')

    st.markdown(
        """
        A Península de Itapagipe tem localização lindeira à Baía de Todos os Santos, topografia suave e clima refrescante, é uma área que tem
        vida própria, guardando ainda em muitos locais, um estilo de vida tradicional, sob muitos aspectos, no qual o sentido de pertencimento
        faz-se presente nas relações com o lugar e com os vizinhos, que ainda mantêm em vários bairros, o hábito de colocar as cadeiras na 
        porta e “prosear” com a vizinhança. 
        """
    )

    st.markdown(
        """
        A Península de Itapagipe fica localizada a poucos 8km do centralizado Mercado Modelo de Salvador (BA) Para quem quer adentrar na diversidade 
        de atrações de Salvador, fugindo dos roteiros tradicionais, um passeio pelo bairro do Bomfim e adjacências, ao domingo, é a medida completa 
        para se conhecer a autêntica baianidade.
        """
    )

    st.markdown('# Painel interativo')
    st.markdown(
        """
     O objetivo deste projeto é apresentar um painel interativo com dados geoestatísticos da Península de Itapagipe, Salvador-BA. 
     Área alvo de vários investimentos estatais com víeis turísticos. Afim de comparar dados com base nos censos dos anos de 2000 e 2010.
     Os usuários esperados são, principalmente, estudantes e pesquisadores, mas este projeto tem a intenção de apresentar 
     informações de forma clara, buscando assim, atender ao interesse de qualquer pessoa que tenha acesso.
        """
    )

    st.markdown('# Produção')
    st.markdown(
        """
    Este projeto está sendo desenvolvido por Jaqueline Lima Amorim, Urbanista (UNEB, 2018) e Mestranda do programa de Pós-graduação de 
    Estudos Territoriais da Universidade do Estado da Bahia, tendo este projeto como parte da sua pesquisa atual.
        """
    )

if pagina == 'Dados':
    st.header('Dados')
    if st.checkbox("  Mostrar tabela de dados"):
        st.subheader("  Tabela de dados")
        st.write(dados_r) 

    if st.checkbox("Mostrar tabela da média dos dados"):
        st.subheader("Tabela da média dos dados")
        st.write(dados_r .describe())

    var = st.selectbox('Selecione uma variável - 2000', ['população_total_2000','homens_2000','mulheres_2000',
                                                'idade_0_a_14_2000','idade_15_a_64_2000','idade_65+_2000',
                                                'população_não_alfabetizada_2000','renda_média_2000',
                                                'domicílios_particulares_2000','domicílios_subnormais_2000',
                                                'infraestrutura_2000','densidade_demográfica_2000',
                                                'idhm_2000'])

    pt = dados_r['nome'].groupby(dados[var]).sum()
    st.table(pt)

    var1 = st.selectbox('Selecione uma variável - 2010', ['população_total_2010','homens_2010','mulheres_2010',
                                                'idade_0_a_14_2010','idade_15_a_64_2010','idade_65+_2010',
                                                'população_não_alfabetizada_2010','renda_média_2010',
                                                'domicílios_particulares_2010','domicílios_subnormais_2010',
                                                'infraestrutura_2010','densidade_demográfica_2010',
                                                'idhm_2010'])

    ptr = dados_r['nome'].groupby(dados[var1]).sum()
    st.table(ptr)


if pagina == 'Metadados':
    st.header('Metadados')

    st.markdown(
        """
        - **Nome:** Nome dos bairros que fazem parte da Península de Itapagipe segundo, a delimitação do Plano Diretor virgente.
        - **População_total_2000:** Número total da população dos bairros da Península de Itapagipe. (Fonte: Equipe observaSSA, 2018)
        - **População_total_2010:** Número total da população por bairro da Península de Itapagipe. (Fonte: Equipe observaSSA, 2018)
        - **Homens_2000:** Porcentagem de homens por bairro da Península de Itapagipe. (Fonte: Equipe observaSSA, 2018)
        - **Homens_2010:** Porcentagem de homens por bairro da Península de Itapagipe. (Fonte: Equipe observaSSA, 2018)
        - **Mulheres_2000:** Porcentagem de mulheres por bairro da Península de Itapagipe. (Fonte: Equipe observaSSA, 2018)
        - **Mulheres_2010:** Porcentagem de mulheres por bairro da Península de Itapagipe. (Fonte: Equipe observaSSA, 2018)
        - **Idade_0_a_14_2000:** Porcentagem da população total entre as idades de 0 a 14 anos por bairro da Península de Itapagipe. (Fonte: quipe observaSSA, 2018)
        - **Idade_0_a_14_2010:** Porcentagem da população total entre as idades de 0 a 14 anos por bairro da Península de Itapagipe. (Fonte: Equipe observaSSA, 2018)
        - **Idade_15_a_64_2000:** Porcentagem da população total entre as idades de 15 a 64 anos por bairro da Península de Itapagipe. (Fonte: Equipe observaSSA, 2018)
        - **Idade_15_a_64_2010:** Porcentagem da população total entre as idades de 15 a 64 anos por bairro da Península de Itapagipe. (Fonte: Equipe observaSSA, 2018)
        - **Idade_65+_2000:** Porcentagem da população total com idade acima de 65 anos por bairro da Península de Itapagipe. (Fonte: Equipe observaSSA, 2018)
        - **Idade_65+_2010:** Porcentagem da população total com idade acima de 65 anos por bairro da Península de Itapagipe. (Fonte: Equipe observaSSA, 2018)
        - **População_não_alfabetizada_2000:** Porcentagem da população , não alfabetizada, com idade acima de 15 anos por bairro da Península de Itapagipe. (Fonte: Equipe observaSSA, 2018)
        - **População_não_alfabetizada_2010:** Porcentagem da população , não alfabetizada, com idade acima de 15 anos por bairro da Península de Itapagipe. (Fonte: Equipe observaSSA, 2018)
        - **Renda_média_2000:** Rendimento médio do responsável pelo domicílio particular permanente por bairro da Península de Itapagipe. (Fonte: Equipe observaSSA, 2018)
        - **Renda_média_2010:** Rendimento médio do responsável pelo domicílio particular permanente por bairro da Península de Itapagipe. (Fonte: Equipe observaSSA, 2018)
        - **Domicílios_particulares_2000:** Número total de domicílios particulares permanentes por bairro da Península de Itapagipe. (Fonte: Equipe observaSSA, 2018)
        - **Domicílios_particulares_2010:** Número total de domicílios particulares permanentes por bairro da Península de Itapagipe. (Fonte: Equipe observaSSA, 2018)
        - **Domicílios_subnormais_2000:** Número total de domicílios subnormal por bairro da Península de Itapagipe. (Fonte: Equipe observaSSA, 2018) 
        - **Domicílios_subnormais_2010:** Número total de domicílios subnormal por bairro da Península de Itapagipe. (Fonte: Equipe observaSSA, 2018) 
        - **Infraestrutura_2000:** Porcentagem da infraestrutura dos domicílios particulares permanentes (Coleta de lixo, Abastecimento de água e Esgotamento sanitário). (Fonte: Equipe observaSSA, 2018)
        - **Infraestrutura_2010:** Porcentagem da infraestrutura dos domicílios particulares permanentes (Coleta de lixo, Abastecimento de água e Esgotamento sanitário). (Fonte: Equipe observaSSA, 2018)
        - **Densidade_demográfica_2000:** Densidade demogáfica (hab/ha). (Fonte: CONDER/ INFORMS, Equipe observaSSA, 2018)
        - **Densidade_demográfica_2010:** Densidade demogáfica (hab/ha). (Fonte: CONDER/ INFORMS, Equipe observaSSA, 2018)
        - **IDHM_2000:** Índice de Desenvolvimento Humano Municipal (Longevidade, Educação e Renda. O índice varia de 0 a 1). (PNUD - Programa das Nações Unidas para o Desenvolvimento, 2020) 
        - **IDHM_2010:** Índice de Desenvolvimento Humano Municipal (Longevidade, Educação e Renda. O índice varia de 0 a 1). (PNUD - Programa das Nações Unidas para o Desenvolvimento, 2020) 
        """
    )

if pagina == 'Gráficos':
    st.header('Gráficos')

    st.subheader(" População total por bairros em 2010")
    result = dados.groupby(["nome"])['população_total_2010'].aggregate(np.median).reset_index().sort_values('população_total_2010')
    nDf = result[result['população_total_2010']>0]
    plt.figure(figsize=(13,7))
    sns.barplot(y='nome',x='população_total_2010', data = nDf)
    plt.xlabel('População total 2010')
    plt.ylabel('Bairros')
    st.pyplot(plt)
    plt.clf()


    st.subheader(" Dados por bairro em função da população total - 2000")
    var_2 = st.selectbox('Selecione uma variável - 2000', ['homens_2000','mulheres_2000',
                                                'idade_0_a_14_2000','idade_15_a_64_2000','idade_65+_2000',
                                                'população_não_alfabetizada_2000','renda_média_2000',
                                                'domicílios_particulares_2000','domicílios_subnormais_2000',
                                                'infraestrutura_2000','densidade_demográfica_2000',
                                                'idhm_2000'])


    ptr = dados_r['população_total_2000'].groupby(dados_r[var_2]).sum().plot(kind = 'barh')
    st.pyplot(plt)
    plt.clf()

    st.subheader(" Dados por bairro em função da população total - 2010")
    var_3 = st.selectbox('Selecione uma variável - 2010', ['homens_2010','mulheres_2010',
                                                'idade_0_a_14_2010','idade_15_a_64_2010','idade_65+_2010',
                                                'população_não_alfabetizada_2010','renda_média_2010',
                                                'domicílios_particulares_2010','domicílios_subnormais_2010',
                                                'infraestrutura_2010','densidade_demográfica_2010',
                                                'idhm_2010'])

    ptr = dados_r['população_total_2010'].groupby(dados_r[var_3]).mean().plot(kind = 'barh')
    st.pyplot(plt)
    plt.clf()


if pagina == 'Mapas':
    st.header('Mapas')

    
    def main():
      bairros = gpd.read_file('dados/Bairros_Itapagipe.geojson')
      bairros_pt = gpd.read_file('dados/Bairros_Itapagipe_pt.geojson')
      ssa_bairros = gpd.read_file('dados/SSA_Bairros.geojson')

      st.subheader("Mapa da população total dos bairros da Península de Itapagipe 2000")
      m = folium.Map (location = [-12.93,-38.50],
                    tiles = 'Stamen Terrain',
                    zoom_start = 13 
                    )

      bins = list(bairros['população_total_2000'].quantile([0, 0.25, 0.5, 0.75, 1]))
      folium.Choropleth(
      geo_data=bairros,
      name='população_total_2000',
      columns=['código', 'população_total_2000'],
      data=bairros,
      key_on='feature.properties.código',
      fill_color='YlGnBu',
      legend_name='População total 2000',
      bins=bins,
      reset=True
      ).add_to(m)

      folium_static(m)
      n = folium.Map (location = [-12.93,-38.50],
                    tiles = 'Stamen Terrain',
                    zoom_start = 13
                    )

      st.subheader("Mapa da população total dos bairros da Península de Itapagipe 2010")
      bins = list(bairros['população_total_2010'].quantile([0, 0.25, 0.5, 0.75, 1]))
      folium.Choropleth(
      geo_data=bairros,
      name='população_total_2010',
      columns=['código', 'população_total_2010'],
      data=bairros,
      key_on='feature.properties.código',
      fill_color='YlGnBu',
      legend_name='População total 2010',
      bins=bins,
      reset=True
      ).add_to(n)

      folium_static(n)


    if __name__ == '__main__':
          main()


if pagina == 'Mapas geoestatísticos':
    st.header('Mapas geoestatísticos')

    st.subheader("Mapa de autocorelação espacial")
    st.markdown(
        """
        Autocorelação espacial
        O conceito de autocorrelação espacial está relacionado com a combinação de dois tipos de similitude espacial: 
        semelhança e semelhança de atributos. É um método de correlação que considera a distribuição de variáveis do 
        problema em um espaço físico considerado. É uma estatística muito útil quando desejamos considerar a distribuição 
        espacial de determinadas variáveis do nosso problema. A ideia é determinar se valores similares encontram-se agrupados, 
        dispersos ou distribuídos aleatoriamente no espaço, ou seja, se existe alguma tendência desses valores no espaço.
        """
    )

    fig, ax = plt.subplots(figsize=(10,7))

    bairros.dropna(subset=['população_total_2010']).to_crs(epsg=31984).plot('população_total_2010', legend=True, 
    linewidth=0.1, ax=ax, edgecolor='white')

    cx.add_basemap(ax, source=cx.providers.Stamen.TonerLite)
    ax.axis('off')

    plt.title('População total dos bairros da Península de Itapagipe 2010 (Quantil)', fontsize=16)

    plt.axis('off')
    st.pyplot(plt)
    plt.clf()

    st.subheader("Mapa de semelhança espaciais")
    st.markdown(
        """
        Semelhança espacial
        Já encontramos pesos espaciais na análise de autocorrelação espacial, 
        os pesos espaciais são utilizados para formalizar a noção de semelhança espacial, há muitas formas 
        de definir pesos, aqui usaremos a contiguidade Queen ou Análise Bivariada. Na análise bivariada, por outro lado, 
        é avaliado o grau de variação espacial de uma variável em relação a outra variável.Deseja-se com esse método 
        identificar se duas variáveis estão correlacionadas no espaço, ou seja, se seguem a mesma tendência espacial. 
        """
    )

    wq = lps.weights.Queen.from_dataframe(bairros)
    wq.transform = 'r'
    y = bairros['população_total_2010']
    ylag = lps.weights.lag_spatial(wq,y)
    f, ax = plt.subplots(1, figsize=(10,9))

    bairros.assign(cl=ylag).plot(column='cl', scheme='quantiles',
      k=5, cmap='GnBu', linewidth=0.1, ax=ax,
      edgecolor='white', legend=True)

    cx.add_basemap(ax, source=cx.providers.Stamen.TonerLite)
    ax.axis('off')

    plt.title('População total dos bairros da Península de Itapagipe 2010 ', fontsize=16)

    plt.plot()
    st.pyplot(plt)
    plt.clf()


    st.subheader("Mapa de comparação dos dados")
    st.markdown(
        """
        Comparação entre os dados do censo de 2000 e 2010 (IBGE) 
        """
    )

    bairros['população_total_2010'] = ylag

    f,ax = plt.subplots(1,2,figsize=(15,10))

    bairros.plot(column='população_total_2000', ax=ax[0],
      scheme='quantiles', k=5, cmap='GnBu')

    ax[0].set_title('População 2000', fontsize=16)

    bairros.plot(column='população_total_2010', ax=ax[1],
      scheme='quantiles', k=5, cmap='GnBu')

    cx.add_basemap(ax[0], crs=bairros.crs.to_string(), source=cx.providers.Stamen.TonerLite)

    cx.add_basemap(ax[1], crs=bairros.crs.to_string(), source=cx.providers.Stamen.TonerLite)

    ax[1].set_title('População 2010', fontsize=16)
    ax[0].axis('off')
    ax[1].axis('off')
    plt.axis('off')
    st.pyplot(plt)
    plt.clf()

if pagina == 'Informações':
    st.header('Informações')

    st.header('Contato')
    st.markdown(
        """
        Email - jaqueline.urb15@gmail.com
        """
    )

    st.header('Para mais informações')
    st.markdown(
        """
        Para mais informações acessar o site Equipe observaSSA:
        """
    )
    st.write("Acesse esse [link](https://observatoriobairrossalvador.ufba.br/)")

    st.header('Novidades')
    st.markdown(
        """
        Em breve será disponibilixado aqui o link para o plano de bairros da Península de Itapagipe (Prefeitura de Salvador, 2021),
        e demais planos incidentes na área.
        """
    )

