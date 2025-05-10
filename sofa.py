import streamlit as st

homepage = st.Page("pages/homepage.py", title="School Of Adults", icon="🌉", default = True)



pg = st.navigation(
	{
            "Home": [homepage]
        }
    )

pg.run()
