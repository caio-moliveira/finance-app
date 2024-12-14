from controller.creator import create_users_table
from controller.insert import insert_user_registration
import streamlit as st
import time
import pandas as pd
import datetime

# Função para exibir o formulário de cadastro
def show_registration_form():
    create_users_table()

    cols = st.columns([1, 3, 1])

    # Formulário de cadastro
    with cols[1].form("registration_form"):
        st.header("🔐 Cadastro")
        username = st.text_input(
            "Nome de usuário", placeholder="Nome de Usuário", max_chars=30
        )
        email = st.text_input(
            "Email", placeholder="Ex.: exemple@exemple.com", max_chars=30
        )
        password = st.text_input(
            "Senha", type="password", placeholder="Senha", max_chars=30
        )
        confirm_password = st.text_input(
            "Confirme sua senha", type="password", placeholder="Confirmação de senha", max_chars=30
        )
        
        col_cadastrar, col_login = st.columns(2)
        
        # Lógica de validação e feedback
        if col_cadastrar.form_submit_button("Cadastrar", type="primary"):
            if not username or not email or not password or not confirm_password:
                st.toast("Por favor, preencha todos os campos.", icon="⚠️")
            elif password != confirm_password:
                st.toast("As senhas não coincidem.", icon="❌")
            else:
                st.toast("Cadastro realizado com sucesso!", icon="✅")
                
                # Aqui você pode adicionar a lógica para salvar os dados do usuário
                data = {
                    "username": [username],
                    "password": [password],
                    "email": [email],
                    "lancamento": [datetime.date.today()]
                }
                df = pd.DataFrame(data)
                insert_user_registration(df)
                
                time.sleep(1)
                st.switch_page("pages/0_login.py")


        if col_login.form_submit_button("Login"):
            st.switch_page("pages/0_login.py")
        
if __name__ == "__main__":
    st.set_page_config(
        page_title="Cadastro",
        page_icon="🔐",
        layout="centered",
    )
    # Exibir o formulário de cadastro
    show_registration_form()
