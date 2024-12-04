import pickle
import numpy as np
from app.repositories.water_quality_repo import fetch_all_water_quality_data

# Load the trained model
with open('app/data/survival_model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_survival_rate(do, salinitas, ph, tds, suhu):

    input_data = np.array([[do, salinitas, ph, tds, suhu]])
    
    survival_rate = model.predict(input_data)[0]
    
    anomaly_detected = False
    distance = 0.0

    if not (5 < do):  # DO must be > 5 ppm
        anomaly_detected = True
        distance += (5 - do) * 0.4  # Weight for DO
    if not (15 <= salinitas <= 25):  # Salinitas must be between 15 and 25 ppt
        anomaly_detected = True
        if salinitas < 15:
            distance += (15 - salinitas) * 0.3  # Weight for Salinity
        else:
            distance += (salinitas - 25) * 0.3
    if not (7.8 <= ph <= 8.5):  # pH must be between 7.8 and 8.5
        anomaly_detected = True
        if ph < 7.8:
            distance += (7.8 - ph) * 0.15  # Weight for pH
        else:
            distance += (ph - 8.5) * 0.15
    if not (300 <= tds <= 600):  # TDS must be between 300 and 600 ppm
        anomaly_detected = True
        if tds < 300:
            distance += (300 - tds) * 0.1  # Weight for TDS
        else:
            distance += (tds - 600) * 0.1
    if not (27 <= suhu <= 30):  # Suhu must be between 27 and 30°C
        anomaly_detected = True
        if suhu < 27:
            distance += (27 - suhu) * 0.05  # Weight for Temperature
        else:
            distance += (suhu - 30) * 0.05

    # Adjust survival rate based on distance from optimal conditions
    adjusted_survival_rate = max(survival_rate - distance, 0)
    
    return adjusted_survival_rate, anomaly_detected

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
