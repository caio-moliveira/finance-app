from templates.sidebar import menu
from templates.metrics import dashboard_metric
from templates.graphcs import entries_by_categories_dashboard, monthly_evolution_dashboard, expenses_by_categories_dashboard, balance_on_account
from utils.dataframe_helpers import check_empty_df
from controller.loader import load_transactions_by_year_and_selected_months
import streamlit as st
import locale

locale.setlocale(locale.LC_ALL, "")

def main():
    df = load_transactions_by_year_and_selected_months(
        st.session_state["ano_selected"],
        st.session_state["meses_selected"]
    )

    # Sem dados para gerar gráficos
    if check_empty_df(df):
        st.toast("Sem dados para gerar os gráficos", icon="🚨")
        st.stop()

    # Mostrando gráficos e metricas
    dashboard_metric(df)

    # Graficos categoria
    coluna_1, coluna_2 = st.columns(2)

    with coluna_1:
        # Entrada por categoria
        entries_by_categories_dashboard(df)

        # Evolução mensal
        monthly_evolution_dashboard(df)

    with coluna_2:
        # Despesas por categoria
        expenses_by_categories_dashboard(df)

        # Saldo por conta
        balance_on_account(df)

if __name__ == "__main__":
    # Configurações da página
    st.set_page_config("Gráficos", "📊", "wide")
    menu()
    main()