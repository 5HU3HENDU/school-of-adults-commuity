import streamlit as st

homepage = st.Page("pages/homepage.py", title="School Of Adults", icon="🌉", default = True)

food = st.Page("pages/health_food.py")
exercise = st.Page("pages/health_exercise.py")
body_parts = st.Page("pages/health_body_parts.py")
check = st.Page("pages/health_check.py")
mental_health = st.Page("pages/health_mental.py")

mental_health = st.Page("pages/health.py")
mental_health = st.Page("pages/health.py")
mental_health = st.Page("pages/health.py")
mental_health = st.Page("pages/health.py")
mental_health = st.Page("pages/health.py")
mental_health = st.Page("pages/health.py")


choose = st.Page("pages/career_choose.py")
job = st.Page("pages/career_job.py")
ladder = st.Page("pages/career_ladder.py")
resignation = st.Page("pages/career_resignation.py")


bathroom = st.Page("pages/home_bathroom.py")
bedroom = st.Page("pages/home_bedroom.py")
kitchen = st.Page("pages/home_kitchen.py")
living_room = st.Page("pages/home_living_room.py")
garden = st.Page("pages/home_garden.py")


enemy = st.Page("pages/people_enemy.py")
family = st.Page("pages/people_family.py")
friends = st.Page("pages/people_friends.py")
kids = st.Page("pages/peopls_kids.py")
office = st.Page("pages/people_office.py")
parents = st.Page("pages/people_parents.py")
self = st.Page("pages/people_self.py")
partner = st.Page("pages/people_partner.py")


cats = st.Page("pages/pets_cats.py")
dogs = st.Page("pages/pets_dogs.py")


mental_health = st.Page("pages/health.py")
mental_health = st.Page("pages/health.py")
mental_health = st.Page("pages/health.py")
mental_health = st.Page("pages/health.py")
mental_health = st.Page("pages/health.py")
mental_health = st.Page("pages/health.py")
mental_health = st.Page("pages/health.py")


books = st.Page("pages/content_books.py")
movies = st.Page("pages/content_movies.py")
news = st.Page("pages/content_news.py")
song = st.Page("pages/content_song.py")


men = st.Page("pages/fashion_men.py")
women = st.Page("pages/fashion_women.py")


driving = st.Page("pages/life_skills_driving.py")
problem_solving = st.Page("pages/life_skills-problem_solving.py")
swimming = st.Page("pages/life_skills_swimming.py")


buying_home = st.Page("pages/life_event_buying_home.py")
marriage = st.Page("pages/life_event_marriage.py")


mental_health = st.Page("pages/health.py")
mental_health = st.Page("pages/health.py")
mental_health = st.Page("pages/health.py")
mental_health = st.Page("pages/health.py")

basic = st.Page("pages/legal_basic.py")




pg = st.navigation(
	{
		"Home": [homepage], 
		"Health": [food, exercise, body_parts, checkup, mental_health ],
		"Wealth": [earn, stocks, mutual_fund, insurance, spend, track],
		"Career": [choose, find_job, career_ladder, resignation],
		"Home Management": [kitchen, bedroom, living_room, bathroom, garden],
		"People Management": [self, family, parent, kids, partner, friends, enemy, office],
		"Pets": [cats, dogs],
		"Travel": [place, stay, flight, train, bus, cab, itinerary],
		"Content": [news, movies, song, book],
		"Fashion": [men, women],
		"Life Skills": [driving, swimming, problem_solving],
		"Life Events": [marriage, buying_home],
		"Tech Management": [mobile, tv, earphone, power_bank],
		"Legal": [basic_legal]
		
        }
    )

pg.run()
