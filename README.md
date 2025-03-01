# winter-school-demo-afrr

### Intro
The aFRR (Automatic Frequency Restoration Reserve) market plays a crucial role in balancing electricity demand and supply. However, predicting its price fluctuations is challenging due to market volatility. This project aims to develop a machine learning-based forecasting model to predict aFRR energy up and down prices for the next 48 hours. Our Streamlit app provides an interactive way to explore dataset insights, compare forecasting models, and analyze feature importance using SHAP values.

### Features 

- **Results of forecasting models** (LightGBM, Darts.LightGBM)
- **Model performance comparison** (MAE)
- **SHAP feature importance analysis**
- **Visualization of results**
- **Summary of Dataset**

## 🛠️ Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/Saleh7127/winter-school-demo-afrr.git

cd winter-school-demo-afrr

pip install streamlit==1.26.0 pandas==2.0.3 matplotlib==3.7.2 plotly==5.15.0

streamlit run home.py
