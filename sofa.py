import streamlit as st

homepage = st.Page("pages/homepage.py", title="School Of Adults", icon="🌉", default = True)

health = st.Page("pages/health.py", title="Health", icon=":dna:")



pg = st.navigation(
	{
		"Home": [homepage],
		"Health":[health]
        }
    )

pg.run()
