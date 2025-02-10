import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv(r"C:\Users\Acer\Desktop\AI-Disease-Prediction\data\disease_data.csv")

# Split dataset into features (X) and target label (y)
X = df.drop(columns=["Disease"])  # All symptoms as input
y = df["Disease"]  # Target output (disease)

# Split into 80% training and 20% testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("✅ Data Loaded and Preprocessed Successfully!")
