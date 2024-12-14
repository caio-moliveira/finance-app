import streamlit as st
from controller.loader import load_accounts, load_categories, load_nome_categories_by_tipo, load_nome_accounts, load_transactions_by_year_and_selected_months
from controller.insert import insert_categories_rows, insert_transactions_rows, insert_accounts_rows
from controller.detele import delete_rows_transactions_by_id, delete_rows_categories_by_id, delete_rows_accounts_by_id
from handlers import processing
from utils import dataframe_helpers

TIPOS = ['Entrada', 'Saida']

@st.fragment()
@st.dialog("Registrar Transação")
def register_transaction():
    with st.container(height=400):
        transaction = processing.Transaction()
        transaction.tipo = st.selectbox('Tipo', TIPOS)
        transaction.descricao = st.text_area("Descrição")
        transaction.valor = st.number_input("Valor")
        transaction.lancamento = st.date_input("Laçamento", format="DD/MM/YYYY")
        transaction.vencimento = st.date_input("Vencimento", format="DD/MM/YYYY")
        with st.container(border=True):
            col1, col2 = st.columns(2)
            if _ := col1.toggle('Efetivado', value=True, disabled=True):
                transaction.efetivacao = col2.date_input(
                    "Efetivação", format="DD/MM/YYYY", label_visibility='collapsed',
                    help='Data de efetivação!'
                )
        categories = load_nome_categories_by_tipo(transaction.tipo)
        transaction.categoria = st.selectbox("Categoria", categories)
        subcategorias = []
        transaction.subcategoria = st.selectbox("Subcategorias", subcategorias)
        cartoes = []
        transaction.cartao = st.selectbox('Cartão', cartoes)
        accounts = load_nome_accounts()
        transaction.conta = st.selectbox("Conta", accounts)

    col_salvar, col_cancelar = st.columns(2)
    if col_salvar.button("Salvar ✅"):
        insert_transactions_rows(transaction.get_df())
        st.rerun()
    
    if col_cancelar.button("Cancelar ❌"):
        st.rerun()
        
        
@st.fragment()
@st.dialog("Registrar Categoria")
def register_categorie():
    categorie = processing.Categorie()
    categorie.nome = st.text_input("Nome")
    categorie.tipo = st.selectbox("Tipo", TIPOS)
    categorie.lancamento = st.date_input("Lançamento", format="DD/MM/YYYY", disabled=True)
    
    col_salvar, col_cancelar = st.columns(2)
    if col_salvar.button("Salvar ✅"):
        insert_categories_rows(categorie.get_df())
        st.rerun()
    
    if col_cancelar.button("Cancelar ❌"):
        st.rerun()


@st.fragment()
@st.dialog("Registrar Conta")
def register_account():
    account = processing.Account()
    account.nome = st.text_input("Nome")
    account.lancamento = st.date_input("Lançamento", format="DD/MM/YYYY", disabled=True)

    col_salvar, col_cancelar = st.columns(2)
    if col_salvar.button("Salvar ✅"):
        insert_accounts_rows(account.get_df())
        st.rerun()
    
    if col_cancelar.button("Cancelar ❌"):
        st.rerun()


@st.fragment()
@st.dialog("Excluir transação", width="large")
def delete_transaction():
    df = load_transactions_by_year_and_selected_months(
        st.session_state["ano_selected"],
        st.session_state["meses_selected"]
    )
    
    if not dataframe_helpers.check_empty_df(df):
        df = df.copy()
    
        if not "Excluir" in df.columns:
            df.insert(0, "Excluir", False)
            
    df_editado = st.data_editor(
        df, 
        use_container_width=True, hide_index=True
    )
    
    col_excluir, col_cancelar = st.columns(2)
    if col_excluir.button("Excluir ✅"):
        delete_rows_transactions_by_id(df_editado)
        st.rerun()

    if col_cancelar.button("Cancelar ❌"):
        st.rerun()


@st.fragment()
@st.dialog("Excluir categoria", width="large")
def delete_categorie():
    df = load_categories()
    if not dataframe_helpers.check_empty_df(df):
        df = df.copy()
        
        if not "Excluir" in df.columns:
            df.insert(0, "Excluir", False)
            
    df_editado = st.data_editor(
        df, 
        use_container_width=True, hide_index=True
    )
    col_excluir, col_cancelar = st.columns(2)
    
    if col_excluir.button("Excluir ✅"):
        delete_rows_categories_by_id(df_editado)
        st.rerun()

    if col_cancelar.button("Cancelar ❌"):
        st.rerun()


@st.fragment()
@st.dialog("Excluir conta", width="large")
def delete_account():
    df = load_accounts()
        
    if not dataframe_helpers.check_empty_df(df):
        df = df.copy()
        
        if not "Excluir" in df.columns:
            df.insert(0, "Excluir", False)
            
    df_editado = st.data_editor(
        df, 
        use_container_width=True, hide_index=True
    )
    col_excluir, col_cancelar = st.columns(2)
    if col_excluir.button("Excluir ✅", key='delete-excluir'):
        delete_rows_accounts_by_id(df_editado)
        st.rerun()

    if col_cancelar.button("Cancelar ❌", key='delete-cancelar'):
        st.rerun()
