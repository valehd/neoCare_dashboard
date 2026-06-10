import streamlit as st

def neocare_css():

    st.markdown(
        """
        <style>

        .stApp {
            background-color: #F8FAFC;
        }

        h1 {
            color: #1F4E79;
        }

        h2 {
            color: #1F4E79;
        }

        h3 {
            color: #1F4E79;
        }

        </style>
        """,
        unsafe_allow_html=True
    )