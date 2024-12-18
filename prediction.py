import joblib
import pandas as pd
from data_preprocessing import preprocess_data

# Fungsi untuk melakukan prediksi
def prediction(data):
    # Memuat model prediksi yang telah dilatih
    model = joblib.load('model/dropout_predictor_model.joblib')
    
    # Memproses data input menggunakan preprocessing
    data_processed = preprocess_data(data)
    
    # Melakukan prediksi menggunakan model
    prediction = model.predict(data_processed)
    
    # Mengembalikan hasil prediksi (0: Tidak Dropout, 1: Dropout)
    return prediction