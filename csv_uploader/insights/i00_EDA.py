import json

def prepare_json_EDA(df):

    # Preparar datos para Chart.js
    quantity_data = df['quantity'].tolist()
    unit_price_data = df['unit_price'].tolist()
    region_data = df['region'].value_counts().to_dict()

    context = {
        'quantity_data': json.dumps(quantity_data),
        'unit_price_data': json.dumps(unit_price_data),
        'region_data': json.dumps(region_data)
    }