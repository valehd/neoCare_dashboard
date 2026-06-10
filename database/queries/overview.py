
import pandas as pd
from database.connection import get_connection


# Overview Queries

def get_total_mothers():
    conn = get_connection()
    return pd.read_sql(
        "SELECT COUNT(*) as total FROM mother",
        conn
    )


def get_total_pregnancies():
    conn = get_connection()
    return pd.read_sql(
        "SELECT COUNT(*) as total FROM pregnancy",
        conn
    )


def get_total_deliveries():
    conn = get_connection()
    return pd.read_sql(
        "SELECT COUNT(*) as total FROM delivery",
        conn
    )


def get_total_newborns():
    conn = get_connection()
    return pd.read_sql(
        "SELECT COUNT(*) as total FROM newborn",
        conn
    )