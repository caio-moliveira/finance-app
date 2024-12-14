import streamlit as st
from handlers import calculations


def dashboard_metric(df):
    """Metricas"""
    entradas, saidas, saldo = calculations.dashboard_metrics(df)

    # Metricas
    col_entradas, col_despesas, col_saldo = st.columns(3)

    with col_entradas.container(border=True):
        st.metric("Entradas", str(entradas))

    with col_despesas.container(border=True):
        st.metric("Saidas", str(saidas))
        
    with col_saldo.container(border=True):
        st.metric("Saldo", str(saldo))
