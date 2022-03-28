import streamlit as st
import pandas as pd
import sweetviz as sv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#mapoutline

#initial instructions
st.markdown('**Welcome to the exploratory data analysis application.**')
st.markdown('_Built into this application is a pipeline that can be applied to your context_')
st.markdown('**Start by loading a CSV file into the App. Please ensure that you upload a CSV file, with one sheet. If you have multiple spreadsheets, consolidate them into one**')

st.markdown('_If you are unsure how to do this, please go to the following link https://www.computerhope.com/issues/ch001356.htm_')

#loading the first part of the data

df = st.file_uploader('Upload a CSV')
df2 = pd.DataFrame(
    df,
    columns=('col %d' % i for i in range(5)))

st.table(df)

st.title('Month vs. Hour Heatmap')
st.title('Dataframe')
st.table(df)
st.markdown(download_csv('Heatmap Dataframe',pd.DataFrame(df)),unsafe_allow_html=True)

#sweet_report = sv.analyze(df)
#Sweet_report.show_html('sweetviz_report.html')

