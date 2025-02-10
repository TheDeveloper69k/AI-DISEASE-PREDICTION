import pandas as pd
import os

# Define the dataset with exactly 50 diseases and their symptoms
data = {
    "Fever": [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0],
    "Cough": [1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    "Fatigue": [0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    "Sore Throat": [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    "Headache": [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1],
    "Nausea": [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1],
    "Shortness of Breath": [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
    "Body Pain": [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    "Loss of Taste": [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
    "Sweating": [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    "Disease": [
        "Flu", "COVID-19", "Malaria", "Dengue", "Food Poisoning", "Typhoid", "Pneumonia", "Vitamin Deficiency", 
        "Cold", "Bronchitis", "Asthma", "Allergy", "Tuberculosis", "Sinusitis", "Gastritis", "Hepatitis", 
        "Cholera", "Leptospirosis", "Urinary Tract Infection", "Conjunctivitis", "Stroke", "Heart Attack", 
        "Acid Reflux", "Diabetes", "High Blood Pressure", "Cirrhosis", "Liver Failure", "Chronic Fatigue Syndrome", 
        "Anemia", "Migraine", "Epilepsy", "Lung Cancer", "Kidney Infection", "Osteoarthritis", "Sickle Cell Anemia", 
        "Influenza", "Sepsis", "Gout", "HIV/AIDS", "Malnutrition", "Hyperthyroidism", "Hypothyroidism", 
        "Pneumococcal Infection", "Gallbladder Disease", "Multiple Sclerosis", "Parkinson’s Disease", 
        "Rheumatoid Arthritis", "Psoriasis", "Cystic Fibrosis", "Zika Virus"  # Removed the last 2 items
    ]
}

# Verify that all lists have the same length
for key, value in data.items():
    if len(value) != 50:
        print(f"Error: The list for '{key}' has {len(value)} items, but it should have 50.")
        exit()

# Convert dictionary to Pandas DataFrame
df = pd.DataFrame(data)

# Define the file path
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file_path = os.path.join(desktop_path, 'disease_data.csv')

# Save the dataset to the Desktop
try:
    df.to_csv(file_path, index=False)
    print(f"Dataset saved as 'disease_data.csv' on your Desktop at: {file_path}")
except Exception as e:
    print(f"An error occurred while saving the file: {e}")