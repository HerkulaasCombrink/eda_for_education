import streamlit as st
st.markdown('_Welcome to the exploratory data analysis application. Built into this application is a pipeline that can be applied to your context_')
df = st.file_uploader('Upload a CSV')
df
