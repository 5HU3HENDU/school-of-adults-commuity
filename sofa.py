import streamlit as st

homepage = st.Page("pages/homepage.py", title="School Of Adults", icon="🌉", default = True)

food = st.Page('pages/health_food.py')
exercise = st.Page('pages/health_exercise.py')
body_parts = st.Page('pages/health_body_parts.py')
check = st.Page('pages/health_check.py')
mental = st.Page('pages/health_mental.py')
periods = st.Page('pages/health_periods.py')
earn = st.Page('pages/wealth_earn.py')
stocks = st.Page('pages/wealth_stocks.py')
mf = st.Page('pages/wealth_mf.py')
insurance = st.Page('pages/wealth_insurance.py')
spend = st.Page('pages/wealth_spend.py')
track = st.Page('pages/wealth_track.py')
choose = st.Page('pages/career_choose.py')
job = st.Page('pages/career_job.py')
ladder = st.Page('pages/career_ladder.py')
resignation = st.Page('pages/career_resignation.py')
kitchen = st.Page('pages/home_kitchen.py')
bedroom = st.Page('pages/home_bedroom.py')
living_room = st.Page('pages/home_living_room.py')
bathroom = st.Page('pages/home_bathroom.py')
garden = st.Page('pages/home_garden.py')
self = st.Page('pages/people_self.py')
parents = st.Page('pages/people_parents.py')
partner = st.Page('pages/people_partner.py')
kids = st.Page('pages/people_kids.py')
friends = st.Page('pages/people_friends.py')
relatives = st.Page('pages/people_relatives.py')
office = st.Page('pages/people_office.py')
enemy = st.Page('pages/people_enemy.py')
cats = st.Page('pages/pets_cats.py')
dogs = st.Page('pages/pets_dogs.py')
place = st.Page('pages/travel_place.py')
stay = st.Page('pages/travel_stay.py')
flight = st.Page('pages/travel_flight.py')
train = st.Page('pages/travel_train.py')
bus = st.Page('pages/travel_bus.py')
cab = st.Page('pages/travel_cab.py')
itinerary = st.Page('pages/travel_itinerary.py')
things_to_carry = st.Page('pages/travel_things_to_carry.py')
news = st.Page('pages/content_news.py')
movies = st.Page('pages/content_movies.py')
songs = st.Page('pages/content_songs.py')
books = st.Page('pages/content_books.py')
men = st.Page('pages/fashion_men.py')
women = st.Page('pages/fashion_women.py')
driving = st.Page('pages/life_skill_driving.py')
swimming = st.Page('pages/life_skill_swimming.py')
problem_solving = st.Page('pages/life_skill_problem_solving.py')
buying_home = st.Page('pages/life_event_buying_home.py')
marriage = st.Page('pages/life_event_marriage.py')
pregnancy = st.Page('pages/life_event_pregnancy.py')
new_city = st.Page('pages/life_event_new_city.py')
mobile = st.Page('pages/tech_mobile.py')
tv = st.Page('pages/tech_tv.py')
earphone = st.Page('pages/tech_earphone.py')
power_bank = st.Page('pages/tech_power_bank.py')
basic = st.Page('pages/legal_basic.py')




pg = st.navigation(
	{
		"Home": [homepage], 
		"Health": [food,exercise,body_parts,check,mental,periods],
		"Wealth": [earn,stocks,mf,insurance,spend,track],
		"Career": [choose,job,ladder,resignation],
		"Home Management": [kitchen,bedroom,living_room,bathroom,garden],
		"People Management": [self,parents,partner,kids,friends,relatives,office,enemy],
		"Pets": [cats,dogs],
		"Travel": [place,stay,flight,train,bus,cab,itinerary,things_to_carry],
		"Content": [news,movies,songs,books],
		"Fashion": [men,women],
		"Life Skills": [driving,swimming,problem_solving],
		"Life Events": [buying_home,marriage,pregnancy,new_city],
		"Tech Management": [mobile,tv,earphone,power_bank],
		"Legal": [basic]
		
        }
    )

pg.run()
