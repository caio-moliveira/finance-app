import streamlit as st
from controller.loader import load_transactions_by_year_and_selected_months, load_categories, load_accounts
from controller.creator import create_transactions_table, create_categories_table, create_accounts_table
from templates.dialogs import register_transaction, delete_transaction, register_categorie, delete_categorie, register_account, delete_account
import pandas as pd


@st.fragment()
def transactions():
    st.subheader("Transações")
    create_transactions_table()
    df_transactions = load_transactions_by_year_and_selected_months(
        st.session_state["ano_selected"],
        st.session_state["meses_selected"]
    )
    st.dataframe(
        df_transactions.drop(columns=['id']), 
        hide_index=True, use_container_width=True
    )
    
    col_registrar, col_deletar = st.columns(2)
    
    if col_registrar.button("➕ Registrar", key="register_transaction"):
        register_transaction()

    if col_deletar.button("❌ Deletar", key="delete_transaction"):
        delete_transaction()


@st.fragment()
def categories():
    st.subheader("Categorias")
    create_categories_table()
    df_categories = load_categories()
    st.dataframe(
        df_categories.drop(columns=['id']), 
        hide_index=True, use_container_width=True
    )
    col_registrar, col_deletar = st.columns(2)
    
    if col_registrar.button("➕ Registrar", key="register_categorie"):
        register_categorie()

    if col_deletar.button("❌ Deletar", key="delete_categorie"):
        delete_categorie()


@st.fragment()
def accounts():
    st.subheader("Contas")
    create_accounts_table()
    df_accounts = load_accounts()
    st.dataframe(
        df_accounts.drop(columns=['id']), 
        hide_index=True, use_container_width=True
    )
    col_registrar, col_deletar = st.columns(2)

    if col_registrar.button("➕ Registrar", key="register_account"):
        register_account()
        
    if col_deletar.button("❌ Deletar", key="delete_account"):
        delete_account()
