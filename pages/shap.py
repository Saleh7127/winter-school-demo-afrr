import streamlit as st

# Dictionary of SHAP importance plots (two images per model)
shap_plots = {
    "LightGBM Base Down": ["images/down-state4-barplot.png", "images/down-state4-summaryplot.png"],
    "LightGBM Base Up": ["images/up-state4-barplot.png", "images/up-state4-summaryplot.png"],
    "LightGBM Extended Down": ["images/down-state5-barplot.png", "images/down-state5-summaryplot.png"],
    "LightGBM Extended Up": ["images/up-state5-barplot.png", "images/up-state5-summaryplot.png"],
}

st.title("SHAP Feature Importance Analysis")
st.subheader("What is SHAP?")
st.write("""
SHAP (SHapley Additive exPlanations) values explain how each feature influences a model’s predictions. Based on game theory, SHAP fairly distributes a prediction among input features, indicating whether a feature increases or decreases the predicted value. It helps interpret machine learning models by identifying the most important factors driving decisions. We used SHAP to determine the key features in our model and shared our findings with our partner company for validation, comparing their SHAP insights with ours.
""")

# Sidebar model selection
st.sidebar.header("Select Model")
selected_model = st.sidebar.selectbox("Choose a model", list(shap_plots.keys()))

# Display SHAP plots
st.subheader(f"SHAP Feature Importance for {selected_model}")

# Load and display two images
st.image(shap_plots[selected_model][0], caption=f"{selected_model} - SHAP Importance (Plot 1)")
st.image(shap_plots[selected_model][1], caption=f"{selected_model} - SHAP Importance (Plot 2)")

