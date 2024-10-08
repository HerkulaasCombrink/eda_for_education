import streamlit as st
import pandas as pd
#import sweetviz as sv
import numpy as np
#import matplotlib.pyplot as plt
import streamlit.components.v1 as components
#import seaborn as sns
#from IPython.display import IFrame
#import codecs

#mapoutline

#initial instructions
st.checkbox('Check me out')
st.markdown('**Welcome to the exploratory data analysis application. This is a test**')
st.button('This is another tesy')
st.button('Hit me')
st.markdown('_Built into this application is a pipeline that can be applied to your context_')
st.markdown('**Start by loading a CSV file into the App. Please ensure that you upload a CSV file, with one sheet. If you have multiple spreadsheets, consolidate them into one**')

st.markdown('_If you are unsure how to do this, please go to the following link https://www.computerhope.com/issues/ch001356.htm_')
st.markdown('_To navigate back to the main Repo, please use this link https://github.com/dsfsi/Higher_Education_EDA_')
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
#loading the first part of the data

# df = st.file_uploader('Upload a CSV') 
#uploaded_file = st.file_uploader("Choose a file")
#if uploaded_file is not None:
#  df = pd.read_csv(uploaded_file)
#  st.write(df)

  
st.markdown('**Let us assess the discriptive analysis on the variables within the dataset**')
st.markdown('***Every dataset has a distribution of data within it that can be described using a variety of measurements.***')
st.markdown('***If any of the variable summaries in the table below are unclear, please read up using this link https://www.bmj.com/about-bmj/resources-readers/publications/statistics-square-one/2-mean-and-standard-deviation.***')
#summary = df.describe()
#summary = summary.transpose()
#st.write(summary)
#making the heatmap


#Plotting the heatmap
#def hitMap(df,nc,l,d):
#    ax = sns.heatmap(df.corr(),cmap=sns.cubehelix_palette(nc,light=l,dark=d))
#    ax.xaxis.tick_top()
#    return df.corr()
#def traverse_df(df):
#    a,b=df.shape
#    #lst_value = np.zeros(a*b)
#    lst_value = []
#    lst_combination = []
 #   k = 0;
 #   for i in range(0,a):
 #       for j in range(0,b):
#            if i!=j:
 #               lst_combination.append((i+1,j+1))
 #               lst_value.append(df.iat[i,j])
 #               #lst_value[k] = df.iat[i,j]
 #               #k +=1 
 #   return lst_value,lst_combination

#Substitute column names with integers 
#def mapColName_Int(df):
#    for i in range(df.shape[1]):
#       df = df.rename(columns={df.iloc[:,i].name:i+1})
#    return df
#Call on previous algorithm
#df_copy = mapColName_Int(df)

st.markdown('**Variable correlation Heatmap**')
st.markdown('***The variable correlation Heatmap is a tool to assist in identifying associations present between variables in a given dataset.***')
st.markdown('***To find out more about Heatmaps, please visit this link https://www.jmp.com/en_ch/statistics-knowledge-portal/exploratory-data-analysis/heatmap.html .***')
#Generating the Heatmap

#df_corr = hitMap(df_copy,10,0.95,0.15)
#fig, ax = plt.subplots()
#sns.heatmap(df_corr.corr(), ax=ax,cmap= 'coolwarm')
#st.write(fig)

#Identify missing values
#df.isnull().sum()
#missing_count = df.isnull().sum()
#value_count = df.isnull().count()
#missing_percentage = round(missing_count/value_count * 100, 2)
#missing_df = pd.DataFrame({'count':missing_count,'percentage':missing_percentage})

st.markdown('**Missing data within the variables**')
st.markdown('***Some analysis may require a knowldge of wheather or not there are missing data points for each of the variables in the dataset.***')
st.markdown('***To find out more about missing values and the impact of missing values, please visit this link https://www.statisticssolutions.com/dissertation-resources/missing-values-in-data/ .***')
#st.write(missing_df)

#Identifying the highest correlation coefficient and converting the vectors into a single array
#values,combination = traverse_df(df_corr)
#values = np.asarray(values)

#def tdlist(rows,cols):
#    lst_combValue = []
#    for j in range(rows):
#        col = []
 #       for i in range(cols):
 #           col.append(0)
 #       lst_combValue.append(col)
#    return lst_combValue

#lst_comb_values = tdlist(2,10)
#lst_comb_values[0][0:len(values)] = combination# Assigning the first row to array of combinations
#lst_comb_values[1][0:len(values)] = values# Assigning the second row to array of values

#df_combValue = pd.DataFrame(lst_comb_values)# Converting the 2-D list into a dataframe
#Get rank with regard number of rows

#def getRank(df): 
#    rank = 0
#    cn = df.shape[1]
#    if cn <=3:
#        rank = cn
#    if 3<cn<=10:
#        rank = 4
#    if 10<cn<=15:
#        rank = 5
#    if cn>20:
 #       rank = 6
#    return rank     
#df_sorted = df_combValue.T.sort_values(by=1,ascending=False)

#row_rep = getRank(df_copy)
#rank = getRank(df_copy)

#Define the report dataframe given the rank
#df_report = df_sorted.head(rank)

#Define the df_report columns
#df_report.columns = ['Combinations','Values']

#Set indices base on a rank value
#indx = np.array(range(1,rank+1))
#df_report = df_report.set_index(indx)

#making the correlation coefficient table
st.markdown('**In the table below, the correlation coefficients that were used to make the heatmap are outlined**')
st.markdown('***The purpose of this is to use this table to find the top three variables that coincide with one another so that we can gain insights.***')
#st.write(df_corr)

#making the raking table, according to the correlation coefficients
st.markdown('**Ranking the top three combinations of variables**')
st.markdown('***For an exploratory data analysis to be successful, you would need to start investigating the highest impact variables first.***')
st.markdown('***In the table before, the three variable pairs with the highest correlation coefficient will be illustrated (combination = variable number; values = correlation coefficient)***')
#st.write(df_report)

#def st_display_sweetviz(report_html, width = 2000, height = 1000):
#  report_file = codecs.open(report_html,'r')
#  page = report_file.read()
#  components.html(page, width=width, height=height,scrolling = True)

#if st.button("Generate Sweetviz report"):
#  report = sv.analyze(df)
#  report.show_html()
#  st_display_sweetviz("SWEETVIZ_REPORT.html")
  
