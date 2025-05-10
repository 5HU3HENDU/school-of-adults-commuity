import streamlit as st

homepage = st.Page("pages/homepage.py", title="School Of Adults", icon="🌉", default = True)

health = st.Page("pages/health.py")



pg = st.navigation(
	{
		"Home": [homepage], 
		"Health": [food, exercise, body_parts, health_checkup, mental_health ],
		"Wealth": [earn, stocks, mutual_fund, insurance, spend, track],
		"Career": [find_job, career_ladder, resignation],
		"Home Management": [kitchen, bedroom, living_room, bathroom, garden],
		"People Management": [self, family, parent, kids, partner, friends, enemy, office],
		"Pets": [cats, dogs],
		"Travel": [place, stay, flight, train, bus, cab, itinerary],
		"Content": [news, movies, song. book],
		"Fashion": [men, women, kid],
		"Life Skills": [driving, swimming, problem_solving],
		"Life Events": [school, college, marriage, buying_home],
		"Tech Management": [mobile, tv, earphone, power_bank],
		"Legal": [basic_legal]
		
        }
    )

pg.run()
