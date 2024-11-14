import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the modified dataset with Survival Rate
data = pd.read_excel('app/data/dataset_filled.xlsx')

# Check for missing values
print("Checking missing values")
print(data.isnull().sum())

# Drop any remaining rows with missing values
data = data.dropna()

# Separate input features (X) and target variable (y)
X = data[['TDS', 'pH']]  # Gunakan kolom input yang diperlukan
y = data['Survival Rate']

# Train the model
model = RandomForestClassifier()
model.fit(X, y)

# Confirm model type
print(type(model))

# Save the trained model
with open('app/data/survival_model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("Model has been trained and saved as survival_model.pkl")
