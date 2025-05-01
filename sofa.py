import streamlit as st

home = st.Page("pages/home.py", title="Bombay Analytics", icon="🌉", default = True)



pg = st.navigation(
	{
            "Home": [home]
        }
    )

pg.run()
