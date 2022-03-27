import streamlit as st
st.markdown('**Welcome to the exploratory data analysis application.**')
st.markdown('_Built into this application is a pipeline that can be applied to your context_')
st.markdown('**Start by loading a CSV file into the App. Please ensure that you upload a CSV file, with one sheet. If you have multiple spreadsheets, consolidate them into one**')

df = st.file_uploader('Upload a CSV')
