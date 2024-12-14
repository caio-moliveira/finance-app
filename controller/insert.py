import streamlit as st
import pandas as pd
import sqlite3
from .config import (
    DATABASE, TRANSACTIONS, CATEGORIES, ACCOUNTS, USERS
)

def insert_rows(table: str, df: pd.DataFrame):
    # Conecte-se ao banco de dados (ou crie um novo se não existir)
    conn = sqlite3.connect(DATABASE)

    # Crie um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Obtenha os nomes das colunas do DataFrame
    columns = ', '.join(df.columns)
    placeholders = ', '.join(['?'] * len(df.columns))

    # Prepare a consulta SQL
    sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

    # Insira as linhas
    for _, row in df.iterrows():
        cursor.execute(sql, tuple(row.values))

    # Confirmar alterações
    conn.commit()

    # Feche a conexão
    cursor.close()
    conn.close()


def insert_transactions_rows(df: pd.DataFrame):
    insert_rows(TRANSACTIONS, df)
    st.cache_resource.clear()
    
    
def insert_categories_rows(df: pd.DataFrame):
    insert_rows(CATEGORIES, df)
    st.cache_resource.clear()
    
    
def insert_accounts_rows(df: pd.DataFrame):
    insert_rows(ACCOUNTS, df)
    st.cache_resource.clear()


def insert_user_registration(df: pd.DataFrame):
    insert_rows(USERS, df)
    st.cache_resource.clear()
    