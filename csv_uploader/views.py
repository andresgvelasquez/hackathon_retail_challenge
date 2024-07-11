from django.shortcuts import render

from .forms import CSVUploadForm
from .preprocessing.p00_preprocessing import preprocess_csv
from .preprocessing.p01_feat_eng import feature_engineering
from .utils.functions import save_to_postgres
from .insights.i00_EDA import prepare_json_EDA

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']

            # Limpieza del CSV
            df_clean, missing_data = preprocess_csv(csv_file)
            
            # Feature engineering
            df_feat_eng = feature_engineering(df_clean)

            # Enviar el dataframe a la base de datos mysql
            save_to_postgres(df_feat_eng, 'online_retail')

            # Convertir EDA en json para mostralo en la web
            context = prepare_json_EDA(df_feat_eng)
            context['missing_data'] = missing_data
            #return render(request, 'csvuploader/upload_success.html', {'df_clean': df_feat_eng})
            return render(request, 'csvuploader/eda_template.html', context)
    else:
        form = CSVUploadForm()
    
    return render(request, 'csvuploader/upload_csv.html', {'form': form})
    #return render(request, 'csvuploader/upload_csv.html')