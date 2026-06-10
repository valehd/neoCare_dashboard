# ==========================
# IMPORTS
# ==========================
import streamlit as st
import plotly.express as px
import pandas as pd
from components.theme import neocare_colors
from components.footer import show_footer
from components.sidebar import show_sidebar
from components.header import show_header
from database.queries.deliveries import get_deliveries


# ==========================
# SIDEBAR-HEADER
# ==========================
show_sidebar()
show_header()


# ==========================
# PAGE TITLE
# ==========================
st.title("Labor and Delivery Analysis")


# ==========================
# DATA
# ==========================
df = get_deliveries()


# ==========================
# FILTERS
# ==========================
st.subheader("Filters")

col1, col2 = st.columns(2)

with col1:

    selected_delivery = st.selectbox(
        "Delivery Type",
        ["All"] + sorted(
            df["delivery_type"]
            .dropna()
            .unique()
        )
    )

with col2:

    selected_outcome = st.selectbox(
        "Birth Outcome",
        ["All"] + sorted(
            df["birth_outcome"]
            .dropna()
            .unique()
        )
    )


# ==========================
# APPLY FILTERS
# ==========================
df_filtered = df.copy()

if selected_delivery != "All":

    df_filtered = df_filtered[
        df_filtered["delivery_type"]
        == selected_delivery
    ]

if selected_outcome != "All":

    df_filtered = df_filtered[
        df_filtered["birth_outcome"]
        == selected_outcome
    ]


# ==========================
# KPIs
# ==========================
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Deliveries",
    len(df_filtered)
)

col2.metric(
    "Avg Vaginal Exams",
    round(
        df_filtered["vaginal_examinations"].mean(),
        1
    )
)

col3.metric(
    "Antibiotic Use (%)",
    round(
        df_filtered["antibiotics"].mean() * 100,
        1
    )
)

col4.metric(
    "Oxytocin Use (%)",
    round(
        df_filtered["oxytocin"].mean() * 100,
        1
    )
)

st.divider()


# ==========================
# DELIVERY TYPE DATA
# ==========================
delivery_type_df = (
    df_filtered["delivery_type"]
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
    title="Delivery Type Distribution",
    color_discrete_sequence=neocare_colors
)


# ==========================
# BIRTH OUTCOMES DATA
# ==========================
outcome_df = (
    df_filtered["birth_outcome"]
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
    title="Birth Outcomes",
    color_discrete_sequence=neocare_colors
)


# ==========================
# FIRST ROW OF CHARTS
# ==========================
col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(
        fig_delivery,
        use_container_width=True
    )

with col2:

    st.plotly_chart(
        fig_outcome,
        use_container_width=True
    )


# ==========================
# ROM DURATION
# ==========================
fig_rom = px.histogram(
    df_filtered,
    x="rupture_membranes_hours",
    nbins=10,
    title="Rupture of Membranes Duration",
    color_discrete_sequence=neocare_colors
)


# ==========================
# INTERVENTIONS DATA
# ==========================
interventions = {
    "Antibiotics":
        df_filtered["antibiotics"].mean() * 100,

    "Oxytocin":
        df_filtered["oxytocin"].mean() * 100,

    "Companion":
        df_filtered["significant_companion"].mean() * 100,

    "Monitoring":
        df_filtered["intrapartum_monitoring"].mean() * 100
}

interventions_df = pd.DataFrame(
    interventions.items(),
    columns=[
        "Intervention",
        "Percentage"
    ]
)

fig_interventions = px.bar(
    interventions_df,
    x="Intervention",
    y="Percentage",
    title="Clinical Interventions During Labor",
    color_discrete_sequence=neocare_colors
)


# ==========================
# SECOND ROW OF CHARTS
# ==========================
col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(
        fig_rom,
        use_container_width=True
    )

with col2:

    st.plotly_chart(
        fig_interventions,
        use_container_width=True
    )


# ==========================
# TABLE
# ==========================
st.subheader("Delivery Records")

display_df = df_filtered.drop(
    columns=["id_delivery"],
    errors="ignore"
)

with st.expander("View Records"):

    st.dataframe(
        display_df,
        use_container_width=True
    )


# ==========================
# FOOTER
# ==========================
show_footer()