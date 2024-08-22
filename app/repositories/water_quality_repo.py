import csv

def fetch_all_water_quality_data():
    """
    Fetch all water quality data from a CSV file.

    :return: List of dictionaries containing water quality data
    """
    data = []
    file_path = 'app/data/dataset.csv'  # Update with the correct path

    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append({
                'do': float(row['DO']),
                'ph': float(row['pH']),
                'temperature': float(row['Water Temperature']),
                'turbidity': float(row['Turbidity']),
                'survival_rate': float(row['Survival Rate'])
            })

    return data
