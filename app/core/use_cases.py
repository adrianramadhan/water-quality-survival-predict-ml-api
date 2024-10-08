import pickle
import numpy as np
from app.repositories.water_quality_repo import fetch_all_water_quality_data

# Load the trained model (assuming the model is saved in a file named 'survival_model.pkl')
with open('app/data/survival_model.pkl', 'rb') as f:
    model = pickle.load(f)
print(model)

# model = load('app/data/survival_model.pkl')
# print(type(model)) 

def predict_survival_rate(do, ph, temperature, turbidity):
    """
    Predict the survival rate of shrimp based on water quality variables.

    :param do: Dissolved Oxygen (float)
    :param ph: pH level (float)
    :param temperature: Water Temperature (float)
    :param turbidity: Turbidity (float)
    :return: Tuple of (survival_rate, anomaly_detected)
    """
    
    # Prepare the input data for prediction
    input_data = np.array([[do, ph, temperature, turbidity]])
    
    # Predict the survival rate using the RandomForest model
    survival_rate = model.predict(input_data)[0]
    
    # Example anomaly detection (customize this logic as needed)
    anomaly_detected = False
    if do < 5.0 or ph < 6.0 or temperature < 20.0 or turbidity > 20.0:
        anomaly_detected = True
    
    print(model)
    return survival_rate, anomaly_detected

def get_water_quality_data():
    """
    Retrieve water quality data from the database.

    :return: List of dictionaries containing water quality data
    """
    # Call the repository function to fetch the data
    data = fetch_all_water_quality_data()
    
    return data

def generate_recommendations(do, ph, temperature, turbidity, anomaly_detected):
    recommendations = []
    if anomaly_detected:
        if do < 4.0:
            recommendations.append("Increase Dissolved Oxygen by adding aeration.")
        if ph < 7.5 or ph > 8.5:
            recommendations.append("Adjust the pH by adding alkaline substances.")
        if turbidity > 20.0:
            recommendations.append("Check the water source for possible contamination.")
        # Add more conditions as needed
    else:
        recommendations = ["Water quality is within optimal parameters. No immediate action required."]
    
    return recommendations