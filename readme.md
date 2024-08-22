# Water Quality ML API

## Description

The `water-quality-ml-api` project is designed to predict the survival rate of shrimp in a pond based on four key water quality variables:

- **DO (Dissolved Oxygen)**
- **pH**
- **Water Temperature**
- **Turbidity**

The project uses a Random Forest algorithm to detect anomalies in water quality and predict the shrimp survival rate (the `y` variable). This API is built with Python, Flask, and Scikit-learn, and is intended to be consumed by a front-end application, specifically for shrimp pond management.

## Project Structure

water-quality-ml-api/
├── app/
│ ├── init.py
│ ├── config.py # Configuration settings for the app (e.g., DB connection)
│ ├── models/ # Model definitions (e.g., RandomForest model)
│ │ ├── init.py
│ │ ├── model.py # ML models and related functions
│ ├── repositories/ # Data access layer
│ │ ├── init.py
│ │ ├── water_quality_repo.py # Functions to retrieve and manipulate data from DB
│ ├── services/ # Business logic
│ │ ├── init.py
│ │ ├── anomaly_detection.py # Logic for detecting anomalies using RandomForest
│ ├── controllers/ # Flask routes and request handling
│ │ ├── init.py
│ │ ├── water_quality.py # Endpoint definitions for water quality data processing
│ ├── utils/ # Utility functions
│ │ ├── init.py
│ │ ├── helpers.py # Common helper functions
│ ├── app.py # Entry point for the Flask app
├── tests/ # Unit tests for the application
│ ├── test_anomaly_detection.py
├── requirements.txt # Python dependencies
├── README.md


## Getting Started

To get started with the `water-quality-ml-api` project, follow the instructions below.

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- pip (Python package installer)
- MySQL database

### Train the Model

Before running the application, you'll need to train the Random Forest model on your dataset. You can either use a real dataset or a dummy dataset for testing purposes.

1. **Prepare the Dataset**: 
   - Ensure your dataset contains the following columns: `DO`, `pH`, `Water Temperature`, `Turbidity`, and `Survival Rate`.

2. **Train the Model**:
   - Run the script to train the model:
   ```bash
   python app/models/train_model.py

This will generate a trained Random Forest model stored in the models directory.

### Running the Application
To start the Flask application, use the following commands:

1. **Install Dependencies**: 
```
    pip install -r requirements.txt
```

2. **Run the Application:**: 
```
    python app.py
```
The Flask application will start and be available at http://localhost:5000.

### API
The water-quality-ml-api exposes several endpoints to interact with the trained model and water quality data.

**Predict Survival Rate**:
- Endpoint: /predict
- Method: POST
- Description: Predict the shrimp survival rate based on input water quality variables.
- Request Body
```
    {
        "do": 6.5,
        "ph": 7.2,
        "temperature": 28.5,
        "turbidity": 10.0
    }
```
- Response
```
{
    "survival_rate": 85.0,
    "anomaly_detected": false
}
```

**Predict Survival Rate**:
- Endpoint: /water-quality
- Method: GET
- Description: Retrieve water quality data from the database.
- Response
```
[
    {
        "do": 6.5,
        "ph": 7.2,
        "temperature": 28.5,
        "turbidity": 10.0,
        "survival_rate": 85.0
    },
]
```