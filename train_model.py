import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# Load the modified dataset with Survival Rate
data = pd.read_excel('app/data/dataset_filled.xlsx')

# Visualisasi distribusi TDS, pH, dan Survival Rate
plt.figure(figsize=(12, 6))

# TDS Distribution
plt.subplot(1, 2, 1)
sns.histplot(data['TDS'], kde=True, color='blue', bins=30)
plt.title('Distribusi TDS')

# pH Distribution
plt.subplot(1, 2, 2)
sns.histplot(data['pH'], kde=True, color='green', bins=30)
plt.title('Distribusi pH')

plt.tight_layout()
plt.show()

# Visualisasi distribusi survival rate
plt.figure(figsize=(8, 6))
sns.histplot(data['Survival Rate'], kde=True, color='purple', bins=30)
plt.title('Distribusi Survival Rate')
plt.show()

# Check for missing values
print("Checking missing values")
print(data.isnull().sum())

# Drop any remaining rows with missing values
data = data.dropna()

# Separate input features (X) and target variable (y)
X = data[['TDS', 'pH']]  # Gunakan kolom input yang diperlukan
y = data['Survival Rate']

# Split data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy * 100:.2f}%")

# Visualisasi Feature Importances
plt.figure(figsize=(8, 6))
feature_importances = model.feature_importances_
features = X.columns

sns.barplot(x=feature_importances, y=features, palette='viridis')
plt.title('Feature Importances')
plt.xlabel('Importance')
plt.show()

# Save the trained model
with open('app/data/survival_model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("Model has been trained and saved as survival_model.pkl")
