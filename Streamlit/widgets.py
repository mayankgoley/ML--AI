import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name.")
if name:
    st.write(f"Hello,{name}")

# Slider

age = st.slider("Select your age:", 0, 100, 25)

st.write(f"Your age is {age}")

options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your favourite Langage:", options)
st.write(f"You have selected {choice}")

uploaded_file = st.file_uploader("Choose a CSV file", type= "csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)