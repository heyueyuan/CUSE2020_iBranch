import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import urllib
import seaborn as sns
import math
import os

@st.cache
def from_data_file(filename):
    url = ("https://raw.githubusercontent.com/crfeng1993/dataset-_for_anything/master/%s" % filename)
    data = pd.read_json(url)
    return data

#The dataset of map
dataset_map = from_data_file("02-14-2020-long-lat.json")

# Produce the map
ALL_LAYERS = {
    "Confirmed Cases": pdk.Layer(
        "ScatterplotLayer",
        data=dataset_map,
        get_position='[Long, Lat]',
        get_color='[40, 220, 160, 160]',
        get_radius='Confirmed',
        radius_scale=6,
    ),
    "Recovered Cases": pdk.Layer(
        "ScatterplotLayer",
        data=dataset_map,
        get_position='[Long, Lat]',
        get_color='[200, 30, 0, 160]',
        get_radius='Recovered',
        radius_scale=100,
    ),
    "Death Cases": pdk.Layer(
        "ScatterplotLayer",
        data=dataset_map,
        get_position='[Long, Lat]',
        get_color='[120, 30, 180, 160]',
        get_radius='Deaths',
        radius_scale=100,
    ),
}

def mapit(df):
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=110,
            zoom=4,
            pitch=50,
        ),
        layers=[Layer for Layername, Layer in ALL_LAYERS.items()
        if st.sidebar.checkbox(Layername, True)]
    ))

# import temporal data
death_df = pd.read_csv('https://raw.githubusercontent.com/crfeng1993/dataset-_for_anything/master/time_series_2019-ncov-Deaths.csv')
confirmed_df = pd.read_csv('https://raw.githubusercontent.com/crfeng1993/dataset-_for_anything/master/time_series_2019-ncov-Confirmed.csv')
recovered_df = pd.read_csv('https://raw.githubusercontent.com/crfeng1993/dataset-_for_anything/master/time_series_2019-ncov-Recovered.csv')

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

#Visual Recognition
def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.file_uploader('Please upload a X-Ray picture of lung', filenames)
    if not selected_filename:
        selected_filename = 'image.jpg'
    print(selected_filename)
    print(filenames)
    return os.path.join(folder_path, selected_filename)

st.title('CoronaVirus-2020: Visualization & Prediction')

# The sidebar's content
add_title = st.sidebar.title('Functional Segement')
add_selectbox = st.sidebar.selectbox(
    'See what we can do...',
    ('Introduction','TimeSeries Display', 'Map Distribution', 'Visual Diagnosis')
    )
if add_selectbox == 'Introduction':
    st.write("### Background Introduction")
    st.image("https://www.sciencenews.org/wp-content/uploads/2020/02/020720_ac-jl-ts_coronavirus_feat-1028x579.jpg",use_column_width=True)
    st.write('''
    The novel (new) coronavirus that was first detected in Wuhan City, Hubei Province, China. On February 11, 2020, the World Health Organization named the disease coronavirus disease 2019 (COVID-19). 
    There are tens of thousands of cases of coronavirus disease in China with the virus reportedly spreading from the close contact between person-to-person, in particular through respiratory droplets from coughs and sneezes within a range of around 6 feet.
    ''')
elif add_selectbox == 'TimeSeries Display':
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
    st.write('### Visualization: Cases Numbers fluncation Trends')
    if add_sliderbar == 'Confirmed Cases':
        plot_confirmed(add_sliderbar_c)
    elif add_sliderbar == 'Recovered Cases':
        plot_recovered(add_sliderbar_c)
    elif add_sliderbar == 'Death Cases':
        plot_death(add_sliderbar_c)
    st.write('''
    In the time series display, users would be able to check the amount changes about the confirmed, recovered and death cases of coronavirus disease in the locations. 
    We can easily found the changes based on the time. It is obvious that there is the dramatic increase in the amount of the confirmed cases in the middle stage but gradually tends towards stability. 
    At the same time, the amount of recovered and death cases increase.
    ''')
    
elif add_selectbox == 'Map Distribution':
    st.sidebar.markdown('The data displayed is updated in 14, Feb, 2020')
    st.sidebar.markdown('### Map Layers')
    df_map = from_data_file("02-14-2020-long-lat.json")
    st.write('### Visualization: Cases Distribution in China ')
    mapit(df_map)
    st.write('''
    In the map distribution display, we can quickly found out where has the large amount of the confirmed, recovered and death cases about coronavirus disease. 
    Wuhan is facing the most serious situation that should be take care.
    ''')
    
else:
    st.sidebar.markdown('''The visual recognition model is supported by IBM Watson Studio-Visual Recognition, 
                            to whom we are expressing our thanks.
                                        ---R.C., L.L., S.Z., Y.H., C.W.'''
                            )
    st.write('### Visual Recognition by X-ray Chest Pics ')
    st.image('http://news.mit.edu/sites/mit.edu.newsoffice/files/styles/news_article_image_top_slideshow/public/images/2019/MIMIC-CXR-Chest-X-Ray-00_0.jpeg?itok=gA6DgDHT',use_column_width=True)                        
    display = file_selector()
    #filename = file_selector()
    filename = 100
    st.write('You selected `%s`' % filename)
    st.write('The probability of this lung could be infected by coronvirus is `%s`' % filename)




    