import streamlit as st
import pandas as pd
import joblib
from utils import user_input_features

# Load model and columns
model = joblib.load('../models/readmission_model.pkl')
columns = pd.read_csv('../data/cleaned_healthcare_data.csv', nrows=1).drop('Readmitted', axis=1).columns

# App UI
st.set_page_config(page_title="Hospital Readmission Risk", layout="centered")
st.title("🏥 Hospital Readmission Risk Prediction")

# Sidebar for user inputs
user_input_df = user_input_features(columns)

# Predict
if st.button("Predict Readmission Risk"):
    prediction = model.predict(user_input_df)
    st.subheader("🔍 Prediction")
    st.write("**Likely to be Readmitted**" if prediction[0] == 1 else "**Not likely to be Readmitted**")
