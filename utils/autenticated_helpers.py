import streamlit as st


def autenticated() -> bool:
    """Travelmend.
        Verifica se está autenticado
    Returns:
        bool: True se autenticado, False se não.
    """
    if "username" in st.session_state and "password" in st.session_state:
        return True
    return False


