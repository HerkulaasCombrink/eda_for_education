import streamlit as st
st.markdown('_**Welcome to the exploratory data analysis application.**')
st.markdown('_Built into this application is a pipeline that can be applied to your context_')


df = st.file_uploader('Upload a CSV')
