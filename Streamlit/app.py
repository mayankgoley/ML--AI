import streamlit as st
import pandas as pd
import numpy as np

## Title of application

st.title("Hello Streamlit")

## Display a simple text

st.write("This is a simple text")

## Create a Data Frame

df = pd.DataFrame({
    'First Column': [1,2,3,4],
    'Second Column':[10,20,30,40]
})

# Display the Data Frame
st.write("Here is the data frame")
st.write(df)