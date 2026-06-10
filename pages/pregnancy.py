# ==========================
# IMPORTS
# ==========================
import streamlit as st
import plotly.express as px
from components.theme import neocare_colors
from components.header import show_header
from components.footer import show_footer
from components.sidebar import show_sidebar

from database.queries.pregnancies import (
    get_pregnancies
)

# ==========================
# SIDEBAR
# ==========================
show_sidebar()
show_header()
# ==========================
# PAGE TITLE
# ==========================
st.title("Pregnancy Management")

# ==========================
# DATA
# ==========================
df = get_pregnancies()

# ==========================
# FILTERS
# ==========================
st.subheader("Filters")

col1, col2, col3 = st.columns(3)

with col1:

    min_ga = int(df["gestational_age_prenatal"].min())
    max_ga = int(df["gestational_age_prenatal"].max())

    ga_range = st.slider(
        "Gestational Age",
        min_ga,
        max_ga,
        (min_ga, max_ga)
    )

with col2:

    pregnancy_type = st.selectbox(
        "Pregnancy Type",
        ["All", "Single", "Multiple"]
    )

with col3:

    condition_filter = st.selectbox(
        "Pregnancy Condition",
        ["All"] + sorted(
            df["pregnancy_conditions"]
            .dropna()
            .unique()
        )
    )

# ==========================
# APPLY FILTERS
# ==========================
df_filtered = df.copy()

df_filtered = df_filtered[
    (df_filtered["gestational_age_prenatal"] >= ga_range[0]) &
    (df_filtered["gestational_age_prenatal"] <= ga_range[1])
]

if pregnancy_type == "Single":

    df_filtered = df_filtered[
        df_filtered["multiple_pregnancy"] == False
    ]

elif pregnancy_type == "Multiple":

    df_filtered = df_filtered[
        df_filtered["multiple_pregnancy"] == True
    ]

if condition_filter != "All":

    df_filtered = df_filtered[
        df_filtered["pregnancy_conditions"]
        == condition_filter
    ]

# ==========================
# KPIs
# ==========================
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Pregnancies",
    len(df_filtered)
)

col2.metric(
    "Average Gestational Age",
    round(
        df_filtered["gestational_age_prenatal"].mean(),
        1
    )
)

col3.metric(
    "Average Prenatal Controls",
    round(
        df_filtered["prenatal_control_count"].mean(),
        1
    )
)

col4.metric(
    "Multiple Pregnancy (%)",
    round(
        df_filtered["multiple_pregnancy"].mean() * 100,
        1
    )
)

# ==========================
# GESTATIONAL AGE
# ==========================
fig_ga = px.histogram(
    df_filtered,
    x="gestational_age_prenatal",
    nbins=10,
    title="Prenatal Gestational Age Distribution",
    color_discrete_sequence=neocare_colors
)

# ==========================
# PRENATAL CONTROLS
# ==========================
fig_controls = px.histogram(
    df_filtered,
    x="prenatal_control_count",
    nbins=10,
    title="Prenatal Control Visits",
    color_discrete_sequence=neocare_colors  
)

# ==========================
# FIRST ROW OF CHARTS
# ==========================
st.divider()

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(
        fig_ga,
        use_container_width=True
    )

with col2:

    st.plotly_chart(
        fig_controls,
        use_container_width=True
    )

# ==========================
# PREGNANCY TYPE
# ==========================
multiple_df = (
    df_filtered["multiple_pregnancy"]
    .value_counts()
    .reset_index()
)

multiple_df.columns = [
    "multiple_pregnancy",
    "total"
]

multiple_df["multiple_pregnancy"] = (
    multiple_df["multiple_pregnancy"]
    .replace({
        True: "Multiple",
        False: "Single"
    })
)

fig_multiple = px.pie(
    multiple_df,
    values="total",
    names="multiple_pregnancy",
    hole=0.4,
    title="Pregnancy Type",
    color_discrete_sequence=neocare_colors
)

# ==========================
# CONDITIONS
# ==========================
conditions_df = (
    df_filtered["pregnancy_conditions"]
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
    title="Pregnancy Conditions",
    color_discrete_sequence=neocare_colors
)

# ==========================
# SECOND ROW OF CHARTS
# ==========================
col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(
        fig_multiple,
        use_container_width=True
    )

with col2:

    st.plotly_chart(
        fig_conditions,
        use_container_width=True
    )

# ==========================
# TABLE
# ==========================
st.subheader("Pregnancy Records")

display_df = df_filtered.drop(
    columns=[
        "id_pregnancy",
        "id_mother"
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