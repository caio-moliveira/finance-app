from templates.sidebar import menu
from templates.metrics import dashboard_metric
from templates.graphcs import (
    spending_by_category_bar_chart,
    monthly_spending_trends,
    recurring_transactions_dashboard,
    budget_vs_actual_dashboard,
    transaction_table_with_filters
)
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

    # Check if the DataFrame is empty
    if check_empty_df(df):
        st.toast("No data available to generate graphs", icon="🚨")
        st.stop()

    # Sidebar inputs for user goals
    savings_goal = st.sidebar.number_input("Savings Goal (R$)", min_value=0, value=10000)
    monthly_budget = st.sidebar.number_input("Monthly Budget (R$)", min_value=0, value=5000)

    # Metrics at the top of the dashboard
    dashboard_metric(df, monthly_budget, savings_goal)

    # Render primary graphs
    spending_by_category_bar_chart(df)
    monthly_spending_trends(df)

    # Tabs for additional insights
    st.divider()
    tab1, tab2, tab3 = st.tabs([
        "Recurring Transactions", "Budget vs Actual", "Transaction Table"
    ])

    with tab1:
        recurring_transactions_dashboard(df)

    with tab2:
        budget_vs_actual_dashboard(df, monthly_budget)

    with tab3:
        transaction_table_with_filters(df)


if __name__ == "__main__":
    st.set_page_config(page_title="Financial Dashboard", page_icon="📊", layout="wide")
    menu()
    main()
