# ==========================
# IMPORTS
# ==========================
import streamlit as st
import plotly.express as px
from components.theme import neocare_colors
from components.styles import neocare_css
from components.footer import show_footer
from components.sidebar import show_sidebar
from database.queries.mothers import (
    get_mothers
)

# ==========================
# SIDEBAR
# ==========================
show_sidebar()
neocare_css()
# ==========================
# PAGE TITLE
# ==========================
st.title("👩 Maternal Analysis")

# ==========================
# DATA
# ==========================
df = get_mothers()

# ==========================
# FILTERS
# ==========================
st.subheader("Filters")

col1, col2, col3 = st.columns(3)

# Age Range
with col1:

    min_age = int(df["age"].min())
    max_age = int(df["age"].max())

    age_range = st.slider(
        "Age Range",
        min_age,
        max_age,
        (min_age, max_age)
    )

# Maternal Condition
with col2:

    selected_condition = st.selectbox(
        "Maternal Condition",
        ["All"] + sorted(
            df["maternal_conditions"]
            .dropna()
            .unique()
        )
    )

# Blood Type
with col3:

    selected_blood = st.selectbox(
        "Blood Type",
        ["All"] + sorted(
            df["blood_type"]
            .dropna()
            .unique()
        )
    )

# ==========================
# APPLY FILTERS
# ==========================
df_filtered = df.copy()

# Age filter
df_filtered = df_filtered[
    (df_filtered["age"] >= age_range[0]) &
    (df_filtered["age"] <= age_range[1])
]

# Condition filter
if selected_condition != "All":

    df_filtered = df_filtered[
        df_filtered["maternal_conditions"]
        == selected_condition
    ]

# Blood type filter
if selected_blood != "All":

    df_filtered = df_filtered[
        df_filtered["blood_type"]
        == selected_blood
    ]

# ==========================
# KPIs
# ==========================
col1, col2 = st.columns(2)

col1.metric(
    "Total Mothers",
    len(df_filtered)
)

col2.metric(
    "Average Maternal Age",
    round(df_filtered["age"].mean(), 1)
)

st.divider()

# ==========================
# BLOOD TYPE DATA
# ==========================
blood_type_df = (
    df_filtered["blood_type"]
    .value_counts()
    .reset_index()
)

blood_type_df.columns = [
    "blood_type",
    "total"
]

# ==========================
# CHARTS
# ==========================
col1, col2 = st.columns(2)

with col1:

    fig_age = px.histogram(
        df_filtered,
        x="age",
        nbins=10,
        title="Maternal Age Distribution",
        color_discrete_sequence=neocare_colors
    )

    st.plotly_chart(
        fig_age,
        use_container_width=True
    )

with col2:

    fig_blood = px.pie(
        blood_type_df,
        values="total",
        names="blood_type",
        hole=0.4,
        title="Blood Type Distribution",
        color_discrete_sequence=neocare_colors
    )

    st.plotly_chart(
        fig_blood,
        use_container_width=True
    )

# ==========================
# MATERNAL CONDITIONS
# ==========================
conditions_df = (
    df_filtered["maternal_conditions"]
    .value_counts()
    .reset_index()
)

conditions_df.columns = [
    "maternal_conditions",
    "total"
]

st.subheader("Maternal Risk Factors")

fig_conditions = px.bar(
    conditions_df,
    x="maternal_conditions",
    y="total",
    title="Frequency of Maternal Conditions",
    color_discrete_sequence=neocare_colors
)

st.plotly_chart(
    fig_conditions,
    use_container_width=True
)

# ==========================
# TABLE
# ==========================
st.subheader("Mother Records")

display_df = df_filtered.drop(
    columns=["id_mother"],
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