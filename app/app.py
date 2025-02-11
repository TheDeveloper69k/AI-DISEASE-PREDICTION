import streamlit as st
import numpy as np
import pandas as pd
import joblib

# ✅ Load the trained model
model = joblib.load(r"C:\Users\hiten\GitHub\AI-Disease-Prediction\models\disease_model.pkl")

# ✅ Load dataset to get feature names
df = pd.read_csv(r"C:\Users\Acer\Desktop\AI-Disease-Prediction\data\disease_data.csv")
symptoms = df.columns[:-1]  # Get symptom names (excluding "Disease")

# ✅ Streamlit Web App
st.title("🩺 AI Disease Prediction System")
st.write("Enter your symptoms and get an AI-based prediction.")

# Create checkboxes for symptoms
user_input = []
for symptom in symptoms:
    user_response = st.radio(f"Do you have {symptom}?", ("No", "Yes"))
    user_input.append(1 if user_response == "Yes" else 0)  # Convert to 1/0

# Predict button
if st.button("Predict Disease"):
    input_array = np.array([user_input]).reshape(1, -1)  # Convert to NumPy array
    predicted_disease = model.predict(input_array)
    st.success(f"🤖 AI Prediction: You may have **{predicted_disease[0]}**")
