# ==========================
# IMPORTS
# ==========================
import streamlit as st
import plotly.express as px
from components.footer import show_footer
from components.sidebar import show_sidebar
from database.queries.neonatal_monitoring import get_neonatal_controls

# ==========================
# PAGE TITLE
# ==========================
st.title("🩺 Neonatal Monitoring")

# ==========================
# DATA
# ==========================
df = get_neonatal_controls()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Avg Heart Rate",
    round(df["heart_rate"].mean(), 0)
)

col2.metric(
    "Avg Respiratory Rate",
    round(df["respiratory_rate"].mean(), 0)
)

col3.metric(
    "Avg Temperature",
    round(df["temperature"].mean(), 1)
)

col4.metric(
    "Avg Oxygen Saturation",
    round(df["oxygen_saturation"].mean(), 1)
)
urination_rate = (
    df["urination"].mean() * 100
)
stool_rate = (
    df["stool"].mean() * 100
)
st.divider()

col1, col2 = st.columns(2)

col1.metric(
    "Urination Rate (%)",
    round(urination_rate, 1)
)

col2.metric(
    "Stool Elimination Rate (%)",
    round(stool_rate, 1)
)

show_footer()
show_sidebar()