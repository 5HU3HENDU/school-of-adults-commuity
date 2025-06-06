import streamlit as st

st.set_page_config(
    layout="wide"   
)

st.title(":school: SofA")

st.header("School Of Adults")

st.divider()

# Insert wordcloud

"""
School of Adults, is a community based platform to navigate every aspect of adulthood!

The idea is to question, discuss and document everything which is _needed_ to live a noise-free and quality life.
"""



st.subheader("Philosophy")

"""
- School time was fun but it didn't prepare us for the real world.
- If we know the question, we can get the answer using Google/AI tools.
- **But what if we don't even know the questions?**
- Everyone is great in something.
"""


st.code("""SofA = Quality People
        + Different Backgrounds
        + Versatile Domains
        + Community
        + Structured Discussions
        + Neat Documentation
        """)


# st.write(st.__version__)




# Sample data: A list of strings
data = [
    "<a href='https://schoolofadults.com/health_food' class='mylink' style='text-decoration: none;'>🍱 Food, Water and Air</a>",
    "<a href='https://schoolofadults.com/health_exercise' class='mylink' style='text-decoration: none;'>🧘 Exercise and Fitness</a>",
    "<a href='https://schoolofadults.com/health_check' class='mylink' style='text-decoration: none;'>🩺 Check Up</a>",
    "<a href='https://schoolofadults.com/health_mental' class='mylink' style='text-decoration: none;'>🧠 Mental Health</a>",
    "<a href='https://schoolofadults.com/health_periods' class='mylink' style='text-decoration: none;'>🗓️ Periods</a>",
    "<a href='https://schoolofadults.com/wealth_create' class='mylink' style='text-decoration: none;'>🪙 Generating Wealth</a>",
    "<a href='https://schoolofadults.com/wealth_invest' class='mylink' style='text-decoration: none;'>💹 Investing</a>",
    "<a href='https://schoolofadults.com/wealth_insurance' class='mylink' style='text-decoration: none;'>🧿 Insurance & Tax</a>",
    "<a href='https://schoolofadults.com/wealth_spend' class='mylink' style='text-decoration: none;'>📊 Spending & Tracking</a>",
    "<a href='https://schoolofadults.com/wealth_loans' class='mylink' style='text-decoration: none;'>💳 Credit Card and Loans</a>",
    "<a href='https://schoolofadults.com/career_choose' class='mylink' style='text-decoration: none;'>🎓Choosing career</a>",
    "<a href='https://schoolofadults.com/career_job' class='mylink' style='text-decoration: none;'>💼 Finding Jobs | SofA</a>",
    "<a href='https://schoolofadults.com/career_ladder' class='mylink' style='text-decoration: none;'>🪜Career Ladder | SofA</a>",
    "<a href='https://schoolofadults.com/career_resignation' class='mylink' style='text-decoration: none;'>Resignation</a>",
    "<a href='https://schoolofadults.com/home_garden' class='mylink' style='text-decoration: none;'>🌱Garden</a>",
    "<a href='https://schoolofadults.com/pets_cats' class='mylink' style='text-decoration: none;'>🐱Cats</a>",
    "<a href='https://schoolofadults.com/pets_dogs' class='mylink' style='text-decoration: none;'>🐶Dogs</a>",
    "<a href='' class='mylink'></a>"


]


# Input box for search query
search_query = st.text_input("Enter a search term:")

# Filter the data based on the search query
if search_query:
    filtered_data = [item for item in data if search_query.lower() in item.lower()]
else:
    filtered_data = data  # Show all data if no query is entered

# Display the filtered results
st.subheader("Topics:")
if filtered_data:
      st.markdown(' '.join(filtered_data), unsafe_allow_html = True)
else:
      st.write("No topics found.")







st.markdown("""

<style>
.mylink {
  display: inline-block;
  text-decoration: none;
  padding: 0.5em;
  margin: 0.1em;
  border-radius: 0.25em; /* Rounded corners */
  font-weight: bold;
  text-align: center;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Slight shadow for elevation */
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.mylink:hover {
  text-decoration: none;
  background-color: #0068C9;
  color: white;
  transform: translateY(-2px); /* Slight lift on hover */
}

.mylink:active {
  text-decoration: none;
  transform: translateY(0); /* Reset lift on click */
}


</style>

""", unsafe_allow_html = True)

