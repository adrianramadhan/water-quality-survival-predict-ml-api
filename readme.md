# Water Quality and Survival Rate Predict ML API

## Description

The `water-quality-and-survival-rate-predict-ml-api` project is designed to predict the survival rate of shrimp in a pond based on four key water quality variables:

- **DO (Dissolved Oxygen)**
- **Salinity**
- **pH**
- **Water Temperature**
- **Total Dissolved Solids (TDS)**

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

   - Ensure your dataset contains the following columns: `DO`, `pH`, `Water Temperature`, `TDS`, `Salinity`, and `Survival Rate`.

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
    "DO": 5.0,
    "Salinitas": 20.0,
    "pH": 7.2,
    "TDS": 250,
    "Suhu": 30.0
}

```

- Response

```
{
    "anomaly_detected": true,
    "survival_rate": 30.099853793449764
}
```

- Request Body

```
{
    "DO": 7.0,
    "Salinitas": 15.0,
    "pH": 9.0,
    "TDS": 500,
    "Suhu": 26.0
}

```

- Response

```
{
    "anomaly_detected": true,
    "survival_rate": 34.370288893660906
}
```


**Anomaly Recommendation:**:

- Endpoint: api/recommendation
- Method: POST
- Request Body
```
{
    "DO": 7.0,
    "Salinitas": 25.0,
    "pH": 7.8,
    "TDS": 350,
    "Suhu": 27.0
}
```

- Response

```
{
    "anomaly_detected": false,
    "recommendation": [
        "Water quality is within optimal parameters. No immediate action required."
    ],
    "survival_rate": 74.54531311614866
}
```

- Request Body
```
{
    "DO": 6.0,
    "Salinitas": 40.0,
    "pH": 7.5,
    "TDS": 600,
    "Suhu": 29.0
}
```

- Response

```
{
    "anomaly_detected": true,
    "recommendation": [
        "Adjust salinity to be between 15 and 25 ppt.",
        "Adjust the pH by using pH buffer solutions."
    ],
    "survival_rate": 39.5908783319008
}
```

- Request Body
```
{
    "DO": 6.0,
    "Salinitas": 22.0,
    "pH": 7.8,
    "TDS": 300,
    "Suhu": 55.0
}
```

- Response

```
{
    "anomaly_detected": true,
    "recommendation": [
        "Adjust temperature to be between 27 and 30°C."
    ],
    "survival_rate": 33.992111805857526
}
```
