import pandas as pd
import numpy as np

def fetch_all_water_quality_data():
    file_path = 'app/data/dataset_with_survival_rate.xlsx'
    data = pd.read_excel(file_path)

    # Handle missing values or anomalies if needed
    data = data[['DO', 'Salinitas', 'pH', 'TDS', 'Suhu', 'survival_rate']].dropna()  # Select relevant columns and remove rows with NaN values

    return data.to_dict(orient='records')

def generate_random_water_quality_data(num_rows=100000):
    """
    Generate random water quality data with specified characteristics and save it to an Excel file.
    """
    # Generate random values for each parameter
    data = {
        'DO': np.random.uniform(0.0, 8.0, num_rows),  # Dissolved Oxygen in mg/L
        'Suhu': np.random.uniform(0.0, 50.0, num_rows),  # Temperature in Celsius
        'pH': np.random.uniform(0.0, 9.0, num_rows),  # pH level
        'Salinitas': np.random.uniform(0.0, 35.0, num_rows),  # Salinity in ppt
        'TDS': np.random.randint(0, 1200, num_rows)  # Total Dissolved Solids in mg/L
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Save the data to a file
    file_path = 'app/data/dataset_generated.xlsx'
    df.to_excel(file_path, index=False)
    print(f"Generated and saved random water quality data to '{file_path}'")
    return file_path
