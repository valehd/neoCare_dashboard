# ==========================
# IMPORTS
# ==========================
import streamlit as st
import plotly.express as px
import pandas as pd
from components.theme import neocare_colors
from components.footer import show_footer
from components.styles import neocare_css
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



neocare_css()
show_sidebar()

# ==========================    
# DASHBOARD TITLE   
# ==========================

st.title("NeoCare Dashboard")
st.caption(
    "Maternal and Neonatal Healthcare Analytics"
)

st.info(
    """
    NeoCare Dashboard provides analytics and visualization
    of maternal, pregnancy, delivery, newborn and neonatal
    monitoring data.
    """
)

# ==========================
# OVERVIEW KPIs
# ==========================

st.subheader("Key Performance Indicators")

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
    hole=0.4,
    color_discrete_sequence=neocare_colors

)


apgar_chart = pd.DataFrame(
    {
        "Minute": ["1 min", "5 min"],
        "Score": [
            avg_apgar_1,
            avg_apgar_5
        ]
    }
)

fig_apgar = px.bar(
    apgar_chart,
    x="Minute",
    y="Score",
    title="Average APGAR Scores",
    color_discrete_sequence=neocare_colors
)

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    st.plotly_chart(
        fig_apgar,
        use_container_width=True
    )

show_footer()
