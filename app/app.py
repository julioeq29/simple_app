import streamlit as st

st.write('Welcome to my app')

spell = st.secrets['spell']
key = st.secrets.some_magic_api.key


st.write(spell)
st.write(key)
