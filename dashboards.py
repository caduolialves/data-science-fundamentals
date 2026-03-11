# biblioteca para contruir os dashboards
import streamlit as st
# biblioteca de manipulação de dados. ler/tratar dados e arquivos
import pandas as pd
# contruir gráficos
import plotly.express as px


# Ranking de repositórios mais populares do GitHub
# Linguagens mais usadas nesses repositórios
# Análise se alguma linguagem influencia na quantidade de estrelas ou forks

st.set_page_config(page_title="GitHub Trending", layout="wide")

df = pd.read_json("data/trending_repositories.json")

df