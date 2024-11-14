import pandas as pd

# Load the data
data = pd.read_excel('app/data/dataset_randomized.xlsx')

# Define a function to calculate survival rate based on TDS and pH
def calculate_survival_rate(row):
    # Check if data falls outside the normal range (anomalies)
    if row['TDS'] < 300 or row['TDS'] > 600 or not (7.8 <= row['pH'] <= 8.5):
        return 20  # Low survival rate for anomalous conditions
    elif 500 <= row['TDS'] <= 600 and 7.8 <= row['pH'] <= 8.5:
        return 80  # High survival rate for ideal conditions
    elif 300 <= row['TDS'] < 500 and 7.8 <= row['pH'] <= 8.5:
        return 50  # Medium survival rate for acceptable conditions
    else:
        return 20  # Default to low survival rate for any other cases

# Apply the function to each row in the dataset
data['Survival Rate'] = data.apply(calculate_survival_rate, axis=1)

# Save the modified dataset to a new file
data.to_excel('app/data/dataset_filled.xlsx', index=False)
print("Data with Survival Rate has been saved to 'app/data/dataset_filled.xlsx'")

# Anomali: Survival Rate 20 jika:
# TDS < 300 atau TDS > 600, atau
# pH di luar rentang 7.8 hingga 8.5

# Kondisi Ideal: Survival Rate 80 jika:
# 500 <= TDS <= 600 dan 7.8 <= pH <= 8.5

# Kondisi Diterima: Survival Rate 50 jika:
# 300 <= TDS < 500 dan 7.8 <= pH <= 8.5