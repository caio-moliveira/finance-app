
def check_empty_df(*args) -> bool:
    """Retorna VERDADEIRO se algum df estiver vazio"""
    df_empty = False

    # Loop
    for df in args:
        if df is None or df.empty:
            df_empty = True

    return df_empty