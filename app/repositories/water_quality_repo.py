import pandas as pd
import numpy as np

def fetch_all_water_quality_data():
    file_path = 'app/data/dataset_randomized.xlsx'
    data = pd.read_excel(file_path)

    # Handle missing values or anomalies if needed
    data = data[['TDS', 'pH']].dropna()  # Select relevant columns and remove rows with NaN values

    return data.to_dict(orient='records')

def generate_random_water_quality_data(num_rows=7275):
    """
    Generate random water quality data with specified characteristics and save it to an Excel file.
    """
    # Generate random values for TDS and pH
    tds_values = np.random.randint(0, 701, num_rows)
    ph_values = np.clip(np.random.normal(loc=8, scale=0.5, size=num_rows), 6, 9)  # Most values around pH 8

    # Create a DataFrame
    data = pd.DataFrame({'TDS': tds_values, 'pH': ph_values})

    # Save the data to a file
    file_path = 'app/data/dataset_randomized.xlsx'
    data.to_excel(file_path, index=False)
    print(f"Generated and saved random water quality data to '{file_path}'")
    return file_path
