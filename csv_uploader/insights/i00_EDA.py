import json

def calculate_missing_values(df):
    missing_values = df.isnull().sum()  # Calcula los valores ausentes por columna
    total_values = df.shape[0]          # Número total de filas

    # Crea un diccionario con los resultados para cada columna
    missing_data = {}
    for column_name, num_missing in zip(missing_values.index, missing_values.values):
        missing_data[column_name] = {
            'num_missing': num_missing,
            'percent_missing': (num_missing / total_values) * 100
        }

    return missing_data

def prepare_json_EDA(df):

    # Preparar datos para Chart.js
    region_data = df['region'].value_counts().to_dict()

    context = {
        'region_data': json.dumps(region_data)
    }

    return context