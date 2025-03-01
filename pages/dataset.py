import streamlit as st
import pandas as pd
import sweetviz as sv
from streamlit.components.v1 import html

# Display DataFrame in Streamlit
st.header("📊 Dataset Overview")

# Show basic info
st.write(f"**Total Rows:** 3937")
st.write(f"**Total Columns:** 18")
st.write(f"**Total Features created based on weather data and market prices:** 48")
st.write("**Granularity:** 15,936 timestamps of 15-minute data")
st.write(f"**Target Variable:** Energy Price of Down and Up regulation")  
st.write(f"**Time Range:** **2024-06-20 22:00** -- **2024-12-01 22:00**")  

st.subheader("Plotting of sample")
st.image('images/dataset_sample.jpeg', caption=f"Plot representation of one week data", use_column_width=True)

st.subheader("Vandiagram of missing values")
st.image('images/miss_van.jpeg', caption=f"Missing values of Down, Up and when both are missing", use_column_width=True)
