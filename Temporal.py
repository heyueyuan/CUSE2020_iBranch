import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

# import temporal data
death_df = pd.read_csv('./time_series_2019-ncov-Deaths.csv')
confirmed_df = pd.read_csv('./time_series_2019-ncov-Confirmed.csv')
recovered_df = pd.read_csv('./time_series_2019-ncov-Recovered.csv')

# temporal plot
def plot_death(country = 'Beijing'):
    x = death_df[death_df['Province/State'] == country].values[0][4:]
    time_series = death_df.columns.values[4:]
    def time_format(date):
        return(date.split(' ')[0].split('/')[0] + \
        '-' + date.split(' ')[0].split('/')[1])
    plot_dot = {}
    plot_dot['date'] = []
    plot_dot['count'] = []
    for i in range(len(x)):
        if math.isnan(x[i]) == False:
            plot_dot['count'].append(int(x[i]))
            plot_dot['date'].append(time_format(time_series[i]))
    plot_df = pd.DataFrame(plot_dot)
    plot_df = plot_df.drop_duplicates()
    sns.relplot(x='date', y="count", data=plot_df, height=8, aspect=1.5)
    st.pyplot()

def plot_confirmed(country = 'Beijing'):
    x = confirmed_df[confirmed_df['Province/State'] == country].values[0][4:]
    time_series = confirmed_df.columns.values[4:]
    def time_format(date):
        return(date.split(' ')[0].split('/')[0] + \
        '-' + date.split(' ')[0].split('/')[1])
    plot_dot = {}
    plot_dot['date'] = []
    plot_dot['count'] = []
    for i in range(len(x)):
        if math.isnan(x[i]) == False:
            plot_dot['count'].append(int(x[i]))
            plot_dot['date'].append(time_format(time_series[i]))
    plot_df = pd.DataFrame(plot_dot)
    plot_df = plot_df.drop_duplicates()
    sns.relplot(x='date', y="count", data=plot_df, height=8, aspect=1.5)
    st.pyplot()

def plot_recovered(country = 'Beijing'):
    x = recovered_df[recovered_df['Province/State'] == country].values[0][4:]
    time_series = recovered_df.columns.values[4:]
    def time_format(date):
        return(date.split(' ')[0].split('/')[0] + \
        '-' + date.split(' ')[0].split('/')[1])
    plot_dot = {}
    plot_dot['date'] = []
    plot_dot['count'] = []
    for i in range(len(x)):
        if math.isnan(x[i]) == False:
            plot_dot['count'].append(int(x[i]))
            plot_dot['date'].append(time_format(time_series[i]))
    plot_df = pd.DataFrame(plot_dot)
    plot_df = plot_df.drop_duplicates()
    sns.relplot(x='date', y="count", data=plot_df, height=8, aspect=1.5)
    st.pyplot()

st.title("Vicualization: Map of Coronavirus's cases")
# The sidebar's content
add_title = st.sidebar.title('Functional Segement')
add_selectbox = st.sidebar.selectbox(
    'See what we can do...',
    ('TimeSeries Display', 'Map Distribution', 'Visual Diagnosis')
    )
if add_selectbox == 'TimeSeries Display':
    add_slot = st.sidebar.empty()
    add_sliderbar = st.sidebar.selectbox('Check the needed info',
    ('Confirmed Cases','Recovered Cases','Death Cases')
    )
    add_sliderbar_c = st.sidebar.selectbox(
        'location',
        ('Anhui', 'Beijing', 'Chongqing', 'Fujian', 'Gansu', 'Guangdong',
       'Guangxi', 'Guizhou', 'Hainan', 'Hebei', 'Heilongjiang', 'Henan',
       'Hubei', 'Hunan', 'Inner Mongolia', 'Jiangsu', 'Jiangxi', 'Jilin',
       'Liaoning', 'Ningxia', 'Qinghai', 'Shaanxi', 'Shandong',
       'Shanghai', 'Shanxi', 'Sichuan', 'Tianjin', 'Tibet', 'Xinjiang',
       'Yunnan', 'Zhejiang', 'Hong Kong', 'Macau', 'Taiwan',
       'Seattle, WA', 'Chicago, IL', 'Tempe, AZ')
    )
    if add_sliderbar == 'Confirmed Cases':
        plot_confirmed(add_sliderbar_c)
    elif add_sliderbar == 'Recovered Cases':
        plot_recovered(add_sliderbar_c)
    elif add_sliderbar == 'Death Cases':
        plot_death(add_sliderbar_c)


elif add_selectbox == 'Map Distribution':
    add_para_1 = st.sidebar.markdown('The data displayed is updated in 14, Feb, 2020')
else:
    add_para_2 = st.sidebar.markdown('The visual recognition model is supported by IBM Watson Studio-Visual Recognition, to whom we are expressing our thanks')
