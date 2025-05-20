import streamlit as st

# homepage = 


pg = st.navigation(
	{
		"About": [
            st.Page("pages/homepage.py", title="School Of Adults", icon="🏫", default = True)
        ], 
		"Health": [
            st.Page('pages/health_basic.py', title = 'Basics', icon = '1️⃣'),
            st.Page('pages/health_food.py', title = 'Food and Water', icon = '🍱'),
            st.Page('pages/health_exercise.py', title = 'Exercise', icon = '🧘'),
            st.Page('pages/health_body_parts.py', title = 'Body', icon = '⚕️'),
            st.Page('pages/health_check.py', title = 'Check Up', icon = '🩺'),
            st.Page('pages/health_mental.py', title = 'Mental Health', icon = '🧠'),
            st.Page('pages/health_periods.py', title = 'Periods', icon = '🗓️')
        ],
		"Wealth": [
            st.Page('pages/wealth_earn.py', title = 'Earning Money', icon = '🪙'),
            st.Page('pages/wealth_stocks.py', title = 'Stocks', icon = '💹'),
            st.Page('pages/wealth_mf.py', title = 'Mutual Fund', icon = '💰'),
            st.Page('pages/wealth_insurance.py', title = 'Insurance', icon = '🧿'),
            st.Page('pages/wealth_spend.py', title = 'Spending Money', icon = '💸'),
            st.Page('pages/wealth_track.py', title = 'Tracking Spends', icon = '📊')
    
        ],
		"Career": [
            st.Page('pages/career_choose.py', title = 'Choosing Career', icon = '🎓'),
            st.Page('pages/career_job.py', title = 'Job Search', icon = '💼'),
            st.Page('pages/career_ladder.py', title = 'Career Ladder', icon = '🪜'),
            st.Page('pages/career_resignation.py', title = 'Resigning', icon = '🗃️')
        ],
		"Home": [
            st.Page('pages/home_kitchen.py', title = 'Kitchen', icon = '🍽️'),
            st.Page('pages/home_bedroom.py', title = 'Bedroom', icon = '🛏️'),
            st.Page('pages/home_living_room.py', title = 'Living Room', icon = '📺'),
            st.Page('pages/home_bathroom.py', title = 'Bathroom', icon = '🛁'),
            st.Page('pages/home_garden.py', title = 'Garden', icon = '🌱')
        ],
		"People": [
            st.Page('pages/people_self.py', title = 'Self', icon = 'ℹ️'),
            st.Page('pages/people_parents.py', title = 'Parents', icon = '🧑‍🍼'),
            st.Page('pages/people_partner.py', title = 'Partner', icon = '♥️'),
            st.Page('pages/people_kids.py', title = 'Kids', icon = '🧒'),
            st.Page('pages/people_friends.py', title = 'Friends', icon = '🫂'),
            st.Page('pages/people_relatives.py', title = 'Relatives', icon = '🌳'),
            st.Page('pages/people_office.py', title = 'Colleagues', icon = '🏢'),
            st.Page('pages/people_enemy.py', title = 'Enemies', icon = '🥷')
            
        ],
		"Pets": [
            st.Page('pages/pets_cats.py', title = 'Cats', icon = '😼'),
            st.Page('pages/pets_dogs.py', title = 'Dogs', icon = '🐕')
            
        ],
		"Travel": [
            st.Page('pages/travel_place.py', title = 'Places', icon = '🗻'),
            st.Page('pages/travel_stay.py', title = 'Stay', icon = '⛺'),
            st.Page('pages/travel_flight.py', title = 'Flight', icon = '✈️'),
            st.Page('pages/travel_train.py', title = 'Train', icon = '🚂'),
            st.Page('pages/travel_bus.py', title = 'Bus', icon = '🚌'),
            st.Page('pages/travel_cab.py', title = 'Cab', icon = '🚕'),
            st.Page('pages/travel_itinerary.py', title = 'Itinerary', icon = '📋'),
            st.Page('pages/travel_things_to_carry.py', title = 'Things to Carry', icon = '🧳')
            
        ],
		"Content": [
            st.Page('pages/content_news.py', title = 'News', icon = '📰'),
            st.Page('pages/content_movies.py', title = 'Movies & Shows', icon = '🍿'),
            st.Page('pages/content_songs.py', title = 'Songs', icon = '🎵'),
            st.Page('pages/content_books.py', title = 'Books', icon = '📚')
        ],
		"Fashion": [
            st.Page('pages/fashion_men.py', title = 'Men', icon = '♂️'),
            st.Page('pages/fashion_women.py', title = 'Women', icon = '♀️')
        ],
		"Life Skills": [
            st.Page('pages/life_skill_driving.py', title = 'Driving', icon = '🚘'),
            st.Page('pages/life_skill_swimming.py', title = 'Swimming', icon = '🥽'),
            st.Page('pages/life_skill_problem_solving.py', title = 'Problem Solvinng', icon = '🕵️')
        ],
		"Life Events": [
            st.Page('pages/life_event_buying_home.py', title = 'Buying Home', icon = '🏡'),
            st.Page('pages/life_event_marriage.py', title = 'Marriage', icon = '💍'),
            st.Page('pages/life_event_pregnancy.py', title = 'Pregnancy', icon = '🤰'),
            st.Page('pages/life_event_new_city.py', title = 'Moving to A New City', icon = '🚛')
        ],
		"Tech": [
            st.Page('pages/tech_mobile.py', title = 'Mobile', icon = '📱'),
            st.Page('pages/tech_tv.py', title = 'TV', icon = '📺'),
            st.Page('pages/tech_earphone.py', title = 'Earphones', icon = '🎧'),
            st.Page('pages/tech_power_bank.py', title = 'Power Bank', icon = '🔋')
        ],
		"Legal": [
            st.Page('pages/legal_basic.py', title = 'Basic', icon = '⚖️')
        ]
		
        }
    )

pg.run()
