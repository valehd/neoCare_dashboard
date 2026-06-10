# ==========================
# IMPORTS
# ==========================
import pandas as pd
from database.connection import get_connection


def get_mothers():
    conn = get_connection()

    query = """
    SELECT *
    FROM mother
    """

    return pd.read_sql(query, conn)

def get_maternal_conditions_distribution():
    conn = get_connection()

    query = """
    SELECT
        maternal_conditions,
        COUNT(*) as total
    FROM mother
    WHERE maternal_conditions IS NOT NULL
    GROUP BY maternal_conditions
    ORDER BY total DESC
    """

    return pd.read_sql(query, conn)