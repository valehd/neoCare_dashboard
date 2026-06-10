# ==========================
# IMPORTS
# ==========================
import pandas as pd
from database.connection import get_connection



def get_neonatal_outcomes():
    conn = get_connection()

    query = """
    SELECT *
    FROM neonatal_outcome
    """

    return pd.read_sql(query, conn)