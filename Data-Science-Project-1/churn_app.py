import streamlit as st
from joblib import load

model = load('random_forest_model.joblib')

st.title("Customer Churn Prediction App")

st.header("Enter Customer Details") 

