import streamlit as st
from matplotlib import image

st.title("Rony Joy:sunglasses:")
st.caption("Data Scientist:desktop_computer:")
st.text("Tech Enthusiast|Student|Data Scientist")
st.subheader("Lets connect...")
btn_click = st.button("Github")
if btn_click == True:
    st.text("https://github.com/R-J15")

btn_click2 = st.button("LinkedIn")
if btn_click2 == True:
    st.text("www.linkedin.com/in/rony-joy-94a1b41a5")

btn_click3 = st.button("Instagram")
if btn_click3 == True:
    img = image.imread("instaQR.jpg")
    st.image(img,width=200)