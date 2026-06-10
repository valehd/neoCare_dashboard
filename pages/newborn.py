
# ==========================
# IMPORTS
# ==========================
import streamlit as st
import plotly.express as px
from components.footer import show_footer
from database.queries.newborn import get_newborns


# ==========================
# PAGE TITLE
# ==========================
st.title("👶 Newborn Analysis")


# ==========================
# DATA
# ==========================
df = get_newborns()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Newborns",
    len(df)
)

col2.metric(
    "Average Weight (g)",
    round(df["weight_gr"].mean(), 0)
)

col3.metric(
    "Average APGAR 1",
    round(df["apgar_1"].mean(), 1)
)

col4.metric(
    "Average APGAR 5",
    round(df["apgar_5"].mean(), 1)
)

st.divider()

col1, col2 = st.columns(2)

with col1:

    fig_weight = px.histogram(
        df,
        x="weight_gr",
        nbins=15,
        title="Birth Weight Distribution"
    )

    st.plotly_chart(
        fig_weight,
        use_container_width=True
    )


    sex_df = (
    df["sex"]
    .value_counts()
    .reset_index()
)

sex_df.columns = [
    "sex",
    "total"
]

with col2:

    fig_sex = px.pie(
        sex_df,
        values="total",
        names="sex",
        hole=0.4,
        title="Sex Distribution"
    )

    st.plotly_chart(
        fig_sex,
        use_container_width=True
    )


    st.subheader("APGAR Scores")

apgar_df = df[["apgar_1", "apgar_5"]]

fig_apgar = px.box(
    apgar_df,
    title="APGAR Score Distribution"
)

st.plotly_chart(
    fig_apgar,
    use_container_width=True
)

st.subheader("Gestational Age")

fig_ga = px.histogram(
    df,
    x="gestational_age_physical_exam",
    nbins=10,
    title="Gestational Age Distribution"
)

st.plotly_chart(
    fig_ga,
    use_container_width=True
)


st.subheader("Newborn Records")

display_df = df.drop(
    columns=["id_newborn", "id_delivery"],
    errors="ignore"
)

st.dataframe(
    display_df,
    use_container_width=True
)

show_footer()