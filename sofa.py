import streamlit as st

homepage = st.Page("pages/homepage.py", title="School Of Adults", icon="🏫", default = True)

food = st.Page('pages/health_food.py', title = 'Food and Water')
exercise = st.Page('pages/health_exercise.py', title = 'Exercise')
body_parts = st.Page('pages/health_body_parts.py', title = 'Body')
check = st.Page('pages/health_check.py', title = 'Check Up')
mental = st.Page('pages/health_mental.py', title = 'Mental Health')
periods = st.Page('pages/health_periods.py', title = 'Periods')
earn = st.Page('pages/wealth_earn.py', title = 'Earning Money')
stocks = st.Page('pages/wealth_stocks.py', title = 'Stocks')
mf = st.Page('pages/wealth_mf.py', title = 'Mutual Fund')
insurance = st.Page('pages/wealth_insurance.py', title = 'Insurance')
spend = st.Page('pages/wealth_spend.py', title = 'Spending Money')
track = st.Page('pages/wealth_track.py', title = 'Tracking Spends')
choose = st.Page('pages/career_choose.py', title = 'Choosing Career')
job = st.Page('pages/career_job.py', title = 'Job Search')
ladder = st.Page('pages/career_ladder.py', title = 'Career Ladder')
resignation = st.Page('pages/career_resignation.py', title = 'Resigning')
kitchen = st.Page('pages/home_kitchen.py', title = 'Kitchen')
bedroom = st.Page('pages/home_bedroom.py', title = 'Bedroom')
living_room = st.Page('pages/home_living_room.py', title = 'Living Room')
bathroom = st.Page('pages/home_bathroom.py', title = 'Bathroom')
garden = st.Page('pages/home_garden.py', title = 'Garden')
self = st.Page('pages/people_self.py', title = 'Self')
parents = st.Page('pages/people_parents.py', title = 'Parents')
partner = st.Page('pages/people_partner.py', title = 'Partner')
kids = st.Page('pages/people_kids.py', title = 'Kids')
friends = st.Page('pages/people_friends.py', title = 'Friends')
relatives = st.Page('pages/people_relatives.py', title = 'Relatives')
office = st.Page('pages/people_office.py', title = 'colleagues')
enemy = st.Page('pages/people_enemy.py', title = 'Enemies')
cats = st.Page('pages/pets_cats.py', title = 'Cats')
dogs = st.Page('pages/pets_dogs.py', title = 'Dogs')
place = st.Page('pages/travel_place.py', title = 'Places')
stay = st.Page('pages/travel_stay.py', title = 'Stay')
flight = st.Page('pages/travel_flight.py', title = 'Flight')
train = st.Page('pages/travel_train.py', title = 'Train')
bus = st.Page('pages/travel_bus.py', title = 'Bus')
cab = st.Page('pages/travel_cab.py', title = 'Cab')
itinerary = st.Page('pages/travel_itinerary.py', title = 'Itinerary')
things_to_carry = st.Page('pages/travel_things_to_carry.py', title = 'Things to Carry')
news = st.Page('pages/content_news.py', title = 'News')
movies = st.Page('pages/content_movies.py', title = 'Movies & Shows')
songs = st.Page('pages/content_songs.py', title = 'Songs')
books = st.Page('pages/content_books.py', title = 'Books')
men = st.Page('pages/fashion_men.py', title = 'Mental Health')
women = st.Page('pages/fashion_women.py', title = 'Women')
driving = st.Page('pages/life_skill_driving.py', title = 'Driving')
swimming = st.Page('pages/life_skill_swimming.py', title = 'Swimming')
problem_solving = st.Page('pages/life_skill_problem_solving.py', title = 'Problem Solvinng')
buying_home = st.Page('pages/life_event_buying_home.py', title = 'Buying Home')
marriage = st.Page('pages/life_event_marriage.py', title = 'Marriage')
pregnancy = st.Page('pages/life_event_pregnancy.py', title = 'Pregnancy')
new_city = st.Page('pages/life_event_new_city.py', title = 'Moving to A New City')
mobile = st.Page('pages/tech_mobile.py', title = 'Mobile')
tv = st.Page('pages/tech_tv.py', title = 'TV')
earphone = st.Page('pages/tech_earphone.py', title = 'Earphones')
power_bank = st.Page('pages/tech_power_bank.py', title = 'Power Bank')
basic = st.Page('pages/legal_basic.py', title = 'Basic')




pg = st.navigation(
	{
		"About": [homepage], 
		"Health": [food,exercise,body_parts,check,mental,periods],
		"Wealth": [earn,stocks,mf,insurance,spend,track],
		"Career": [choose,job,ladder,resignation],
		"Home": [kitchen,bedroom,living_room,bathroom,garden],
		"People": [self,parents,partner,kids,friends,relatives,office,enemy],
		"Pets": [cats,dogs],
		"Travel": [place,stay,flight,train,bus,cab,itinerary,things_to_carry],
		"Content": [news,movies,songs,books],
		"Fashion": [men,women],
		"Life Skills": [driving,swimming,problem_solving],
		"Life Events": [buying_home,marriage,pregnancy,new_city],
		"Tech": [mobile,tv,earphone,power_bank],
		"Legal": [basic]
		
        }
    )

pg.run()
