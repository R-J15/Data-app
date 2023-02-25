import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os
import matplotlib.pyplot as plt

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "car_i.jpeg")
DATA_PATH = os.path.join(dir_of_interest, "data", "car_df.csv")

st.title("Dashboard - Car Data")

img = image.imread(IMAGE_PATH)
st.image(img, width=500)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

brand = st.selectbox("Select the Car:", df['Brand_name'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['Brand_name'] == brand], x="Total_Price")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['Brand_name'] == brand], y="Total_Price")
col2.plotly_chart(fig_2, use_container_width=True)


fig_3 = px.bar(df, x="Brand_name", y="Total_Price",barmode = 'group')
st.plotly_chart(fig_3, use_container_width = True)