# ==========================
# IMPORTS
# ==========================
import streamlit as st
import plotly.express as px
import pandas as pd
from components.footer import show_footer
from database.queries.deliveries import get_deliveries

# ==========================
# PAGE TITLE
# ==========================
st.title("🚑 Labor and Delivery Analysis")


# ==========================
# DATA
# ==========================
df = get_deliveries()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Deliveries",
    len(df)
)

col2.metric(
    "Avg Vaginal Exams",
    round(df["vaginal_examinations"].mean(), 1)
)

col3.metric(
    "Antibiotic Use (%)",
    round(df["antibiotics"].mean() * 100, 1)
)

col4.metric(
    "Oxytocin Use (%)",
    round(df["oxytocin"].mean() * 100, 1)
)

delivery_type_df = (
    df["delivery_type"]
    .value_counts()
    .reset_index()
)

delivery_type_df.columns = [
    "delivery_type",
    "total"
]

fig_delivery = px.pie(
    delivery_type_df,
    values="total",
    names="delivery_type",
    hole=0.4,
    title="Delivery Type Distribution"
)

st.plotly_chart(
    fig_delivery,
    use_container_width=True
)


fig_rom = px.histogram(
    df,
    x="rupture_membranes_hours",
    nbins=10,
    title="Rupture of Membranes Duration"
)

st.plotly_chart(
    fig_rom,
    use_container_width=True
)


interventions = {
    "Antibiotics": df["antibiotics"].mean() * 100,
    "Oxytocin": df["oxytocin"].mean() * 100,
    "Companion": df["significant_companion"].mean() * 100,
    "Monitoring": df["intrapartum_monitoring"].mean() * 100
}



interventions_df = pd.DataFrame(
    interventions.items(),
    columns=["Intervention", "Percentage"]
)

fig_interventions = px.bar(
    interventions_df,
    x="Intervention",
    y="Percentage",
    title="Clinical Interventions During Labor"
)

st.plotly_chart(
    fig_interventions,
    use_container_width=True
)

outcome_df = (
    df["birth_outcome"]
    .value_counts()
    .reset_index()
)

outcome_df.columns = [
    "birth_outcome",
    "total"
]

fig_outcome = px.bar(
    outcome_df,
    x="birth_outcome",
    y="total",
    title="Birth Outcomes"
)

st.plotly_chart(
    fig_outcome,
    use_container_width=True
)

show_footer()