import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate random data
num_rows = 100000

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

# Save the DataFrame to an Excel file
df.to_excel('app/data/dataset_generated.xlsx', index=False)
print("Data with 100,000 rows has been saved to 'app/data/dataset_generated.xlsx'")
