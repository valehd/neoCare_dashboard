# ==========================
# IMPORTS
# ==========================
import streamlit as st
import plotly.express as px
from components.theme import neocare_colors
from components.footer import show_footer
from components.sidebar import show_sidebar
from components.header import show_header
from database.queries.neonatal_outcomes import (
    get_neonatal_outcomes
)

# ==========================
# SIDEBAR - HEADER
# ==========================
show_sidebar()
show_header()
# ==========================
# PAGE TITLE
# ==========================
st.title("Neonatal Outcomes")

# ==========================
# DATA
# ==========================
df = get_neonatal_outcomes()

# ==========================
# FILTERS
# ==========================
st.subheader("Filters")

selected_destination = st.selectbox(
    "Destination",
    ["All"] + sorted(
        df["destination"]
        .dropna()
        .unique()
    )
)

# ==========================
# APPLY FILTERS
# ==========================
df_filtered = df.copy()

if selected_destination != "All":

    df_filtered = df_filtered[
        df_filtered["destination"]
        == selected_destination
    ]

# ==========================
# KPIs
# ==========================
hospitalized = len(
    df_filtered[
        df_filtered["admission_reason"].notna()
    ]
)

hospitalization_rate = (
    hospitalized / len(df_filtered) * 100
    if len(df_filtered) > 0
    else 0
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Outcomes",
    len(df_filtered)
)

col2.metric(
    "Hospitalized",
    hospitalized
)

col3.metric(
    "Hospitalization Rate (%)",
    round(hospitalization_rate, 1)
)

# ==========================
# DESTINATION DISTRIBUTION
# ==========================
destination_df = (
    df_filtered["destination"]
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
    title="Neonatal Destination Distribution",
    color_discrete_sequence=neocare_colors
)

# ==========================
# ADMISSION REASONS
# ==========================
admission_df = (
    df_filtered["admission_reason"]
    .fillna("No Admission")
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
    title="Admission Reasons",
    color_discrete_sequence=neocare_colors
)

# ==========================
# CHARTS
# ==========================
st.divider()

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(
        fig_destination,
        use_container_width=True
    )

with col2:

    st.plotly_chart(
        fig_admission,
        use_container_width=True
    )

# ==========================
# TABLE
# ==========================
st.subheader("Outcome Records")

display_df = df_filtered.drop(
    columns=[
        "id_outcome",
        "id_newborn"
    ],
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