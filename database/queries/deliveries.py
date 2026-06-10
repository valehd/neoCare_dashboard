# ==========================
# IMPORTS
# ==========================
import pandas as pd
from database.connection import get_connection


def get_delivery_distribution():
    conn = get_connection()

    query = """
    SELECT
        delivery_type,
        COUNT(*) as total
    FROM delivery
    GROUP BY delivery_type
    """

    return pd.read_sql(query, conn)


def get_deliveries():
    conn = get_connection()

    query = """
    SELECT *
    FROM delivery
    """

    return pd.read_sql(query, conn)