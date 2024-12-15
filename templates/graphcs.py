import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from utils import dataframe_helpers
from controller.config import ENTRADA, SAIDA

ENTRADA = "Entrada"
SAIDA = "Saida"


def monthly_spending_trends(df):
    """Monthly Spending Trends by Category"""
    time_filter = st.selectbox("Timeframe", ["Monthly", "Weekly", "Daily"])

    if time_filter == "Monthly":
        df['month'] = pd.to_datetime(df['lancamento']).dt.to_period('M').astype(str)
        df['day'] = pd.to_datetime(df['lancamento']).dt.day  # Extract days
        grouped_df = df[df['tipo'] == SAIDA].groupby(['month', 'day', 'categoria'])['valor'].sum().reset_index()

        fig = px.line(
            grouped_df,
            x='day',
            y='valor',
            color='categoria',
            title='Spending Trends Over Days in the Month',
            labels={'valor': 'Amount (R$)', 'day': 'Day of the Month', 'categoria': 'Category'}
        )

    elif time_filter == "Weekly":
        df['week'] = pd.to_datetime(df['lancamento']).dt.to_period('W').astype(str)
        df['day_name'] = pd.to_datetime(df['lancamento']).dt.day_name()  # Extract day names
        grouped_df = df[df['tipo'] == SAIDA].groupby(['day_name', 'categoria'])['valor'].sum().reset_index()

        # Order days of the week for better visualization
        day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        grouped_df['day_name'] = pd.Categorical(grouped_df['day_name'], categories=day_order, ordered=True)

        fig = px.bar(
            grouped_df,
            x='day_name',
            y='valor',
            color='categoria',
            title='Spending Trends Over Days in the Week',
            labels={'valor': 'Amount (R$)', 'day_name': 'Day of the Week', 'categoria': 'Category'},
            barmode='stack'  # Stacked bars
        )

    elif time_filter == "Daily":
        today = pd.Timestamp.now().date()
        df['date'] = pd.to_datetime(df['lancamento']).dt.date
        daily_data = df[(df['tipo'] == SAIDA) & (df['date'] == today)].groupby(['categoria'])['valor'].sum().reset_index()

        fig = px.bar(
            daily_data,
            x='categoria',
            y='valor',
            title=f'Spending Trends for Today ({today})',
            labels={'valor': 'Amount (R$)', 'categoria': 'Category'}
        )

    st.plotly_chart(fig)


def spending_by_category_bar_chart(df):
    """Spending by Category with Time Filter"""
    st.subheader("Spending by Category")

    # Ensure 'lancamento' is in datetime format
    df['lancamento'] = pd.to_datetime(df['lancamento'], errors='coerce')

    last_7_days = st.checkbox("Show Last 7 Days Only")
    if last_7_days:
        # Filter data for the last 7 days
        df = df[df['lancamento'] >= (pd.Timestamp.now() - pd.Timedelta(days=7))]

    # Create the bar chart
    fig = px.bar(
        df[df['tipo'] == SAIDA],
        x='categoria',
        y='valor',
        title='Spending by Category',
        labels={'categoria': 'Category', 'valor': 'Amount (R$)'},
        color='categoria'
    )
    st.plotly_chart(fig)



def recurring_transactions_dashboard(df):
    """Highlight Recurring Transactions"""
    recurring = df.groupby(['descricao']).filter(lambda x: len(x) > 1)
    
    with st.container():
        st.subheader("Recurring Transactions")
        st.dataframe(recurring)


def budget_vs_actual_dashboard(df, budget):
    """Budget vs Actual"""
    # Group by 'tipo' and sum only the 'valor' column
    df_grouped = df.groupby('tipo')['valor'].sum().reset_index()

    # Get actual spending
    actual = df_grouped.loc[df_grouped['tipo'] == SAIDA, 'valor'].values[0] if SAIDA in df_grouped['tipo'].values else 0

    # Create a bar chart for Budget vs Actual
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=['Budget', 'Actual'],
        y=[budget, actual],
        name='Spending',
        marker_color=['green', 'blue']
    ))

    fig.update_layout(
        title='Budget vs Actual',
        yaxis_title='Amount (R$)',
        barmode='group'
    )

    st.plotly_chart(fig)


def transaction_table_with_filters(df):
    """Transaction Table with Filters"""
    with st.container():
        st.subheader("Transaction Details")
        category = st.selectbox("Filter by Category", options=["All"] + df['categoria'].unique().tolist())
        account = st.selectbox("Filter by Account", options=["All"] + df['conta'].unique().tolist())
        
        filtered_df = df
        if category != "All":
            filtered_df = filtered_df[filtered_df['categoria'] == category]
        if account != "All":
            filtered_df = filtered_df[filtered_df['conta'] == account]
        
        st.dataframe(filtered_df)




