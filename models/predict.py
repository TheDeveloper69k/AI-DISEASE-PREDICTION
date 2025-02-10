import numpy as np
import pandas as pd
import joblib

# ✅ Load the trained model
model = joblib.load(r"C:\Users\Acer\Desktop\AI-Disease-Prediction\models\disease_model.pkl")

# ✅ Load dataset to get feature names
df = pd.read_csv(r"C:\Users\Acer\Desktop\AI-Disease-Prediction\data\disease_data.csv")
symptoms = df.columns[:-1]  # Get symptom names

# ✅ Function to predict disease
def predict_disease():
    user_input = []

    print("\nEnter '1' if you have the symptom, '0' if you don't.")
    
    for symptom in symptoms:
        value = input(f"Do you have {symptom}? (1/0): ")
        user_input.append(int(value))  # Convert input to integer

    # Convert to NumPy array and reshape for model input
    input_array = np.array([user_input]).reshape(1, -1)

    # Make a prediction
    predicted_disease = model.predict(input_array)
    print(f"\n🤖 AI Prediction: You may have {predicted_disease[0]}\n")

# Run the interactive system
predict_disease()
