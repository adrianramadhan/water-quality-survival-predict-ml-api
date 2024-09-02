from flask import Blueprint, request, jsonify
from app.core.use_cases import predict_survival_rate
from app.core.use_cases import get_water_quality_data
from app.core.use_cases import generate_recommendations

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

@api_bp.route('/recommendation', methods=['POST'])
def get_recommendation():
    data = request.json
    do = data['do']
    ph = data['ph']
    temperature = data['temperature']
    turbidity = data['turbidity']
    
    # Call the model to predict survival rate (assuming the function exists)
    survival_rate, anomaly_detected = predict_survival_rate(do, ph, temperature, turbidity)
    
    # Generate recommendations
    recommendations = generate_recommendations(do, ph, temperature, turbidity, anomaly_detected)
    
    return jsonify({
        "survival_rate": survival_rate,
        "anomaly_detected": anomaly_detected,
        "recommendation": recommendations
    })