import streamlit as st
import pandas as pd
import sqlite3
from .config import (
    DATABASE, TRANSACTIONS, CATEGORIES, ACCOUNTS, USERS
)


def load_data(table: str, cols: list):
    conn = sqlite3.connect(DATABASE)
    cols_str = ', '.join(cols)
    
    query = f"""
        SELECT {cols_str} FROM {table} WHERE user_id = ?
    """
    
    params = (st.session_state["user_id"],)
    
    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    return df


def load_nome_by_tipo(table:str, tipo: str) -> pd.DataFrame:
    # Conecte ao banco de dados com os adaptadores registrados
    conn = sqlite3.connect(DATABASE)

    query = f"""
        SELECT nome FROM {table}
        WHERE tipo = ? AND user_id = ?  
        GROUP BY nome
    """
    
    params = (tipo, st.session_state["user_id"])
    df = pd.read_sql_query(query, conn, params=params)
    
    conn.close()  # Fechar a conexão após a execução da consulta
    return df


def load_nome(table: str):
    # Conecte ao banco de dados com os adaptadores registrados
    conn = sqlite3.connect(DATABASE)

    query = f"""
        SELECT nome FROM {table} 
        WHERE user_id = ? 
        GROUP BY nome
    """
    params = (st.session_state["user_id"],)
    df = pd.read_sql_query(query, conn, params=params)

    conn.close()  # Fechar a conexão após a execução da consulta
    return df


def load_years(table: str):
    conn = sqlite3.connect(DATABASE)

    query = f"""
        SELECT DISTINCT 
            strftime('%Y', lancamento) AS ano 
        FROM {table} 
        WHERE user_id = ? 
        ORDER BY ano DESC
    """
    params = (st.session_state["user_id"],)
    df = pd.read_sql_query(query, conn, params=params)
    
    conn.close()  # Fechar a conexão após a execução da consulta
    return df


def load_months_by_year(table: str, year: str):
    conn = sqlite3.connect(DATABASE)

    query = f"""
        SELECT DISTINCT 
            strftime('%m', lancamento) AS mes 
        FROM {table} 
        WHERE strftime('%Y', lancamento) = ? AND user_id = ? 
        ORDER BY mes DESC
    """
    params = (year, st.session_state["user_id"])
    
    df = pd.read_sql_query(query, conn, params=params)
    
    conn.close()  # Fechar a conexão após a execução da consulta
    return df


def load_data_by_year_and_selected_months(table: str, selected_year: str, months: list):
    conn = sqlite3.connect(DATABASE)
    
    # Construa a cláusula IN para os meses
    placeholders = ', '.join('?' for _ in months)
    
    query = f"""
        SELECT 
            id, 
            tipo, 
            descricao, 
            valor, 
            lancamento, 
            vencimento, 
            efetivacao, 
            categoria, 
            subcategoria, 
            cartao, 
            conta 
        FROM {table}
        WHERE strftime('%Y', lancamento) = ? 
        AND strftime('%m', lancamento) IN ({placeholders}) 
        AND user_id = ? 
        ORDER BY strftime('%Y', lancamento), strftime('%m', lancamento) DESC
    """
    
    # Parâmetros combinados (ano, meses e user_id)
    params = (selected_year, *months, st.session_state["user_id"])
    
    # Execute a consulta SQL
    df = pd.read_sql_query(query, conn, params=params)
    
    conn.close()
    return df


def load_credentials(table: str, username: str, password: str) -> pd.DataFrame:
    conn = sqlite3.connect(DATABASE)

    query = f"""
        SELECT 
            * 
        FROM {table} 
        WHERE ? = username AND ? = password 
    """

    params = (username, password)

    df = pd.read_sql_query(query, conn, params=params)
    
    conn.close()
    return df


@st.cache_resource
def load_nome_categories_by_tipo(tipo: str) -> pd.DataFrame:
    """Carrega as categorias por tipo"""
    df = load_nome_by_tipo(CATEGORIES, tipo)
    return df


@st.cache_resource
def load_nome_accounts():
    """Carrega os nomes das contas"""
    df = load_nome(ACCOUNTS)
    return df


@st.cache_resource
def load_years_transactions():
    """Carrega os anos das transações cadastradas"""
    df = load_years(TRANSACTIONS)
    return df


@st.cache_resource
def load_months_transactions_by_year(year: str):
    """Carrega os meses das transações cadastradas por ano"""
    df = load_months_by_year(TRANSACTIONS, year)
    return df


@st.cache_resource
def load_transactions_by_year_and_selected_months(year: str, months: list):
    """Carrega as transações por ano e meses selecionados"""
    df = load_data_by_year_and_selected_months(TRANSACTIONS, year, months)
    return df
    

@st.cache_resource
def load_categories():
    """Carrega todas as categorias cadastradas"""
    cols = ['id', 'lancamento', 'nome', 'tipo']
    df = load_data(CATEGORIES, cols)
    return df


@st.cache_resource
def load_accounts():
    """Carrega todas as contas cadastradas"""
    cols = ['id', 'lancamento', 'nome']
    df = load_data(ACCOUNTS, cols)
    return df


def load_users_credentials(username: str, password: str) -> pd.DataFrame:
    """Carrega as credenciais no banco de dados"""
    df = load_credentials(USERS, username, password)
    return df