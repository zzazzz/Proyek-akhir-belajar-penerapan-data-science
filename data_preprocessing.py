import pandas as pd
import joblib
from outlierhandler import OutlierHandler

# Muat model dan encoder saat aplikasi dimulai
outlier_handler = joblib.load('model/outlier_handler_pipeline.joblib')
encoders = joblib.load('model/encoder.joblib')

def preprocess_data(form_input):
    # Buat dataframe dari input form
    data_df = pd.DataFrame([form_input])
    
    # Tangani outlier
    columns_to_process = [
        'Admission_grade', 'Age_at_enrollment',
        'Curricular_units_1st_sem_enrolled', 'Curricular_units_1st_sem_evaluations',
        'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade',
        'Curricular_units_2nd_sem_enrolled', 'Curricular_units_2nd_sem_evaluations',
        'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade'
    ]

    data_df[columns_to_process] = outlier_handler.transform(data_df[columns_to_process])
    
    # Encoding kategori
    category_cols = data_df.select_dtypes(include=['category', 'object']).columns.tolist()
    for col in category_cols:
        encoder = encoders[col]
        data_df[col] = encoder.transform(data_df[col])
    
    return data_df