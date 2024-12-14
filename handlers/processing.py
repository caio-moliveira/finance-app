import pandas as pd
import streamlit as st

class Transaction:
    def __init__(self):
        self.user_id = st.session_state['user_id']
        self.descricao = None
        self.valor = None
        self.lancamento = None
        self.vencimento = None
        self.efetivacao = None
        self.categoria = None
        self.subcategoria = None
        self.cartao = None
        self.conta = None

    def get_df(self) -> pd.DataFrame:
        return pd.DataFrame([self.__dict__])


class Categorie:
    def __init__(self):
        self.user_id = st.session_state['user_id']
        self.nome = None
        self.lancamento = None
        self.tipo = None

    def get_df(self) -> pd.DataFrame:
        return pd.DataFrame([self.__dict__])
    

class Account:
    def __init__(self):
        self.user_id = st.session_state['user_id']
        self.nome = None
        self.lancamento = None

    def get_df(self) -> pd.DataFrame:
        return pd.DataFrame([self.__dict__])
    

class CreditCard:
    def __init__(self):
        self.user_id = st.session_state['user_id']
        self.nome = None
        self.lancamento = None
        self.fechamento = None
        self.vencimento = None
        self.limite = None

    def get_df(self) -> pd.DataFrame:
        return pd.DataFrame([self.__dict__])
    