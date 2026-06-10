
import pandas as pd
from database.connection import get_connection



# Newborn
def get_newborns():
    conn = get_connection()

    query = """
    SELECT *
    FROM newborn
    """

    return pd.read_sql(query, conn)

def get_average_birth_weight():
    conn = get_connection()

    query = """
    SELECT AVG(weight_gr) as avg_weight
    FROM newborn
    """

    return pd.read_sql(query, conn)


def get_average_apgar():
    conn = get_connection()

    query = """
    SELECT
        AVG(apgar_1) as avg_apgar_1,
        AVG(apgar_5) as avg_apgar_5
    FROM newborn
    """

    return pd.read_sql(query, conn)


