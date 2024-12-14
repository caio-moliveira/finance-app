from templates import sidebar
import streamlit as st
import locale

locale.setlocale(locale.LC_ALL, "")

def main():

    st.toast("Em desenvolvimento...", icon="⚙️")

if __name__ == "__main__":
    # Configurações da página
    st.set_page_config("Configurações", "⚙️", "wide")
    sidebar.menu()
    main()
        