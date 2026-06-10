# ==========================
# IMPORTS
# ==========================
import streamlit as st
import plotly.express as px
from components.footer import show_footer
from database.queries.mothers import (
    get_mothers,
    get_maternal_conditions_distribution
)

# ==========================
# PAGE TITLE
# ==========================
st.title("👩 Maternal Analysis")

# ==========================
# DATA
# ==========================
df = get_mothers()
maternal_conditions_df = get_maternal_conditions_distribution()

# ==========================
# KPIs
# ==========================

col1, col2 = st.columns(2)

col1.metric(
    "Total Mothers",
    len(df)
)

col2.metric(
    "Average Maternal Age",
    round(df["age"].mean(), 1)
)

st.divider()

# ==========================
# BLOOD TYPE DATA
# ==========================

blood_type_df = (
    df["blood_type"]
    .value_counts()
    .reset_index()
)

blood_type_df.columns = [
    "blood_type",
    "total"
]

# ==========================
# CHARTS ROW
# ==========================

col1, col2 = st.columns(2)

with col1:

    fig_age = px.histogram(
        df,
        x="age",
        nbins=10,
        title="Maternal Age Distribution"
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
        title="Blood Type Distribution"
    )

    st.plotly_chart(
        fig_blood,
        use_container_width=True
    )

# ==========================
# MATERNAL CONDITIONS
# ==========================

st.subheader("Maternal Risk Factors")

fig_conditions = px.bar(
    maternal_conditions_df.sort_values(
        "total",
        ascending=False
    ),
    x="maternal_conditions",
    y="total",
    title="Frequency of Maternal Conditions"
)

st.plotly_chart(
    fig_conditions,
    use_container_width=True
)

# ==========================
# TABLE
# ==========================

st.subheader("Mother Records")

display_df = df.drop(
    columns=["id_mother"],
    errors="ignore"
)

st.dataframe(
    display_df,
    use_container_width=True
)

# ==========================
# FOOTER
# ==========================
show_footer()