import streamlit as st
import pandas as pd
import sweetviz as sv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
#mapoutline


#Plotting the heatmap
def hitMap(df,nc,l,d):
    ax = sns.heatmap(df.corr(),cmap=sns.cubehelix_palette(nc,light=l,dark=d))
    ax.xaxis.tick_top()
    
    return df.corr()
  
#initial instructions
st.markdown('**Welcome to the exploratory data analysis application.**')
st.markdown('_Built into this application is a pipeline that can be applied to your context_')
st.markdown('**Start by loading a CSV file into the App. Please ensure that you upload a CSV file, with one sheet. If you have multiple spreadsheets, consolidate them into one**')

st.markdown('_If you are unsure how to do this, please go to the following link https://www.computerhope.com/issues/ch001356.htm_')
#loading the first part of the data

df = st.file_uploader('Upload a CSV')

df_corr = hitMap(df,20,0.95,0.15)
f,ax = plt. subplots(figsize = (10,10))
sns.heatmap(df_corr, annot = False,cmap= 'coolwarm' )
