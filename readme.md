# Water Quality and Survival Rate Predict ML API

## Description

The `water-quality-and-survival-rate-predict-ml-api` project is designed to predict the survival rate of shrimp in a pond based on four key water quality variables:

- **DO (Dissolved Oxygen)**
- **pH**
- **Water Temperature**
- **Turbidity**

The project uses a Random Forest algorithm to detect anomalies in water quality and predict the shrimp survival rate (the `y` variable). This API is built with Python, Flask, and Scikit-learn, and is intended to be consumed by a front-end application, specifically for shrimp pond management.

## Getting Started

To get started with the `water-quality-ml-api` project, follow the instructions below.

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- pip (Python package installer)
- MySQL database
- Pandas
- Scikit-learn
- Pickle
- Flask

### Train the Model

Before running the application, you'll need to train the Random Forest model on your dataset. You can either use a real dataset or a dummy dataset for testing purposes.

1. **Prepare the Dataset**:

   - Ensure your dataset contains the following columns: `DO`, `pH`, `Water Temperature`, `Turbidity`, and `Survival Rate`.

2. **Train the Model**:
   - Run the script to train the model:
   ```bash
   train_model.py
   ```

This will generate a trained Random Forest model stored in the models directory.

### Running the Application

To start the Flask application, use the following commands:

1. **Install Dependencies**:

```
    pip install -r requirements.txt
```

2. **Run the Application:**:

```
    python run.py
```

The Flask application will start and be available at http://localhost:5000.

### API

The water-quality-ml-api exposes several endpoints to interact with the trained model and water quality data.

**Predict Survival Rate**:

- Endpoint: api/predict
- Method: POST
- Request Body

```
    {
       "pH": 7.2,
       "Turbidity": 3.5,
       "do": 6.5,
       "temperature": 28.5,
    }
```

- Response

```
{
    "survival_rate": 90,
    "anomaly_detected": false
}
```

**Get Water Quality Data:**:

- Endpoint: api/data
- Method: GET
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

**Anomaly Recommendation:**:

- Endpoint: api/recommendation
- Method: POST
- Request Body
```
   {
    "do": 3.5,
    "ph": 6.2,
    "temperature": 26.5,
    "turbidity": 22.0
   }
```

- Response

```
{
    "anomaly_detected": true,
    "recommendation": [
        "Increase Dissolved Oxygen by adding aeration.",
        "Adjust the pH by adding alkaline substances.",
        "Check the water source for possible contamination."
    ],
    "survival_rate": 75.0
}
```
