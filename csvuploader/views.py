from django.shortcuts import render
from django.conf import settings
import pandas as pd

from .forms import CSVUploadForm
from .preprocessing.p00_preprocessing import preprocess_csv
from .preprocessing.p01_feat_eng import feature_engineering

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            
            # Limpieza del CSV
            df_clean = preprocess_csv(csv_file)
            
            # Feature engineering
            df_feat_eng = feature_engineering(df_clean)

            # Aquí podrías guardar df_clean en la base de datos si es necesario
            
            return render(request, 'csvuploader/upload_success.html', {'df_clean': df_feat_eng})
    else:
        form = CSVUploadForm()
    
    return render(request, 'csvuploader/upload_csv.html', {'form': form})