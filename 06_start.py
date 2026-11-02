import streamlit as st

st.title("Repair the search")
items = ["Robotics Lab", "Art Studio", "Chess Meetup", "Music Jam"]
query = st.text_input("Search by name")
if st.button("Search"):
    for item in items:
        if query.lower() not in item.lower():
            st.write(item)
