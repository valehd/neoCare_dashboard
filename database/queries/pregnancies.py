
import pandas as pd
from database.connection import get_connection

def get_pregnancies():
    conn = get_connection()

    query = """
    SELECT *
    FROM pregnancy
    """

    return pd.read_sql(query, conn)