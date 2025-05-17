import streamlit as st

st.set_page_config(
   layout="wide",
   page_title= "Analyse des données de notre API MovieLenz",
   page_icon= "🎞️"
)
# Navigation
page_1 = st.Page("page1.py", title="Overview", icon="🎬")     # Film clapperboard
page_2 = st.Page("page2.py", title="Tags Insights", icon="📊")  # Bar chart
page_3 = st.Page("page3.py", title="Movie Explorer", icon="🔎") # Magnifying glass

pg = st.navigation([page_1, page_2, page_3])
pg.run()