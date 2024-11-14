from flask import Blueprint, request, jsonify
from app.core.use_cases import predict_survival_rate, get_water_quality_data, generate_recommendations

# Create a blueprint for the API routes
api_bp = Blueprint('api', __name__)


@api_bp.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome to the Shrimp Survival API!'})

# Define a route for the predict endpoint
@api_bp.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    data = request.json
    
    # Extract the required variables
    tds = data.get('tds')
    ph = data.get('ph')
    
    # Validate input
    if tds is None or ph is None:
        return jsonify({'error': 'Missing one or more required parameters'}), 400

    if not isinstance(tds, (int, float)) or not isinstance(ph, (int, float)):
        return jsonify({'error': 'Invalid input data type for tds or ph'}), 400

    # Call the use case to predict the survival rate
    survival_rate, anomaly_detected = predict_survival_rate(tds, ph)
    
    # Return the result as a JSON response
    return jsonify({
        'survival_rate': int(survival_rate),  # Convert to int for proper serialization
        'anomaly_detected': anomaly_detected
    })


# Define a route for the water quality endpoint
@api_bp.route('/water-quality', methods=['GET'])
def water_quality():
    # Retrieve water quality data using the use case
    data = get_water_quality_data()

    # Return the data as a JSON response
    return jsonify(data)

@api_bp.route('/recommendation', methods=['POST'])
def get_recommendation():
    data = request.json
    tds = data['tds']
    ph = data['ph']
    
    # Call the model to predict survival rate
    survival_rate, anomaly_detected = predict_survival_rate(tds, ph)

    # Mengonversi ke tipe data standar Python (int, float) jika perlu
    survival_rate = float(survival_rate)  # Pastikan survival_rate adalah float
    anomaly_detected = bool(anomaly_detected)  # Pastikan anomaly_detected adalah boolean
    
    # Generate recommendations
    recommendations = generate_recommendations(tds, ph, anomaly_detected)
    
    return jsonify({
        "survival_rate": survival_rate,
        "anomaly_detected": anomaly_detected,
        "recommendation": recommendations
    })
