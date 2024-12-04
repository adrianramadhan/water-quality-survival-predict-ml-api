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
    
    # Example anomaly detection
    anomaly_detected = False
    if tds < 300 or tds > 600 or ph < 7.8 or ph > 8.5:
        anomaly_detected = True
    
    return survival_rate, anomaly_detected

def get_water_quality_data():
    """
    Retrieve water quality data from the database.
    """
    data = fetch_all_water_quality_data()
    return data

def generate_recommendations(tds, ph, anomaly_detected):
    recommendations = []
    if anomaly_detected:
        if tds < 300:
            recommendations.append("Increase TDS by adding minerals.")
        elif tds > 600:
            recommendations.append("Reduce TDS by partial water replacement.")
        if ph < 7.8 or ph > 8.5:
            recommendations.append("Adjust the pH by using pH buffer solutions.")
    else:
        recommendations = ["Water quality is within optimal parameters. No immediate action required."]
    
    return recommendations
