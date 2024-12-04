import pickle
import numpy as np
from app.repositories.water_quality_repo import fetch_all_water_quality_data

# Load the trained model
with open('app/data/survival_model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_survival_rate(do, salinitas, ph, tds, suhu):
    """
    Predict the survival rate of shrimp based on water quality parameters.
    """
    # Prepare the input data for prediction
    input_data = np.array([[do, salinitas, ph, tds, suhu]])
    
    # Predict the survival rate using the RandomForest model
    survival_rate = model.predict(input_data)[0]
    
    # Check for anomalies based on optimal conditions
    anomaly_detected = False
    if not (5 < do):  # DO must be > 5 ppm
        anomaly_detected = True
    if not (15 <= salinitas <= 25):  # Salinitas must be between 15 and 25 ppt
        anomaly_detected = True
    if not (7.8 <= ph <= 8.5):  # pH must be between 7.8 and 8.5
        anomaly_detected = True
    if not (300 <= tds <= 600):  # TDS must be between 300 and 600 ppm
        anomaly_detected = True
    if not (27 <= suhu <= 30):  # Suhu must be between 27 and 30°C
        anomaly_detected = True
    
    # Adjust survival rate if anomalies are detected
    if anomaly_detected:
        survival_rate *= 0.5  # Reduce survival rate by 50% if any anomaly is detected
    
    return survival_rate, anomaly_detected

def get_water_quality_data():
    """
    Retrieve water quality data from the database.
    """
    data = fetch_all_water_quality_data()
    return data

def generate_recommendations(do, salinitas, ph, tds, suhu, anomaly_detected):
    recommendations = []
    if anomaly_detected:
        if not (5 < do):
            recommendations.append("Increase DO by aerating the water.")
        if not (15 <= salinitas <= 25):
            recommendations.append("Adjust salinity to be between 15 and 25 ppt.")
        if not (7.8 <= ph <= 8.5):
            recommendations.append("Adjust the pH by using pH buffer solutions.")
        if not (300 <= tds <= 600):
            recommendations.append("Adjust TDS to be between 300 and 600 ppm.")
        if not (27 <= suhu <= 30):
            recommendations.append("Adjust temperature to be between 27 and 30°C.")
    else:
        recommendations = ["Water quality is within optimal parameters. No immediate action required."]
    
    return recommendations
