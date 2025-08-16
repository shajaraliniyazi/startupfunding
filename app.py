import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
st.set_page_config(layout="wide",page_title='Startup Analysis')

df= pd.read_csv('startup_clean.csv')
## load overall anaylysis
def load_overall_detail():
    st.title('Overall Detail')


    ## total invested amount
    total_money=round(df['amount'].sum())
    max_money=round(df['amount'].max())
    mean_amount=round(df.groupby('startup')['amount'].sum().mean())
    total_startup=df['startup'].nunique()


    st.metric('Total Money Invested',str(total_money) + '  Cr')
    st.metric('Max Money Invested',str(max_money) + '  Cr')
    st.metric('Mean Money Invested',str(mean_amount) + '  Cr')
    st.metric('Total Startups',str(total_startup) + '  Cr')


def load_invester_detail(inv_name):
    st.title(inv_name)
    ## load imvester deatils of last 5 innvestment
    last5_df= df[df['investers'].str.contains(inv_name)][['date','startup','vertical','city']].head(5)
    st.subheader('Most recent investment details')
    st.dataframe(last5_df)






    ## biggest investement
    big_invest=df[df['investers'].str.contains(inv_name)].groupby('startup')['amount'].sum().sort_values(ascending=False).head(5)
    st.subheader('Biggest Investment')














    col1, col2 = st.columns(2)
    with col1:

        ## SECTOR invested in
        vertical_series = df[df['investers'].str.contains(inv_name )].groupby('vertical')['amount'].sum()
        st.subheader('Sector invested in')
        fig1,ax1=plt.subplots()
        ax1.pie(vertical_series,labels=vertical_series.index)
        st.pyplot(fig1)
        ## city wise
    with col2:
        city_series = df[df['investers'].str.contains(inv_name)].groupby('city')['amount'].sum()
        st.subheader('city invested in')
        fig2, ax2 = plt.subplots()
        ax2.pie(city_series, labels=city_series.index)
        st.pyplot(fig2)


## data cleaning
df['Investors Name']=df['investers'].fillna('undisclosed ')
st.sidebar.title('Startup Funding analysis')
option=st.sidebar.selectbox('Select One',['Overall Analysis','Investor'])
if option=='Overall Analysis':

    btn0 = st.sidebar.button('Overall Analysis')
    if btn0:
        load_overall_detail()







else:
    selected_invester = st.sidebar.selectbox('Select Investor',sorted(set(df['investers'].str.split(',').sum())))
    btn2=st.sidebar.button('Find Invester  Deatail')
    if btn2:
        load_invester_detail(selected_invester)


