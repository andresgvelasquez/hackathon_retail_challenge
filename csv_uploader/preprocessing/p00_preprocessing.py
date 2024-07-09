import pandas as pd

from ..utils.functions import clean_outliners, fill_empty_descriptions, normalized_descriptions, treatment_missing_values # Funciones locales

def preprocess_csv(csv_file, normalize_description=False, outliners=False):

    # lectura del dataframe 
    df = pd.read_csv(csv_file, encoding='ISO-8859-1', encoding_errors='replace')  

    # Pasar el nombre de las columnas a mínusculas y dejarlo en snake_case
    df.columns = df.columns.str.lower()

    # Tratamiento de valores ausentes
    df_without_nan = treatment_missing_values(df)

    # Rellenar descripciones vacias (compuestas por caracteres especiales solamente)
    df_clean = fill_empty_descriptions(df_without_nan)
    
    # Pasar la columna invoice_date a tipo datetime
    df_clean['invoice_date'] = pd.to_datetime(df_clean['invoice_date'], format='%d/%m/%Y %H:%M', errors='coerce')

    # Eliminar duplicados explicitos
    df_clean.drop_duplicates(inplace=True)

    # Normalizar descripciones 
    if normalize_description:
        df_clean = normalized_descriptions(df_clean)

    # Eliminar valores atípicos para quantity y unit_price
    if outliners:
        df_clean = clean_outliners(df_clean, 'quantity')
        df_clean = clean_outliners(df_clean, 'unit_price')

    return df_clean