
# ==========================
# IMPORTS
# ==========================
import streamlit as st
import mysql.connector

@st.cache_resource
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root1717",
        database="maternal_database"
    )