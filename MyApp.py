import pandas as pd
import streamlit as st
from VariableTypeDetector import Detector
import SamPlot as sp
import numpy as np

st.set_option('deprecation.showfileUploaderEncoding', False)

#Header and Displaying data
st.write("![Foo](https://miro.medium.com/max/615/1*Nr8BJzXWodgpDZl-54abrQ.jpeg)")
st.write("""
# App for Exploratory Data Analysis

The Objective of this project is to Make available different types of Exploratory Data Analysis for **Clean** Data

Click to [Download](https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv) Default Data
""")

st.sidebar.header('Upload Section')
file = st.sidebar.file_uploader('Upload a Clean DataSet To Visualize',type=['csv'])
if file:
    data = pd.read_csv(file)
else:
    data = pd.read_csv('titanic.csv')

st.dataframe(data)
cols = list(data.columns.values)
cols.insert(0,'None')


#Printing the column types
st.write("""## Columns Type
Continuous/Categorical/Ordinal

PS : Since it is algorithmic determination, it wont be perfect all the time  
""")

column_type = {}
for i in data.columns:
    column_type[i] = [Detector(data[i])]
col_type_frame = pd.DataFrame(column_type)

col_type_frame_display = col_type_frame.transpose()
col_type_frame_display.columns = ['Type']
col_type_frame_display.index.name = 'Column Name'
st.dataframe(col_type_frame_display)


#User-Inputs
st.sidebar.write("Select the Data You want to see")
feature_1 = st.sidebar.selectbox('Select X-Axis Feature',cols)
temp = cols.copy()
if feature_1!='None':temp.remove(feature_1)
feature_2 = st.sidebar.selectbox('Select Y-Axis Feature',temp)

#DisplayFunctions
def display_ContCont(var_1,var_2):
    flag = st.radio("""Convert \'{}\' into Categorical? (By Binning)""".format(var_1), ['No', 'Yes'])
    if flag == 'Yes':
        no_of_bins = st.slider('Select the number of Categories for \'{}\''.format(var_1), min_value=2, max_value=10)
        q = np.linspace(0, 1, no_of_bins + 1)
        data[var_1 + '_Binned'] = pd.qcut(data[var_1], q)
        display_CatCont(var_1 + '_Binned', var_2)
    else:
        sp.plot_ContCont(data,var_1,var_2)

def display_ContCat():
    sp.plot_ContCat()

def display_CatCat(var_1,var_2):
    feature_3_check = st.radio('Target Variable',['Count','Other'])
    if feature_3_check == 'Count':
        sp.plot_CatCat(data,var_1,var_2)
    if feature_3_check == 'Other':
        global temp
        temp.remove('None')
        temp = [i for i in temp if (col_type_frame[i].values=='Continuous' or col_type_frame[i].values=='Binary Num')]
        var_3 = st.selectbox('Value',temp)
        sp.plot_CatCatValue(data,var_1,var_2,var_3)

def display_CatCont(var_1,var_2):
    flag = st.radio("""Convert \'{}\' into Categorical? (By Binning)""".format(var_2), ['No', 'Yes'])
    if flag == 'Yes':
        no_of_bins = st.slider('Select the number of Categories for \'{}\''.format(var_2), min_value=2, max_value=10)
        q = np.linspace(0, 1, no_of_bins + 1)
        data[var_2 + '_Binned'] = pd.qcut(data[var_2], q)
        display_CatCat(var_1, var_2 + '_Binned')
    else:
        sp.plot_CatCont(data,var_1,var_2)


#Plotting and Display
if (feature_1!='None'):
    st.write('# Plot')
if (feature_1!='None') & (feature_2=='None'):
    st.write("### We are exploring the Feature **{}**".format(feature_1))
    if data[feature_1].dtype!='object':
        sp.plot_cont(data,feature_1)
    else:
        sp.plot_cat(data,feature_1)

elif (feature_1=='None') & (feature_2!='None'):
    st.write("### Please Select a Feature for the X-Axis")

elif (feature_1!='None') & (feature_2!='None'):
    st.write("### We are exploring the Features **{}** and **{}**".format(feature_1,feature_2))
    if (col_type_frame[feature_1].values == 'Continuous') and (col_type_frame[feature_2].values == 'Continuous'):
        display_ContCont(feature_1,feature_2)

    elif (col_type_frame[feature_1].values == 'Continuous') and (col_type_frame[feature_2].values != 'Continuous'):
        display_ContCat()

    elif (col_type_frame[feature_1].values != 'Continuous') and (col_type_frame[feature_2].values != 'Continuous'):
        display_CatCat(feature_1,feature_2)

    else:
        display_CatCont(feature_1, feature_2)





