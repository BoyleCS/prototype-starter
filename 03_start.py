import streamlit as st

items = ["Robotics Lab", "Art Studio", "Chess Meetup", "Music Jam"]
st.title("Activity finder")
query = st.text_input("Search by name")

if st.button("Search"):
    for item in items:
        if query.lower() in item.lower():
            st.write(item)
