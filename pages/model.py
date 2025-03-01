import streamlit as st
import pandas as pd

models = [
    {
        "name": "LightGBM Base",
        "down_mae": 7.37,
        "up_mae": 21.50,
        "up_plot": "images/up_48_base.png", 
        "down_plot": "images/down_48_base.png", 
        "features": "22",
    },
    {
        "name": "LightGBM Extended",
        "down_mae": 8.78,
        "up_mae": 23.95,
        "up_plot": "images/up_48_ext.png",
        "down_plot": "images/down_48_ext.png",
        "features": "54",
    },
    {
        "name": "Darts.LightGBM",
        "down_mae": 9.28,
        "up_mae": 36.56,
        "up_plot": "images/up_48_darts.png",
        "down_plot": "images/down_48_darts.png",
        "features": "69"
    },
]

st.title("Model Comparison Demo")
st.sidebar.header("Select Model")
selected_model_name = st.sidebar.selectbox("Choose a model", [model["name"] for model in models])

selected_model = next(model for model in models if model["name"] == selected_model_name)


st.subheader(f"Model Performance")


col1, col2, col3 = st.columns(3)

col1.metric(label="Down MAE", value=selected_model["down_mae"])
col2.metric(label="Up MAE", value=selected_model["up_mae"])
col3.metric(label="Features Used", value=selected_model["features"])

st.subheader("Up Predictions vs Actual Values")
st.image(selected_model["up_plot"], caption=f"{selected_model['name']} - Up Predictions")

st.subheader("Down Predictions vs Actual Values")
st.image(selected_model["down_plot"], caption=f"{selected_model['name']} - Down Predictions")
