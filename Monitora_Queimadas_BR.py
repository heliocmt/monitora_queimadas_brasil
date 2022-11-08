#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import folium
import folium.plugins as plugins

# extração dos dados
tabela = pd.read_csv(r"https://queimadas.dgi.inpe.br/home/download?id=focos_brasil&time=48h&outputFormat=csv&utm_source=landing-page&utm_medium=landing-page&utm_campaign=dados-abertos&utm_content=focos_brasil_48h")

# ETL
tabela.drop(["FID", "id", "satelite", "municipio_id", "estado_id", "pais_id", "numero_dias_sem_chuva", "precipitacao","risco_fogo", "bioma", "geom"], axis=1, inplace=True)

tabela['data_hora_gmt'] = tabela['data_hora_gmt'].str.replace('T','\n').astype(str)

tabela.to_excel(r'C:\Users\helio\OneDrive\Área de Trabalho\Projeto Data Science\dados.xlsx', index=False)

dados = pd.read_excel(r"C:\Users\helio\OneDrive\Área de Trabalho\Projeto Data Science\dados.xlsx")

# armazenamento de dados em listas
coordenadas = []
for latitude, longitude in zip(dados.latitude.values[:1000], dados.longitude.values[:1000]):
        coordenadas.append([latitude, longitude])

municipios = dados['municipio'].tolist()

data = dados['data_hora_gmt'].tolist()

# criação do mapa
mapa = folium.Map(
        location=[-19.8222, -40.3381],
        zoom_start=7.5
    )
# criação das marcações
for i in range(0, len(coordenadas)):
        folium.Marker(
            location=coordenadas[i],
            popup=f'Município: {municipios[i]}\n\nRegistro: {data[i]}\n\nCoordenadas: {coordenadas[i]}',
            tooltop='Clique aqui!',
            icon=folium.Icon(color='red')
        ).add_to(mapa)
mapa.add_child(plugins.HeatMap(coordenadas))
mapa

