import pandas as pd
import numpy as np

# Load the generated dataset
df = pd.read_excel('app/data/dataset_generated.xlsx')

# Define weights for each parameter
weights = {
    'DO': 0.40,      # Oksigen Terlarut
    'Salinitas': 0.30,  # Salinitas
    'pH': 0.15,      # pH
    'TDS': 0.10,     # Total Dissolved Solids
    'Suhu': 0.05     # Suhu
}

# Define optimal ranges
optimal_conditions = {
    'DO': (5, float('inf')),  # DO > 5 ppm
    'Salinitas': (15, 25),     # Salinitas 15-25 ppt
    'pH': (7.8, 8.5),          # pH 7.8-8.5
    'TDS': (300, 600),         # TDS 300-600 ppm
    'Suhu': (27, 30)           # Suhu 27-30°C
}

# Normalize the parameters to a scale of 0 to 1
df['DO_normalized'] = (df['DO'] - df['DO'].min()) / (df['DO'].max() - df['DO'].min())
df['Salinitas_normalized'] = (df['Salinitas'] - df['Salinitas'].min()) / (df['Salinitas'].max() - df['Salinitas'].min())
df['pH_normalized'] = (df['pH'] - df['pH'].min()) / (df['pH'].max() - df['pH'].min())
df['TDS_normalized'] = (df['TDS'] - df['TDS'].min()) / (df['TDS'].max() - df['TDS'].min())
df['Suhu_normalized'] = (df['Suhu'] - df['Suhu'].min()) / (df['Suhu'].max() - df['Suhu'].min())

# Calculate the survival rate based on the weighted sum of normalized parameters
df['survival_rate'] = (
    df['DO_normalized'] * weights['DO'] +
    df['Salinitas_normalized'] * weights['Salinitas'] +
    df['pH_normalized'] * weights['pH'] +
    df['TDS_normalized'] * weights['TDS'] +
    df['Suhu_normalized'] * weights['Suhu']
) * 100  # Scale to percentage

# Adjust survival rate based on distance from optimal conditions
def adjust_survival_rate(row):
    # Calculate distance from optimal conditions
    distance = 0.0
    
    # Check DO
    if row['DO'] <= optimal_conditions['DO'][0]:
        distance += (optimal_conditions['DO'][0] - row['DO']) * weights['DO']
    
    # Check Salinitas
    if row['Salinitas'] < optimal_conditions['Salinitas'][0]:
        distance += (optimal_conditions['Salinitas'][0] - row['Salinitas']) * weights['Salinitas']
    elif row['Salinitas'] > optimal_conditions['Salinitas'][1]:
        distance += (row['Salinitas'] - optimal_conditions['Salinitas'][1]) * weights['Salinitas']
    
    # Check pH
    if row['pH'] < optimal_conditions['pH'][0]:
        distance += (optimal_conditions['pH'][0] - row['pH']) * weights['pH']
    elif row['pH'] > optimal_conditions['pH'][1]:
        distance += (row['pH'] - optimal_conditions['pH'][1]) * weights['pH']
    
    # Check TDS
    if row['TDS'] < optimal_conditions['TDS'][0]:
        distance += (optimal_conditions['TDS'][0] - row['TDS']) * weights['TDS']
    elif row['TDS'] > optimal_conditions['TDS'][1]:
        distance += (row['TDS'] - optimal_conditions['TDS'][1]) * weights['TDS']
    
    # Check Suhu
    if row['Suhu'] < optimal_conditions['Suhu'][0]:
        distance += (optimal_conditions['Suhu'][0] - row['Suhu']) * weights['Suhu']
    elif row['Suhu'] > optimal_conditions['Suhu'][1]:
        distance += (row['Suhu'] - optimal_conditions['Suhu'][1]) * weights['Suhu']
    
    # Calculate adjusted survival rate
    adjusted_rate = row['survival_rate'] - distance
    return max(adjusted_rate, 0)  # Ensure survival rate does not go below 0

# Apply the adjustment function to the DataFrame
df['adjusted_survival_rate'] = df.apply(adjust_survival_rate, axis=1)

# Save the updated DataFrame to a new Excel file
df.to_excel('app/data/dataset_with_survival_rate.xlsx', index=False)
print("Data with adjusted survival rate has been saved to 'app/data/dataset_with_survival_rate.xlsx'")
