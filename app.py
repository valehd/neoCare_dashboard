# ==========================
# IMPORTS
# ==========================
import streamlit as st
import plotly.express as px
from components.footer import show_footer
from components.sidebar import show_sidebar
from database.queries.overview import (
    get_total_mothers,
    get_total_pregnancies,
    get_total_deliveries,
    get_total_newborns,
)
from database.queries.deliveries import get_delivery_distribution
from database.queries.newborn import get_average_birth_weight, get_average_apgar 


# Set page config

st.set_page_config(
    page_title="NeoCare Dashboard",
    layout="wide"
)

# ==========================    
# DASHBOARD TITLE   
# ==========================

st.title("🤰 NeoCare Dashboard")

# ==========================
# OVERVIEW KPIs
# ==========================


col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Mothers",
    get_total_mothers().iloc[0]["total"]
)

col2.metric(
    "Pregnancies",
    get_total_pregnancies().iloc[0]["total"]
)

col3.metric(
    "Deliveries",
    get_total_deliveries().iloc[0]["total"]
)

col4.metric(
    "Newborns",
    get_total_newborns().iloc[0]["total"]
)


# ==========================
# DELIVERY ANALYTICS
# ==========================

st.divider()

st.subheader("Delivery Type Distribution")

df_delivery = get_delivery_distribution()

fig = px.pie(
    df_delivery,
    values="total",
    names="delivery_type",
    hole=0.4
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# ==========================
# NEWBORN ANALYTICS
# ==========================

avg_weight = get_average_birth_weight().iloc[0]["avg_weight"]

apgar_data = get_average_apgar()

avg_apgar_1 = apgar_data.iloc[0]["avg_apgar_1"]
avg_apgar_5 = apgar_data.iloc[0]["avg_apgar_5"]

st.divider()

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Birth Weight (g)",
    round(avg_weight, 0)
)

col2.metric(
    "Avg APGAR 1 min",
    round(avg_apgar_1, 1)
)

col3.metric(
    "Avg APGAR 5 min",
    round(avg_apgar_5, 1)
)

show_footer()
show_sidebar()