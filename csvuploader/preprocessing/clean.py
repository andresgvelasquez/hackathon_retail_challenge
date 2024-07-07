import pandas as pd
import chardet
def preprocess_csv(csv_file):
    # Leer el archivo CSV en un DataFrame de pandas
    # Intenta con diferentes encodings si 'utf-8' falla
    #raw_data = csv_file.read()
    #result = chardet.detect(raw_data)
    #encoding = result['encoding']
    #print(f"El encoding detectado es: {encoding}")
    #csv_file.seek(0)
    #unicode_escape
    #ISO-8859-1
    df = pd.read_csv(csv_file, encoding='ISO-8859-1', encoding_errors='replace')  # Otro encoding comúnmente usado

    # Realizar cualquier manipulación necesaria
    # Por ejemplo, eliminar filas con valores nulos
    df_clean = df.dropna()
    # Otra posible manipulación de datos, como cambiar el formato de fecha, etc.

    return df_clean.head()