from mysql.connector import pooling
import os

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_HOST", "admin"),
    "password": os.getenv("DB_HOST", "admin"),
    "database": os.getenv("DB_HOST", "cscan"),
    "autocommit": False
}

# Connection pool (important for large seeding)
connection_pool = pooling.MySQLConnectionPool(
    pool_name="seed_pool",
    pool_size=10,
    **DB_CONFIG
)

def get_connection():
    return connection_pool.get_connection()

# def get_connection():
#     """
#     Returns a MySQL connection
#     """
#     return mysql.connector.connect(**DB_CONFIG)

# def get_cursor(conn):
#     """
#     Returns a buffered cursor
#     """
#     return conn.cursor(buffered=True)
