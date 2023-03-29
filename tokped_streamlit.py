import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
import matplotlib
import mapclassify
from streamlit_folium import st_folium

st.title('Analysis of Hampers Lebaran on Tokpred')


@st.cache_data
def get_data(name):
    df = pd.read_csv(name)
    return df

df = get_data('Data/tokped_clean.csv')

st.write(f"### Total data yang dikumpulkan adalah {df.shape[0]} data")


loc = st.sidebar.multiselect(label ='Select Location:', options=df['lokasi'].unique(), default='lainnya')

df1 = df.query('lokasi == @loc')

s1,s2,s3,s4 = st.columns(4)
with s1:
    st.metric(label='Total penjualan:', value=df1.shape[0])
with s2:
    st.metric(label='Average rating:', value=round(df1['rating_avg'].mean(),2))
with s3:
    st.metric(label='Average terjual:', value=round(df1['terjual'].mean(),2))
with s4:
    try:
        st.metric(label='Average harga:', value=int(df1['harga'].mean()))
    except ValueError:
        st.metric(label='Average harga:', value=0)
st.write(f"Lokasi: {loc}")


df2 = pd.DataFrame(df[df['lokasi'].isin(loc)]['lokasi'].value_counts())
try:
    fig1 = px.bar(df2, x=df2.index, y=df2['lokasi'])
    st.plotly_chart(fig1)
except ValueError:
    st.write('#### No data available!')


df3 =df[df['lokasi'].isin(loc)]
st.write('#### Boxplot package sold')
try:
    fig2= px.box(df3, x='lokasi', y='terjual')
    st.plotly_chart(fig2)
except ValueError:
    st.write('#### No data available as well!')
st.write('#### Boxplot price of the package')
try:
    fig3= px.box(df3, x='lokasi', y='harga')
    st.plotly_chart(fig3)
except ValueError:
    st.write('#### No data available as well!')

loc_terjual = st.sidebar.selectbox(label='Lokasi angka terjual:', options=df['lokasi'].unique())
val_terjual = st.sidebar.slider(label='Angka terjual:', min_value=0, max_value=int(df[df['lokasi']==loc_terjual]['terjual'].max()))
st.write('### Top hampers products according to the number of sold: (please use the tools on your left side)')
try:
    st.table(df[(df['lokasi']==loc_terjual) & (df['terjual']>=val_terjual-200) & (df['terjual']<=val_terjual)][['nama_produk','harga', 'terjual']].sample(5,replace=False))
except ValueError:
    st.table(df[(df['lokasi']==loc_terjual) & (df['terjual']>=val_terjual-200) & (df['terjual']<=val_terjual)][['nama_produk','harga', 'terjual']].head())

fav = st.select_slider(label='Wanna find the best hamper product on tokpret?', options=['no', 'yes'], value='no')
if fav=='yes':
    st.table(df[df['nama_toko']=='Ivory and Berry'].sample(1))

st.write('### Percentage people who searched "hampers lebaran" using google search and google shopping on any given time')
websuche = get_data('Data/gsws.csv')
fig4 = px.line(websuche, x=websuche['Zeit'], y=[websuche['Google Shopping'],websuche['Google Search']])
st.plotly_chart(fig4)

st.write('### Percentage people who interested in hampers lebaran according to the province: ')
dfg = gpd.read_file('Data/indo.geojson')
df_w = pd.read_csv('Data/websuche_unterrgn.csv',skiprows=2)
dfg = dfg.merge(df_w, on='Propinsi', how='left')
m = dfg.explore(tooltip=['Propinsi', 'perc'])
st_folium(m, width=700, height=400)

st.write('Are you satisfied with the analysis we provided?')
st.write('Please click the button below')
B1,B2 = st.columns(2)
with B1:
    btn = st.button('yes!')
    if btn:
        st.balloons()
        st.write('### Thank you!')
with B2:
    btn = st.button('no!')
    if btn:
        st.snow()
        st.write('### gele gele!')

