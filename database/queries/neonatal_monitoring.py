
import pandas as pd
from database.connection import get_connection



def get_neonatal_controls():
    conn = get_connection()

    query = """
    SELECT *
    FROM neonatal_control
    """

    return pd.read_sql(query, conn)