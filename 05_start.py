import streamlit as st

st.title("Counter experiment")
count = 0
if st.button("Add one"):
    count = count + 1
st.write("Count:", count)
