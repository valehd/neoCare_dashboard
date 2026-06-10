# ==========================
# IMPORTS
# ==========================
import streamlit as st
import plotly.express as px
from components.footer import show_footer
from database.queries.neonatal_outcomes import get_neonatal_outcomes

# ==========================
# PAGE TITLE
# ==========================
st.title("🏥 Neonatal Outcomes")

# ==========================
# DATA
# ==========================
df = get_neonatal_outcomes()

destination_df = (
    df["destination"]
    .value_counts()
    .reset_index()
)

destination_df.columns = [
    "destination",
    "total"
]

fig_destination = px.pie(
    destination_df,
    values="total",
    names="destination",
    hole=0.4,
    title="Neonatal Destination Distribution"
)

st.plotly_chart(
    fig_destination,
    use_container_width=True
)


admission_df = (
    df["admission_reason"]
    .value_counts()
    .reset_index()
)

admission_df.columns = [
    "admission_reason",
    "total"
]

fig_admission = px.bar(
    admission_df,
    x="admission_reason",
    y="total",
    title="Admission Reasons"
)

st.plotly_chart(
    fig_admission,
    use_container_width=True
)

st.metric(
    "Total Outcomes Registered",
    len(df)
)

show_footer()