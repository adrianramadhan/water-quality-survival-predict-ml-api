import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import pickle

# Load the data
data = pd.read_csv('app/data/dataset.csv')

# check missing values
print("Checking missing value")
print(data.isnull().sum())

# handle missing values
data = data.dropna()

# Split the data into X and y
# Separating input features (X) and target variable (y)
X = data.drop('Survival Rate', axis=1)
y = data['Survival Rate']

# train the model
model = RandomForestClassifier()
model.fit(X, y)

print(type(model))


# save the model
# joblib.dump(model, 'app/data/survival_model.pkl')
with open('app/data/survival_model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("Model has been trained and saved as survival_model.pkl")