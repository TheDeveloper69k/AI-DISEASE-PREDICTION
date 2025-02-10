import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib  # To save the model

# ✅ Step 1: Load Dataset
df = pd.read_csv(r"C:\Users\Acer\Desktop\AI-Disease-Prediction\data\disease_data.csv")

# ✅ Step 2: Split into Features (X) and Target (y)
X = df.drop(columns=["Disease"])  # Symptoms
y = df["Disease"]  # Target disease

# ✅ Step 3: Split into Training & Testing Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Step 4: Train the Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ✅ Step 5: Check Accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Training Complete! Accuracy: {accuracy * 100:.2f}%")

# ✅ Step 6: Save Model
joblib.dump(model, r"C:\Users\Acer\Desktop\AI-Disease-Prediction\models\disease_model.pkl")
print("✅ Model saved as 'disease_model.pkl'")
