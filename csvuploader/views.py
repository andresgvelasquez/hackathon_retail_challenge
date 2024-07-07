from django.shortcuts import render

from .forms import CSVUploadForm
from .preprocessing.p00_preprocessing import preprocess_csv
from .preprocessing.p01_feat_eng import feature_engineering
from utils.functions import save_to_mysql

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            
            # Limpieza del CSV
            df_clean = preprocess_csv(csv_file)
            
            # Feature engineering
            df_feat_eng = feature_engineering(df_clean)

            # Enviar el dataframe a la base de datos mysql
            save_to_mysql(df_clean, 'nombre_de_tu_tabla')

            return render(request, 'csvuploader/upload_success.html', {'df_clean': df_feat_eng})
    else:
        form = CSVUploadForm()
    
    return render(request, 'csvuploader/upload_csv.html', {'form': form})