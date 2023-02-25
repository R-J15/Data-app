import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "covid.png")
DATA_PATH = os.path.join(dir_of_interest, "data", "covid_worldwide.csv")

st.title("Dashboard - Covid_Worldwide Data")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

case = st.selectbox("Select the Country:", df['Country'].unique())


fig_1 = px.bar(df[df['Country'] == case], x="Total Cases")
st.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['Country'] == case], y="Total Cases")
st.plotly_chart(fig_2, use_container_width=True)