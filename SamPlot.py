import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_cont(data,var):
    fig, axs = plt.subplots(1, 2, figsize=(15,5))
    axs = axs.ravel()
    axs[0].set_title('Distribution')
    sns.distplot(data[var], kde=False, ax=axs[0])
    axs[1].set_title('Box-Plot')
    sns.boxplot(data[var], ax=axs[1])
    st.pyplot(fig)

def plot_cat(data,var):
    fig, axs = plt.subplots(1, 2, figsize=(15, 5))
    axs = axs.ravel()
    axs[0].set_title('Distribution')
    temp_data = data[var].value_counts()
    sns.barplot(temp_data.index, temp_data.values, ax=axs[0])
    plt.axis('off')
    st.pyplot(fig)

def plot_ContCont(data,var1,var2):
    fig, axs = plt.subplots(1, 2, figsize=(15, 5))
    axs = axs.ravel()
    axs[0].set_title('Scatter Plot')
    sns.scatterplot(data[var1], data[var2], ax=axs[0])
    plt.axis('off')
    st.pyplot(fig)

def plot_ContContReg(data,var1,var2):
    fig, axs = plt.subplots(1, 2, figsize=(15, 5))
    axs = axs.ravel()
    axs[0].set_title('Scatter Plot')
    sns.regplot(data[var1], data[var2], ax=axs[0])
    plt.axis('off')
    st.pyplot(fig)

def plot_ContContLine(data,var1,var2):
    fig, axs = plt.subplots(1, 2, figsize=(15, 5))
    axs = axs.ravel()
    axs[0].set_title('Scatter Plot')
    sns.lineplot(data[var1], data[var2], ax=axs[0])
    plt.axis('off')
    st.pyplot(fig)

def plot_ContContScatterHue(data,var1,var2,var_3):
    fig, axs = plt.subplots(1, 2, figsize=(15, 5))
    axs = axs.ravel()
    axs[0].set_title('Scatter Plot')
    sns.scatterplot(data[var1], data[var2],hue=var_3, data=data, ax=axs[0])
    plt.axis('off')
    st.pyplot(fig)

def plot_ContContLineHue(data,var1,var2,var_3):
    fig, axs = plt.subplots(1, 2, figsize=(15, 5))
    axs = axs.ravel()
    axs[0].set_title('Scatter Plot')
    sns.lineplot(data[var1], data[var2],hue=var_3, data=data, ax=axs[0])
    plt.axis('off')
    st.pyplot(fig)

def plot_CatCat(data,var1,var2):
    fig, axs = plt.subplots(2, 1, figsize=(10, 10))
    axs = axs.ravel()
    ## Aggregating value
    temp = list(data.columns.values)
    temp.remove(var1)
    temp.remove(var2)
    aggvar = temp[0]
    ## Aggregating Function
    def counting(data):
        return len(data)
    st.write('Count for *\'{}\'* and *\'{}\'* categories'.format(var1, var2))
    #Plotting Barplot
    sns.barplot(data=data, x=var1, y=aggvar, hue=var2, estimator=counting,ax=axs[0])
    axs[0].set_ylabel('Count')
    plt.show()
    #Plotting Matrix
    temp_data = pd.pivot_table(data, index=var1, columns=var2,values=aggvar, aggfunc='count')
    sns.heatmap(temp_data,ax=axs[1],annot=True,cmap="Spectral")
    st.pyplot(fig)

def plot_ContCat():
    st.write('Please Swap the Features')

def plot_CatCont(data,var1,var2):
    fig, axs = plt.subplots(1, 2, figsize=(15, 5))
    axs = axs.ravel()
    axs[0].set_title('Mean of {} across {}'.format(var2,var1))
    sns.barplot(data[var1], data[var2], ax=axs[0])
    plt.axis('off')
    st.pyplot(fig)

def plot_CatCatValue(data,var1,var2,value):
    fig, axs = plt.subplots(2, 1, figsize=(10, 10))
    axs = axs.ravel()
    st.write('Mean *\'{}\'* across *\'{}\'* and *\'{}\'* categories'.format(value,var1,var2))
    sns.barplot(data=data, x=var1, y=value, hue=var2,ax=axs[0])
    temp_data = pd.pivot_table(data, index=var1, columns=var2, values=value, aggfunc='mean')
    sns.heatmap(temp_data, annot=True, cmap="Spectral",ax=axs[1])
    st.pyplot(fig)



