import streamlit as st

def dashboard_metric(df, monthly_budget, savings_goal):
    """Metrics for Dashboard"""
    # Calculate metrics
    entradas = df[df['tipo'] == "Entrada"]['valor'].sum()
    saidas = df[df['tipo'] == "Saida"]['valor'].sum()
    savings = entradas - saidas
    remaining_budget = max(monthly_budget - saidas, 0)
    over_budget = saidas > monthly_budget

    # Calculate savings progress
    savings_progress = min((savings / savings_goal) * 100, 100) if savings_goal > 0 else 0
    savings_status = "Achieved" if savings >= savings_goal else "In Progress"

    # Display metrics
    st.markdown("### 📊 Financial Overview")
    col_entradas, col_saidas, col_savings, col_budget_status = st.columns(4)

    with col_entradas:
        st.metric(label="💰 Entradas", value=f"R$ {entradas:,.2f}")

    with col_saidas:
        st.metric(label="📉 Saídas", value=f"R$ {saidas:,.2f}")

    with col_savings:
        st.metric(
            label="💾 Savings So Far",
            value=f"R$ {savings:,.2f}",
            delta=f"{savings_progress:.2f}% of Goal",
            delta_color="normal" if savings < savings_goal else "off"
        )

    with col_budget_status:
        if over_budget:
            st.metric(
                label="⚠️ Budget Status",
                value="Over Budget",
                delta=f"-R$ {saidas - monthly_budget:,.2f}",
                delta_color="inverse"
            )
        else:
            st.metric(
                label="✔️ Budget Status",
                value="Under Budget",
                delta=f"+R$ {remaining_budget:,.2f}",
                delta_color="normal"
            )

    # Additional savings goal section
    st.markdown("### 🏦 Savings Goal Progress")
    st.progress(savings_progress / 100)
    st.write(f"**Savings Goal:** R$ {savings_goal:,.2f} ({savings_status})")
