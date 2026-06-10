# ==========================
# IMPORTS
# ==========================

import streamlit as st
import plotly.express as px
import pandas as pd
from components.footer import show_footer
from database.queries.pregnancies import get_pregnancies
from components.sidebar import show_sidebar

# ==========================
# PAGE TITLE
# ==========================
st.title("🤰 Pregnancy Management")


# ==========================
# DATA
# ==========================
df = get_pregnancies()


col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Pregnancies",
    len(df)
)

col2.metric(
    "Average Gestational Age",
    round(df["gestational_age_prenatal"].mean(), 1)
)

col3.metric(
    "Average Prenatal Controls",
    round(df["prenatal_control_count"].mean(), 1)
)

col4.metric(
    "Multiple Pregnancy (%)",
    round(df["multiple_pregnancy"].mean() * 100, 1)
)

fig_ga = px.histogram(
    df,
    x="gestational_age_prenatal",
    nbins=10,
    title="Prenatal Gestational Age Distribution"
)

st.plotly_chart(
    fig_ga,
    use_container_width=True
)

fig_controls = px.histogram(
    df,
    x="prenatal_control_count",
    nbins=10,
    title="Prenatal Control Visits"
)

st.plotly_chart(
    fig_controls,
    use_container_width=True
)

multiple_df = (
    df["multiple_pregnancy"]
    .value_counts()
    .reset_index()
)

multiple_df.columns = [
    "multiple_pregnancy",
    "total"
]

multiple_df["multiple_pregnancy"] = multiple_df[
    "multiple_pregnancy"
].replace({
    True: "Multiple",
    False: "Singleton"
})

fig_multiple = px.pie(
    multiple_df,
    values="total",
    names="multiple_pregnancy",
    hole=0.4,
    title="Pregnancy Type"
)

st.plotly_chart(
    fig_multiple,
    use_container_width=True
)


conditions_df = (
    df["pregnancy_conditions"]
    .value_counts()
    .reset_index()
)

conditions_df.columns = [
    "pregnancy_conditions",
    "total"
]


fig_conditions = px.bar(
    conditions_df,
    x="pregnancy_conditions",
    y="total",
    title="Pregnancy Conditions"
)

st.plotly_chart(
    fig_conditions,
    use_container_width=True
)


st.subheader("Pregnancy Records")

display_df = df.drop(
    columns=["id_pregnancy", "id_mother"],
    errors="ignore"
)

st.dataframe(
    display_df,
    use_container_width=True
)

show_footer()
show_sidebar()