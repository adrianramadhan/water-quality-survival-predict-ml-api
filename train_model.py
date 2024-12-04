import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset with Survival Rate
data = pd.read_excel('app/data/dataset_with_survival_rate.xlsx')

# Visualisasi distribusi DO, Salinitas, pH, TDS, Suhu, dan Survival Rate
plt.figure(figsize=(15, 10))

# DO Distribution
plt.subplot(2, 3, 1)
sns.histplot(data['DO'], kde=True, color='blue', bins=30)
plt.title('Distribusi DO')

# Salinitas Distribution
plt.subplot(2, 3, 2)
sns.histplot(data['Salinitas'], kde=True, color='orange', bins=30)
plt.title('Distribusi Salinitas')

# pH Distribution
plt.subplot(2, 3, 3)
sns.histplot(data['pH'], kde=True, color='green', bins=30)
plt.title('Distribusi pH')

# TDS Distribution
plt.subplot(2, 3, 4)
sns.histplot(data['TDS'], kde=True, color='purple', bins=30)
plt.title('Distribusi TDS')

# Suhu Distribution
plt.subplot(2, 3, 5)
sns.histplot(data['Suhu'], kde=True, color='red', bins=30)
plt.title('Distribusi Suhu')

# Survival Rate Distribution
plt.subplot(2, 3, 6)
sns.histplot(data['survival_rate'], kde=True, color='brown', bins=30)
plt.title('Distribusi Survival Rate')

plt.tight_layout()
plt.show()

# Check for missing values
print("Checking missing values")
print(data.isnull().sum())

# Drop any remaining rows with missing values
data = data.dropna()

# Separate input features (X) and target variable (y)
X = data[['DO', 'Salinitas', 'pH', 'TDS', 'Suhu']]  # Gunakan kolom input yang diperlukan
y = data['survival_rate']

# Split data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Calculate evaluation metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print evaluation metrics
print(f"Mean Squared Error: {mse:.2f}")
print(f"R^2 Score: {r2:.2f}")

# Visualisasi Feature Importances
plt.figure(figsize=(8, 6))
feature_importances = model.feature_importances_
features = X.columns

sns.barplot(x=feature_importances, y=features, palette='viridis')
plt.title('Feature Importances')
plt.xlabel('Importance')
plt.show()

# Visualisasi Residuals
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_test - y_pred)
plt.axhline(0, color='red', linestyle='--')
plt.title('Residuals Plot')
plt.xlabel('Actual Survival Rate')
plt.ylabel('Residuals')
plt.show()

# Save the trained model
with open('app/data/survival_model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("Model has been trained and saved as survival_model.pkl")
