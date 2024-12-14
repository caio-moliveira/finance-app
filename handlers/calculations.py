import locale
from controller.config import ENTRADA, SAIDA

locale.setlocale(locale.LC_ALL, "")

def dashboard_metrics(df):
    """
    Retorna: saldo, entradas e despesas calculadas com base no df recebido
    """
    entradas = df.loc[df["tipo"]==ENTRADA, "valor"].sum()
    despesas = df.loc[df["tipo"]==SAIDA, "valor"].sum()
    saldo = entradas - despesas

    class BRL:
        def __init__(self, valor: float) -> None:
            self.valor = valor
            
        def converter_pontuacao(self, valor: float) -> str:
            valor_str = f'{valor:,.2f}'
            valor_str = valor_str.replace('.', '_')
            valor_str = valor_str.replace(',', '.')
            valor_str = valor_str.replace('_', ',')
            return valor_str
        
        def adicionar_rs_sifrao(self, valor: str) -> str:
            valor_brl = f'R$ {valor}'
            return valor_brl
        
        def __repr__(self) -> str:
            valor_brl = self.converter_pontuacao(self.valor)
            valor_brl = self.adicionar_rs_sifrao(valor_brl)
            return valor_brl


    entradas = BRL(entradas)
    despesas = BRL(despesas)
    saldo = BRL(saldo)

    return entradas, despesas, saldo
