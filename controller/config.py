from pathlib import Path

# Database path (ensure it's relative to the current directory)
DATABASE = "database/database.db"

# Constants for transaction types
ENTRADA = "Entrada"
SAIDA = "Saida"

TIPOS = (ENTRADA, SAIDA)

# Table names
TRANSACTIONS = "transactions"
ACCOUNTS = "accounts"
CATEGORIES = "categories"
USERS = "users"
