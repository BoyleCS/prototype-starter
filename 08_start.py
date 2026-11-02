import streamlit as st
from data import ACTIVITIES

st.title("Activity finder")
query = st.text_input("Search by name")
category = st.selectbox("Category", ["All", "Technology", "Arts", "Games"])

if st.button("Search"):
    for activity in ACTIVITIES:
        name_matches = query.lower() in activity["name"].lower()
        category_matches = category == "All" or activity["category"] == category
        if name_matches and category_matches:
            st.write(activity["name"])
