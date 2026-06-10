
# ==========================
# IMPORTS
# ==========================
import streamlit as st
import plotly.express as px
from components.footer import show_footer
from components.sidebar import show_sidebar
from components.header import show_header
from components.theme import neocare_colors
from database.queries.newborn import get_newborns


show_header()
show_sidebar()


# ==========================
# PAGE TITLE
# ==========================
st.title("Newborn Analysis")

# ==========================
# DATA
# ==========================
df = get_newborns()



# ==========================
# FILTERS
# ==========================

st.subheader("Filters")

col1, col2 = st.columns(2)

with col1:

    selected_sex = st.selectbox(
        "Sex",
        ["All"] + sorted(
            df["sex"].dropna().unique()
        )
    )

with col2:

    min_weight = int(df["weight_gr"].min())
    max_weight = int(df["weight_gr"].max())

    weight_range = st.slider(
        "Birth Weight Range (g)",
        min_weight,
        max_weight,
        (min_weight, max_weight)
    )

# ==========================
# APPLY FILTERS
# ==========================

df_filtered = df.copy()

# Sex filter
if selected_sex != "All":

    df_filtered = df_filtered[
        df_filtered["sex"] == selected_sex
    ]

# Weight filter
df_filtered = df_filtered[
    (df_filtered["weight_gr"] >= weight_range[0]) &
    (df_filtered["weight_gr"] <= weight_range[1])
]



col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Newborns",
    len(df_filtered)
)

col2.metric(
    "Average Weight (g)",
    round(df_filtered["weight_gr"].mean(), 0)
)

col3.metric(
    "Average APGAR 1",
    round(df_filtered["apgar_1"].mean(), 1)
)

col4.metric(
    "Average APGAR 5",
    round(df_filtered["apgar_5"].mean(), 1)
)

st.divider()

col1, col2 = st.columns(2)

with col1:

    fig_weight = px.histogram(
        df_filtered,
        x="weight_gr",
        nbins=15,
        title="Birth Weight Distribution",
        color_discrete_sequence=neocare_colors
    )

    st.plotly_chart(
        fig_weight,
        use_container_width=True
    )


    sex_df = (
    df_filtered["sex"]
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
        title="Sex Distribution",
        color_discrete_sequence=neocare_colors
    )

    st.plotly_chart(
        fig_sex,
        use_container_width=True
    )


    st.subheader("APGAR Scores")

apgar_df = df_filtered[["apgar_1", "apgar_5"]]

fig_apgar = px.box(
    apgar_df,
    title="APGAR Score Distribution",
    color_discrete_sequence=neocare_colors
)

st.plotly_chart(
    fig_apgar,
    use_container_width=True
)

st.subheader("Gestational Age")

fig_ga = px.histogram(
    df_filtered,
    x="gestational_age_physical_exam",
    nbins=10,
    title="Gestational Age Distribution",
    color_discrete_sequence=neocare_colors
)

st.plotly_chart(
    fig_ga,
    use_container_width=True
)


st.subheader("Newborn Records")

display_df = df_filtered.drop(
    columns=["id_newborn", "id_delivery"],
    errors="ignore"
)

with st.expander("View Records"):

    st.dataframe(
        display_df,
        use_container_width=True
    )

show_footer()
