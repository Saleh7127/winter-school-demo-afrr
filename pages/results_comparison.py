import streamlit as st
import pandas as pd
# Dictionary of SHAP importance plots (two images per model)
shap_plots = [
    {
        "name": "Testing with Same Model-LightGBM",
        "plot": "images/testing-same-model.png",
        "true_pred_down": "16.268",
        "true_pred_up": "49.004",
        "bench_true_down": "19.261",
        "bench_true_up" : "60.138",
    },
    {
        "name": "Testing By Re-training Model-LightGBM",
        "plot": "images/testing-retrain.png",
        "true_pred_down": "13.182 ",
        "true_pred_up": "41.675",
        "bench_true_down": "19.261",
        "bench_true_up" : "60.138",
    }
]


st.title("Testing with Benchmark")
st.subheader("How Sliding Window testing works for LightGBM?")
st.write("""The following figure illustrates the training procedure defined by experts. The model is trained for a fixed period (60 or 90 days) and generates predictions for the next 48 hours. However, performance metrics are calculated only for the final 24 hours of the test window, as the first 24 hours are considered less critical. The evaluation includes comparisons against both true and benchmark values. Two training approaches were tested: retraining the model at each step versus continuously updating the existing model with new data. The results indicate that extending the training window improves Down value predictions, and retraining the model yields better performance compared to incremental updates. """)
st.image("images/sliding_window.png", caption=f"Testing process", use_column_width=True)

# Sidebar model selection
st.sidebar.header("Select Model")
selected_model_name = st.sidebar.selectbox("Choose a model", [model["name"] for model in shap_plots])

# Find the corresponding model dictionary
selected_model = next(model for model in shap_plots if model["name"] == selected_model_name)

metrics_data = {
    "Metric": ["Down MAE", "Up MAE"],
    "True vs Predicted": [selected_model["true_pred_down"], selected_model["true_pred_up"]],
    "True vs Benchmark": [selected_model["bench_true_down"], selected_model["bench_true_up"]],
}

# Convert dictionary to DataFrame
df_metrics = pd.DataFrame(metrics_data)

# Display the table
st.subheader("Performance Metrics")
st.table(df_metrics)


# Display SHAP plot
st.subheader(f"Results comparison with benchmark: {selected_model['name']}")
st.image(selected_model["plot"], caption=f"{selected_model['name']} - Comparison with Benchmark", use_column_width=True)