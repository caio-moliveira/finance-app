import sqlite3
from pathlib import Path
from .config import DATABASE, TRANSACTIONS, CATEGORIES, ACCOUNTS, USERS


def ensure_database_directory():
    """Ensure the database directory exists before connecting to the database."""
    db_path = Path(DATABASE)
    db_path.parent.mkdir(parents=True, exist_ok=True)


def create_table(query: str):
    """
    Create a table in the SQLite database.

    Args:
        query (str): The SQL query to create the table.
    """
    # Ensure the database directory exists
    ensure_database_directory()

    try:
        # Connect to the database (or create it if it doesn't exist)
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Execute the table creation query
        cursor.execute(query)

        # Commit changes to the database
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")
    finally:
        # Ensure resources are properly closed
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()


def create_transactions_table():
    query = f"""
    CREATE TABLE IF NOT EXISTS {TRANSACTIONS} (
        id INTEGER PRIMARY KEY, 
        user_id INT, 
        tipo TEXT, 
        descricao TEXT, 
        valor FLOAT, 
        lancamento DATETIME,
        vencimento DATETIME,
        efetivacao DATETIME, 
        categoria TEXT, 
        subcategoria TEXT, 
        cartao TEXT, 
        conta TEXT 
    )
    """
    create_table(query)


def create_categories_table():
    query = f"""
    CREATE TABLE IF NOT EXISTS {CATEGORIES} (
        id INTEGER PRIMARY KEY, 
        user_id INT, 
        lancamento DATETIME, 
        nome TEXT, 
        tipo TEXT
    )
    """
    create_table(query)


def create_accounts_table():
    query = f"""
    CREATE TABLE IF NOT EXISTS {ACCOUNTS} (
        id INTEGER PRIMARY KEY, 
        user_id INT, 
        lancamento DATETIME, 
        nome TEXT
    )
    """
    create_table(query)


def create_users_table():
    query = f"""
    CREATE TABLE IF NOT EXISTS {USERS} (
        id INTEGER PRIMARY KEY, 
        username TEXT, 
        password TEXT, 
        email TEXT, 
        lancamento DATETIME 
    )
    """
    create_table(query)
