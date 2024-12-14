import streamlit as st
from pathlib import Path
from controller.creator import create_users_table
from controller.loader import load_users_credentials
PAGES_DIR = Path(__file__).parent

def main():
    create_users_table()
    
    cols = st.columns([1, 3, 1])

    with cols[1].form('form-login-travelmetry', border=True):
        st.header('🔐 Login', anchor=False)
        username = st.text_input(
            'Nome de usuário', placeholder="Nome de Usuário", max_chars=30
        )
        password = st.text_input(
            'Senha', type='password', placeholder="Senha", max_chars=30
        )

        col_entrar, col_cadastrar = st.columns(2)

        if col_entrar.form_submit_button('Entrar', type="primary"):

            if username and password:
                df_user = load_users_credentials(username, password)
                if not df_user.empty:
                    st.cache_data.clear()
                    st.cache_resource.clear()
                    st.session_state['username'] = username
                    st.session_state['password'] = password
                    st.session_state['user_id'] = str(df_user['id'].values[0])
                    st.switch_page('pages/2_dashboard.py')
                else:
                    st.toast("Credênciais inválidas", icon='❌')
            
            elif not username and password:
                st.toast("Preencha o Nome de usuário", icon="⚠️")
            
            elif not password and username:
                st.toast("Preencha a Senha", icon="⚠️")
            
            else:
                st.toast("Preencha os campos", icon="⚠️")
        
        if col_cadastrar.form_submit_button("Cadastro"):
            st.switch_page('pages/1_register.py')
        
        st.divider()
        st.write("Copyright © 2024 Mateus Alves")
        st.write("")

if __name__ == "__main__":
    st.set_page_config(
        page_title="Login",
        page_icon="🔐",
        layout="centered",
    )
    main()
    