import streamlit as st
import pandas as pd

def user_input_features(columns):
    input_data = {}
    for col in columns:
        if "Age" in col:
            input_data[col] = st.slider(col, 0, 100, 50)
        elif "Billing" in col or "Amount" in col:
            input_data[col] = st.number_input(col, min_value=0.0, step=100.0)
        elif "Gender" in col:
            input_data[col] = st.selectbox(col, ['Male', 'Female']) == 'Female'
        elif "emergency" in col or "obese" in col:
            input_data[col] = st.checkbox(col)
        else:
            input_data[col] = st.number_input(col, step=1.0)
    return pd.DataFrame([input_data])
