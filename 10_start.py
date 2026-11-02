import streamlit as st

def process_input(value):
    # Replace this sample rule with the rule on your planning sheet.
    return value

st.title("My prototype")
value = st.text_input("Your input")
if st.button("Run"):
    result = process_input(value)
    st.write(result)
