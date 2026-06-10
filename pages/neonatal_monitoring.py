# ==========================
# IMPORTS
# ==========================
import streamlit as st
import plotly.express as px
import pandas as pd
from components.theme import neocare_colors
from components.footer import show_footer
from components.header import show_header
from components.sidebar import show_sidebar
from database.queries.neonatal_monitoring import (
    get_neonatal_controls
)

# ==========================
# SIDEBAR
# ==========================
show_sidebar()

show_header()

# ==========================
# PAGE TITLE
# ==========================
st.title("Neonatal Monitoring")

# ==========================
# DATA
# ==========================
df = get_neonatal_controls()



# ==========================
# FILTERS
# ==========================

st.subheader("Filters")

selected_hour = st.selectbox(
    "Hour of Life",
    ["All", 1, 2]
)

df_filtered = df.copy()

if selected_hour != "All":

    df_filtered = df_filtered[
        df_filtered["hour_of_life"] == selected_hour
    ]

# ==========================
# KPIs - VITAL SIGNS
# ==========================
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Avg Heart Rate",
    round(df_filtered["heart_rate"].mean(), 0)
)

col2.metric(
    "Avg Respiratory Rate",
    round(df_filtered["respiratory_rate"].mean(), 0)
)

col3.metric(
    "Avg Temperature",
    round(df_filtered["temperature"].mean(), 1)
)

col4.metric(
    "Avg Oxygen Saturation",
    round(df_filtered["oxygen_saturation"].mean(), 1)
)

# ==========================
# KPIs - ADAPTATION
# ==========================
urination_rate = (
    df_filtered["urination"].mean() * 100
)

stool_rate = (
    df_filtered["stool"].mean() * 100
)

st.divider()

col1, col2 = st.columns(2)

col1.metric(
    "Urination Rate (%)",
    round(urination_rate, 1)
)

col2.metric(
    "Stool Elimination Rate (%)",
    round(stool_rate, 1)
)

# ==========================
# VITAL SIGNS DISTRIBUTION
# ==========================
st.divider()

st.subheader("Vital Signs Distribution")

# ==========================
# FIRST ROW OF CHARTS
# ==========================
col1, col2 = st.columns(2)

with col1:

    fig_hr = px.histogram(
        df_filtered,
        x="heart_rate",
        nbins=10,
        title="Heart Rate Distribution",
        color_discrete_sequence=neocare_colors
    )

    st.plotly_chart(
        fig_hr,
        use_container_width=True
    )

with col2:

    fig_rr = px.histogram(
        df_filtered,
        x="respiratory_rate",
        nbins=10,
        title="Respiratory Rate Distribution",
        color_discrete_sequence=neocare_colors
    )

    st.plotly_chart(
        fig_rr,
        use_container_width=True
    )

# ==========================
# SECOND ROW OF CHARTS
# ==========================
col1, col2 = st.columns(2)

with col1:

    fig_temp = px.histogram(
        df_filtered,
        x="temperature",
        nbins=10,
        title="Temperature Distribution",
        color_discrete_sequence=neocare_colors
    )

    st.plotly_chart(
        fig_temp,
        use_container_width=True
    )

with col2:

    fig_sat = px.histogram(
        df_filtered,
        x="oxygen_saturation",
        nbins=10,
        title="Oxygen Saturation Distribution",
        color_discrete_sequence=neocare_colors
    )

    st.plotly_chart(
        fig_sat,
        use_container_width=True
    )



hour_comparison = (
    df.groupby("hour_of_life")
      .agg({
          "temperature": "mean",
          "oxygen_saturation": "mean",
          "heart_rate": "mean",
          "respiratory_rate": "mean"
      })
      .reset_index()
)

comparison_df = hour_comparison.melt(
    id_vars="hour_of_life",
    var_name="Metric",
    value_name="Value"
)

fig_compare = px.bar(
    comparison_df,
    x="hour_of_life",
    y="Value",
    color="Metric",
    barmode="group",
    title="Vital Signs Comparison by Hour of Life",
    color_discrete_sequence=neocare_colors
)

st.plotly_chart(
    fig_compare,
    use_container_width=True
)




# ==========================
# ADAPTATION INDICATORS
# ==========================
st.divider()

st.subheader("Neonatal Adaptation Indicators")

adaptation_df = pd.DataFrame(
    {
        "Indicator": [
            "Urination",
            "Stool Elimination"
        ],
        "Percentage": [
            urination_rate,
            stool_rate
        ]
    }
)

fig_adaptation = px.bar(
    adaptation_df,
    x="Indicator",
    y="Percentage",
    title="Adaptation Indicators (%)",
    color_discrete_sequence=neocare_colors
)

st.plotly_chart(
    fig_adaptation,
    use_container_width=True
)



# ==========================
# TABLE
# ==========================

st.subheader("Monitoring Records")

display_df = df.drop(
    columns=[
        "id_control",
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