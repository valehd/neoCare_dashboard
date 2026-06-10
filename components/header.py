def show_header():

    col1, col2 = st.columns([1, 6])

    with col1:
        st.image(
            "assets/logo/neoCare_logo.png",
            width=100
        )

    with col2:
        st.title("Maternal Analysis")
        st.caption("NeoCare Dashboard")