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

# Save the updated DataFrame to a new Excel file
df.to_excel('app/data/dataset_with_survival_rate.xlsx', index=False)
print("Data with survival rate has been saved to 'app/data/dataset_with_survival_rate.xlsx'")
