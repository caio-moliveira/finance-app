import streamlit as st
from controller.creator import create_transactions_table
from controller.loader import load_years_transactions, load_months_transactions_by_year
import calendar
from utils import autenticated_helpers

def input_period():
    # Supondo que controller já tenha as funções definidas
    create_transactions_table()
    df_anos = load_years_transactions()
    lista_de_anos = df_anos["ano"].tolist()
    ano_selected = st.selectbox("Ano", lista_de_anos)

    df_meses = load_months_transactions_by_year(ano_selected)
    lista_de_meses = df_meses["mes"].tolist()

    # Converte os números dos meses para nomes completos
    lista_de_meses_nome = [calendar.month_name[int(mes)] for mes in lista_de_meses]

    # Seleciona os nomes dos meses
    meses_nome_selected = st.multiselect("Meses", lista_de_meses_nome, lista_de_meses_nome)

    # Converte os nomes dos meses selecionados para números
    meses_selected = [str(list(calendar.month_name).index(mes_nome)).zfill(2) for mes_nome in meses_nome_selected]

    st.session_state["ano_selected"] = ano_selected
    st.session_state["meses_selected"] = meses_selected


def button_sair():
    if st.button("SAIR", type='primary', use_container_width=True):
        st.cache_data.clear()
        st.cache_resource.clear()
        st.session_state.clear()
        st.rerun()


def menu():
    if not autenticated_helpers.autenticated():
        st.switch_page("pages/0_login.py")
    else:
        with st.sidebar:
            # Usuário
            st.header(f"{str(st.session_state["username"]).upper()}", divider=True)
            
            # Links
            st.subheader("Menu", divider=True)
            st.page_link("pages/2_dashboard.py", label="Gráficos", icon="📊")
            st.page_link("pages/3_reports.py", label="Relatórios", icon="📄")
            st.page_link("pages/4_settings.py", label="Configurações", icon="⚙️")
            # Input periodo
            st.subheader("Período", divider=True)
            input_period()

            # Sair
            st.divider()
            button_sair()
