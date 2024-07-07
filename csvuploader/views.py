from django.shortcuts import render
from django.conf import settings
import pandas as pd

from .forms import CSVUploadForm
from .preprocessing.clean import preprocess_csv  # Ajusta según la ubicación real de tu función de preprocesamiento

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            
            # Procesamiento del CSV
            df_clean = preprocess_csv(csv_file)
            
            # Aquí podrías guardar df_clean en la base de datos si es necesario
            
            return render(request, 'csvuploader/upload_success.html', {'df_clean': df_clean})
    else:
        form = CSVUploadForm()
    
    return render(request, 'csvuploader/upload_csv.html', {'form': form})