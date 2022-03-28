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

#df = st.file_uploader('Upload a CSV')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write(df)

#making the heatmap


#Plotting the heatmap
def hitMap(df,nc,l,d):
    ax = sns.heatmap(df.corr(),cmap=sns.cubehelix_palette(nc,light=l,dark=d))
    ax.xaxis.tick_top()
    return df.corr()
def traverse_df(df):
    a,b=df.shape
    #lst_value = np.zeros(a*b)
    lst_value = []
    lst_combination = []
    k = 0;
    for i in range(0,a):
        for j in range(0,b):
            if i!=j:
                lst_combination.append((i+1,j+1))
                lst_value.append(df.iat[i,j])
                #lst_value[k] = df.iat[i,j]
                #k +=1 
    return lst_value,lst_combination

#Substitute column names with integers 
def mapColName_Int(df):
    for i in range(df.shape[1]):
       df = df.rename(columns={df.iloc[:,i].name:i+1})
    return df
#Call on previous algorithm
df_copy = mapColName_Int(df)

st.markdown('**Insert Heatmap Here**')
df_corr = hitMap(df_copy,20,0.95,0.15)
fig, ax = plt.subplots()
sns.heatmap(df_corr.corr(), ax=ax)
st.write(fig)
#sweet_report = sv.analyze(df)
#Sweet_report.show_html('sweetviz_report.html')

