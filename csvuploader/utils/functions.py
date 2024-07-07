#%% ################################################# Importaciones #########################################################################################
# Importaciones del sistema
from collections import defaultdict

# Importaciones para procesamiento de texto y comparación difusa
from fuzzywuzzy import process, fuzz

# Importaciones para procesamiento de lenguaje natural (NLP)
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# importaciones para manejo de datos
import pandas as pd

# Descargar recursos de nltk necesarios
nltk.download('wordnet')
nltk.download('omw-1.4')
#%% ################################################# Funciones #########################################################################################
def normalize_descriptions(descriptions):
    ''' 
    Normaliza descripciones convirtiéndolas a minúsculas y lematizándolas.
    
    Args:
    descriptions (list): Lista de descripciones a normalizar.
    
    Returns:
    list: Lista de descripciones normalizadas y lematizadas.
    
    Esta función convierte cada descripción a minúsculas, divide las palabras,
    y luego aplica lematización utilizando el lematizador de WordNet para 
    convertir cada verbo a su forma base.
    '''
    lemmatizer = WordNetLemmatizer()
    normalized_descriptions = []
    for desc in descriptions:
        words = desc.lower().split()
        lemmatized_words = [lemmatizer.lemmatize(word, wordnet.VERB) for word in words]
        normalized_descriptions.append(' '.join(lemmatized_words))
    return normalized_descriptions

def cluster_similar_descriptions(descriptions, threshold=90):
    ''' 
    Agrupa descripciones similares en clusters basados en la similitud de texto.

    Args:
    descriptions (list): Lista de descripciones a agrupar.
    threshold (int, optional): Umbral de similitud mínimo para considerar una coincidencia. 
                               Valor por defecto es 90.

    Returns:
    defaultdict: Diccionario con las descripciones originales como claves y listas 
                 de descripciones similares como valores.

    Esta función encuentra y agrupa descripciones similares en clusters utilizando 
    el algoritmo FuzzyWuzzy. Para cada descripción única, encuentra coincidencias 
    con otras descripciones en la lista basadas en el puntaje de similitud (ratio). 
    Las descripciones que superan el umbral especificado se agrupan bajo una misma clave.
    '''
    unique_descriptions = list(set(descriptions))
    clusters = defaultdict(list)
    visited = set()

    for desc in unique_descriptions:
        if desc in visited:
            continue
        matches = process.extract(desc, unique_descriptions, scorer=fuzz.ratio)
        cluster = [match[0] for match in matches if match[1] >= threshold]
        for item in cluster:
            visited.add(item)
        clusters[desc].extend(cluster)
    return clusters

def determine_canonical_form(clusters, descriptions):
    ''' 
    Determina la forma canónica para cada cluster de descripciones.

    Args:
    clusters (dict): Diccionario donde las claves son las descripciones originales y 
                     los valores son listas de descripciones similares agrupadas.
    descriptions (list): Lista completa de todas las descripciones.

    Returns:
    dict: Diccionario de reemplazo donde las claves son las descripciones similares 
          y los valores son sus formas canónicas correspondientes.

    Esta función recorre cada cluster de descripciones similares y determina la forma 
    canónica para cada uno. La forma canónica es la descripción más frecuente dentro 
    del cluster, calculada a partir de la lista completa de todas las descripciones.
    '''
    replacement_dict = {}
    for key, cluster in clusters.items():
        canonical_form = max(set(cluster), key=descriptions.count)
        for item in cluster:
            replacement_dict[item] = canonical_form
    return replacement_dict

def fill_missing_descriptions(row, mapping_dict):
    """
    Complementa las descripciones faltantes basadas en el código de stock.

    Esta función toma una fila de un DataFrame y un diccionario de mapeo de códigos de stock a descripciones.
    Si la descripción de la fila es NaN, la función busca en el diccionario el código de stock de la fila
    y devuelve la descripción correspondiente. Si la descripción no es NaN, la función devuelve la descripción
    original.

    Args:
    row (pd.Series): Una fila del DataFrame que contiene las columnas 'stock_code' y 'description'.
    mapping_dict (dict): Un diccionario donde las claves son códigos de stock y los valores son descripciones.

    Returns:
    str: La descripción original si no es NaN, o la descripción mapeada a partir del código de stock si la
    descripción original es NaN.
    """
    if pd.isna(row['description']):
        return mapping_dict.get(row['stock_code'], row['description'])
    return row['description']

def order_cluster(cluster_field_name, target_field_name, df, ascending): 
    """
    Reordena los clusters en un DataFrame basándose en la media de un campo objetivo.
    
    Parámetros:
    cluster_field_name (str): El nombre del campo que contiene los clusters.
    target_field_name (str): El nombre del campo objetivo según el cual se ordenarán los clusters.
    df (DataFrame): El DataFrame que contiene los datos a ser reordenados.
    ascending (bool): Indica si el orden debe ser ascendente (True) o descendente (False).

    Retorna:
    DataFrame: Un DataFrame con los clusters reordenados según la media del campo objetivo.
    
    Ejemplo de uso:
    df_ordenado = order_cluster('Cluster', 'AnnualIncome', df, ascending=True)
    """
    new_cluster_field_name = 'new_' + cluster_field_name 
    df_new = df.groupby(cluster_field_name)[target_field_name].mean().reset_index() 
    df_new = df_new.sort_values(by=target_field_name,ascending=ascending).reset_index(drop=True) 
    df_new['index'] = df_new.index 
    df_final = pd.merge(df,df_new[[cluster_field_name,'index']], on=cluster_field_name) 
    df_final = df_final.drop([cluster_field_name],axis=1) 
    df_final = df_final.rename(columns={"index":cluster_field_name}) 
    return df_final 

def treatment_missing_values(df):
    df = df.copy() 

    # Se recuperaran algunos valores ausentes de description usando el stock_code
    # Crear el diccionario de mapeo de stock_code a description
    mapping_dict = df.dropna(subset=['description']).drop_duplicates(subset=['stock_code']).set_index('stock_code')['description'].to_dict()

    # Aplicar la función para rellenar las descripciones faltantes
    df['description'] = df.apply(fill_missing_descriptions, axis=1, args=(mapping_dict,))

    # Eliminar/rellenar valores ausentes
    df_clean = df.dropna(subset=['description'])   # Para la columna descripcion se elimininaran al ser solo el 0.2% de los datos. 
    df_clean = df.fillna('unknown')                # Para la columna customer_id se reemplazaran por la palabra unknown

    return df_clean

def fill_empty_descriptions(df):
    # Eliminar caracteres especiales usando una expresión regular
    df['description'] = df['description'].str.replace(r'[^A-Za-z0-9\s]', '', regex=True)

    # Limpiar la columna 'description' eliminando espacios en blanco y convirtiendo None a cadenas vacías
    df['description'] = df['description'].str.strip()

    # Remplazar cadenas vacias por unknown
    df = df.replace('','unknown')

    return df

def normalized_descriptions(df):
    # Normalizar descripciones
    df['normalized_description'] = normalize_descriptions(df['description'])

    # Crear clusters de frases similares
    clusters = cluster_similar_descriptions(df['normalized_description'])

    # Crear diccionario de reemplazo automáticamente
    replacement_dict = determine_canonical_form(clusters, df['normalized_description'].tolist())

    # Reemplazar las frases en el DataFrame
    df['normalized_description'] = df['normalized_description'].replace(replacement_dict)

    # Eliminar la columna description
    df.drop(column='description', inplace=True)

    return df
