import streamlit as st

homepage = st.Page("pages/homepage.py", title="School Of Adults", icon="🏫", default = True)

food = st.Page('pages/health_food.py', title = 'Food and Water', icon = '🍱')
exercise = st.Page('pages/health_exercise.py', title = 'Exercise', icon = '🧘')
body_parts = st.Page('pages/health_body_parts.py', title = 'Body', icon = '⚕️')
check = st.Page('pages/health_check.py', title = 'Check Up', icon = '🩺')
mental = st.Page('pages/health_mental.py', title = 'Mental Health', icon = '🧠')
periods = st.Page('pages/health_periods.py', title = 'Periods', icon = '🗓️')
earn = st.Page('pages/wealth_earn.py', title = 'Earning Money', icon = '🪙')
stocks = st.Page('pages/wealth_stocks.py', title = 'Stocks', icon = '💹')
mf = st.Page('pages/wealth_mf.py', title = 'Mutual Fund', icon = '💰')
insurance = st.Page('pages/wealth_insurance.py', title = 'Insurance', icon = 'ℹ️')
spend = st.Page('pages/wealth_spend.py', title = 'Spending Money', icon = '💸')
track = st.Page('pages/wealth_track.py', title = 'Tracking Spends', icon = '📊')
choose = st.Page('pages/career_choose.py', title = 'Choosing Career', icon = '🎓')
job = st.Page('pages/career_job.py', title = 'Job Search', icon = '💼')
ladder = st.Page('pages/career_ladder.py', title = 'Career Ladder', icon = '🪜')
resignation = st.Page('pages/career_resignation.py', title = 'Resigning', icon = '🗃️')
kitchen = st.Page('pages/home_kitchen.py', title = 'Kitchen', icon = '🍽️')
bedroom = st.Page('pages/home_bedroom.py', title = 'Bedroom', icon = '🛏️')
living_room = st.Page('pages/home_living_room.py', title = 'Living Room', icon = '📺')
bathroom = st.Page('pages/home_bathroom.py', title = 'Bathroom', icon = '🛁')
garden = st.Page('pages/home_garden.py', title = 'Garden', icon = '🌱')
self = st.Page('pages/people_self.py', title = 'Self', icon = 'ℹ️')
parents = st.Page('pages/people_parents.py', title = 'Parents', icon = '🧑‍🍼')
partner = st.Page('pages/people_partner.py', title = 'Partner', icon = '♥️')
kids = st.Page('pages/people_kids.py', title = 'Kids', icon = '🧒')
friends = st.Page('pages/people_friends.py', title = 'Friends', icon = '🫂')
relatives = st.Page('pages/people_relatives.py', title = 'Relatives', icon = '🌳')
office = st.Page('pages/people_office.py', title = 'colleagues', icon = '🏢')
enemy = st.Page('pages/people_enemy.py', title = 'Enemies', icon = '🥷')
cats = st.Page('pages/pets_cats.py', title = 'Cats', icon = '😼')
dogs = st.Page('pages/pets_dogs.py', title = 'Dogs', icon = '🐕')
place = st.Page('pages/travel_place.py', title = 'Places', icon = '🗻')
stay = st.Page('pages/travel_stay.py', title = 'Stay', icon = '⛺')
flight = st.Page('pages/travel_flight.py', title = 'Flight', icon = '✈️')
train = st.Page('pages/travel_train.py', title = 'Train', icon = '🚂')
bus = st.Page('pages/travel_bus.py', title = 'Bus', icon = '🚌')
cab = st.Page('pages/travel_cab.py', title = 'Cab', icon = '🚕')
itinerary = st.Page('pages/travel_itinerary.py', title = 'Itinerary', icon = '📋')
things_to_carry = st.Page('pages/travel_things_to_carry.py', title = 'Things to Carry', icon = '✅')
news = st.Page('pages/content_news.py', title = 'News', icon = '📰')
movies = st.Page('pages/content_movies.py', title = 'Movies & Shows', icon = '🍿')
songs = st.Page('pages/content_songs.py', title = 'Songs', icon = '🎵')
books = st.Page('pages/content_books.py', title = 'Books', icon = '📚')
men = st.Page('pages/fashion_men.py', title = 'Men', icon = '♂️')
women = st.Page('pages/fashion_women.py', title = 'Women', icon = '♀️')
driving = st.Page('pages/life_skill_driving.py', title = 'Driving', icon = '🚘')
swimming = st.Page('pages/life_skill_swimming.py', title = 'Swimming', icon = '🥽')
problem_solving = st.Page('pages/life_skill_problem_solving.py', title = 'Problem Solvinng', icon = '🕵️')
buying_home = st.Page('pages/life_event_buying_home.py', title = 'Buying Home', icon = '🏡')
marriage = st.Page('pages/life_event_marriage.py', title = 'Marriage', icon = '💍')
pregnancy = st.Page('pages/life_event_pregnancy.py', title = 'Pregnancy', icon = '🤰')
new_city = st.Page('pages/life_event_new_city.py', title = 'Moving to A New City', icon = '🚛')
mobile = st.Page('pages/tech_mobile.py', title = 'Mobile', icon = '📱')
tv = st.Page('pages/tech_tv.py', title = 'TV', icon = '📺')
earphone = st.Page('pages/tech_earphone.py', title = 'Earphones', icon = '🎧')
power_bank = st.Page('pages/tech_power_bank.py', title = 'Power Bank', icon = '🔋')
basic = st.Page('pages/legal_basic.py', title = 'Basic', icon = '⚖️')



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
