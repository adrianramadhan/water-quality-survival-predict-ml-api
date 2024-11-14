import pandas as pd
import numpy as np

# Load the data
data = pd.read_excel('app/data/dataset.xlsx')

# Generate random values for TDS
data['TDS'] = np.random.randint(0, 701, size=len(data))

# Generate random values for pH around 8, constrained between 6 and 9
ph_values = np.random.normal(loc=8, scale=0.5, size=len(data))  # Mean 8, StdDev 0.5
ph_values = np.clip(ph_values, 6, 9)  # Ensure values stay between 6 and 9
data['pH'] = ph_values

# Save the modified dataset to a new file
data.to_excel('app/data/dataset_randomized.xlsx', index=False)
print("Data with random TDS and pH values has been saved to 'app/data/dataset_randomized.xlsx'")
