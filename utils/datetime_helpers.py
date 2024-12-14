from datetime import datetime, timedelta
import locale

locale.setlocale(locale.LC_ALL, "portuguese_brazil")

def format_data_br(data):
    if isinstance(data, str):
        formato = "%Y-%m-%d"
        formato_br = "%d/%m/%Y"
        data_datetime = datetime.datetime.strptime(data, formato)
        data_str = data_datetime.strftime(formato_br)
        return data_str
    

def create_period(days: int):
    inicio, fim = datetime.now() - timedelta(days=days), datetime.now()
    return inicio, fim