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
    do = data.get('DO')
    salinitas = data.get('Salinitas')
    ph = data.get('pH')
    tds = data.get('TDS')
    suhu = data.get('Suhu')
    
    # Validate input
    if None in [do, salinitas, ph, tds, suhu]:
        return jsonify({'error': 'Missing one or more required parameters'}), 400

    if not all(isinstance(x, (int, float)) for x in [do, salinitas, ph, tds, suhu]):
        return jsonify({'error': 'Invalid input data type for one or more parameters'}), 400

    # Call the use case to predict the survival rate
    survival_rate, anomaly_detected = predict_survival_rate(do, salinitas, ph, tds, suhu)
    
    # Return the result as a JSON response
    return jsonify({
        'survival_rate': float(survival_rate),  # Convert to float for proper serialization
        'anomaly_detected': anomaly_detected
    })

# Define a route for the water quality endpoint
@api_bp.route('/water-quality', methods=['GET'])
def water_quality():
    # Retrieve water quality data using the use case
    data = get_water_quality_data()

    # Return the data as a JSON response
    return jsonify(data)

# Define a route for the recommendation endpoint
@api_bp.route('/recommendation', methods=['POST'])
def get_recommendation():
    data = request.json
    
    # Extract the required variables
    do = data.get('DO')
    salinitas = data.get('Salinitas')
    ph = data.get('pH')
    tds = data.get('TDS')
    suhu = data.get('Suhu')
    
    # Validate input
    if None in [do, salinitas, ph, tds, suhu]:
        return jsonify({'error': 'Missing one or more required parameters'}), 400

    if not all(isinstance(x, (int, float)) for x in [do, salinitas, ph, tds, suhu]):
        return jsonify({'error': 'Invalid input data type for one or more parameters'}), 400

    # Call the model to predict survival rate
    survival_rate, anomaly_detected = predict_survival_rate(do, salinitas, ph, tds, suhu)

    # Generate recommendations
    recommendations = generate_recommendations(do, salinitas, ph, tds, suhu, anomaly_detected)
    
    return jsonify({
        "survival_rate": float(survival_rate),
        "anomaly_detected": anomaly_detected,
        "recommendation": recommendations
    })
