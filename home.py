import streamlit as st

st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Home","Dataset", "Model Comparison", "SHAP Feature Importance", "Results Comparison With Benchmark"])

if page == "Home":
    st.title("Forecasting the behavior of the aFRR energy market")
    # st.subheader("The Future of Smart Energy Trading")
    # st.image("images/afrr.webp", use_column_width=True)
    video_file = open("images/intro-vid.mp4", "rb")  # Open the video file
    st.video(video_file)

    st.write("""Renewable energy is the future of power generation, however, its integration into the grid comes with challenges. The unpredictability of green energy resources, such as wind and solar, disrupts grid stability and the balance between electricity supply and demand. The Automatic Frequency Restoration Reserve (aFRR) market is essential for grid stability, automatically maintaining a grid frequency at 50Hz by balancing electricity generation and consumption. However, forecasting aFRR price fluctuations is challenging due to market volatility and external influences. This project aims to develop a machine learning model to predict up and down marginal energy prices in the aFRR energy market for the next 48 hours. The objective is to improve grid stability, lower electricity costs, and help market participants optimize their bidding strategies within the evolving energy landscape.""")

elif page == "Model Comparison":
    st.switch_page("pages/model.py") # Redirect to Model page
    
elif page == "SHAP Feature Importance":
    st.switch_page("pages/shap.py")  # Redirect to SHAP page

elif page == "Results Comparison With Benchmark":
    st.switch_page("pages/results_comparison.py")  # Redirect to Results comparison page

elif page == "Dataset":
    st.switch_page("pages/dataset.py")  # Redirect to dataset page
