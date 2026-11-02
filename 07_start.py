import streamlit as st

st.title("Keep a shortlist")
if "saved" not in st.session_state:
    st.session_state.saved = []

name = st.text_input("Name an activity")
if st.button("Save"):
    cleaned = name.strip()
    if cleaned and cleaned not in st.session_state.saved:
        st.session_state.saved.append(cleaned)

st.write("Saved:", st.session_state.saved)
