import streamlit as st
from utils.instalador import install_requirements
import locale

locale.setlocale(locale.LC_ALL, "")


# Chamar a função para instalar os pacotes
def main():
    install_requirements()
    st.switch_page("pages/0_login.py")


if __name__ == "__main__":
    main()