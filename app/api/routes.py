from flask import Blueprint, request, jsonify
from app.core.use_cases import predict_survival_rate
from app.core.use_cases import get_water_quality_data

# Create a blueprint for the API routes
api_bp = Blueprint('/', __name__)

@api_bp.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome to the Shrimp Survival API!'})

# Define a route for the predict endpoint
@api_bp.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    data = request.json
    
    # Extract the required variables
    do = data.get('do')
    ph = data.get('ph')
    temperature = data.get('temperature')
    turbidity = data.get('turbidity')
    
    # Validate input
    if do is None or ph is None or temperature is None or turbidity is None:
        return jsonify({'error': 'Missing one or more required parameters'}), 400

    # Call the use case to predict the survival rate
    survival_rate, anomaly_detected = predict_survival_rate(do, ph, temperature, turbidity)
    
    # Return the result as a JSON response
    return jsonify({
        'survival_rate': survival_rate,
        'anomaly_detected': anomaly_detected
    })

# Define a route for the water quality endpoint
@api_bp.route('/water-quality', methods=['GET'])
def water_quality():
    # Retrieve water quality data using the use case
    data = get_water_quality_data()

    # Return the data as a JSON response
    return jsonify(data)
