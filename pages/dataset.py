import streamlit as st
import pandas as pd
import sweetviz as sv
from streamlit.components.v1 import html

# Title of the app
# st.title("Data Profiling with Ydata Profiling")

df = pd.read_csv("afrr-energy-prices-fi-hourly-with-additional-features-updated-version-20250121-original-fi-hourly.csv")
if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'], axis=1)

# Display DataFrame in Streamlit
st.header("📊 Dataset Overview")

# Show basic info
st.write(f"**Total Rows:** {df.shape[0]+1}")
st.write(f"**Total Columns:** {df.shape[1]}")
st.write("**Granularity:** 15,936 timestamps of 15-minute data")
st.write(f"**Target Variable:** Energy Price of Down and Up regulation")  
st.write(f"**Time Range:** **2024-06-20 22:00** -- **2024-12-01 22:00**")  

# Show sample data
# st.subheader("🔍Sample Data of current dataframe")
# st.dataframe(df.head())

st.subheader("Plotting of sample")
st.image('images/dataset_sample.jpeg', caption=f"Plot representation of one week data", use_column_width=True)

st.subheader("Vandiagram of missing values")
st.image('images/miss_van.jpeg', caption=f"Missing values of Down, Up and when both are missing", use_column_width=True)

# st.markdown("### Ydata Profiling Report:")
# with open("ydata_report.html", "r", encoding="utf-8") as f:
#     report_html = f.read()

# html(report_html, height=800, scrolling=True)