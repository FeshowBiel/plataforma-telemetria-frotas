# arquivo: frontend/app/dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import os

st.set_page_config(page_title="Inteligência de Frotas & SST", page_icon="🚚", layout="wide")

DB_USER = os.getenv("POSTGRES_USER", "admin")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "admin_password")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_NAME = os.getenv("POSTGRES_DB", "frotas_db")
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"

@st.cache_data(ttl=5)
def carregar_dados_limpos():
    try:
        engine = create_engine(DATABASE_URL)
        # 🚨 A MÁGICA AQUI: Lendo da nossa nova camada do dbt!
        query = "SELECT * FROM analytics.stg_telemetria ORDER BY data_hora_leitura DESC"
        df = pd.read_sql(query, engine)
        return df
    except Exception as e:
        st.error(f"Erro ao conectar no banco de dados: {e}")
        return pd.DataFrame()

st.title("📊 Centro de Controle Operacional: Frotas & SST")
st.markdown("Consumindo dados modelados e limpos pela camada dbt (Data Build Tool).")

if st.button("🔄 Atualizar Dados Agora"):
    st.cache_data.clear()

df = carregar_dados_limpos()

if df.empty:
    st.warning("Aguardando dados... Envie requisições via Swagger e rode o dbt!")
else:
    st.markdown("### 🎯 KPIs Globais")
    col1, col2, col3, col4 = st.columns(4)
    
    total_veiculos = df['veiculo_id'].nunique()
    alertas_fadiga = df[df['alerta_fadiga'] == True].shape[0]
    vel_maxima = df['velocidade_kmh'].max()
    cargas_perigosas = df[df['carga_perigosa_status'] != "NORMAL"].shape[0]

    col1.metric("Veículos Ativos", total_veiculos)
    col2.metric("🚨 Alertas de Fadiga (SST)", alertas_fadiga, delta_color="inverse")
    col3.metric("Velocidade Máxima", f"{vel_maxima} km/h")
    col4.metric("Cargas Perigosas", cargas_perigosas)

    st.divider()

    col_chart1, col_chart2 = st.columns(2)

    with col_chart1:
        st.markdown("#### 🌡️ Temperatura Atual do Motor")
        df_temp_atual = df.groupby('veiculo_id')['temperatura_motor_celsius'].first().reset_index()
        fig_temp = px.bar(df_temp_atual, x='veiculo_id', y='temperatura_motor_celsius', color='veiculo_id')
        st.plotly_chart(fig_temp, use_container_width=True)

    with col_chart2:
        st.markdown("#### 🛞 Análise de Pressão dos Pneus (Extraído do JSON)")
        st.info("Graças ao dbt, os dados complexos agora são colunas estruturadas prontas para análise!")
        # Mostrando as colunas limpas que o dbt gerou
        df_pneus = df[['veiculo_id', 'pressao_eixo_1_esq', 'pressao_eixo_1_dir', 'pressao_eixo_2_esq', 'pressao_eixo_2_dir']].head(5)
        st.dataframe(df_pneus, use_container_width=True)

    st.divider()
    
    st.markdown("#### 📋 Dados Analíticos (Staging - dbt)")
    st.dataframe(df, use_container_width=True)