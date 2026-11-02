import streamlit as st
from data import ACTIVITIES

st.title("Activity finder")
for activity in ACTIVITIES:
    st.write(activity["name"])
